# Feature Specification: F076 - Habit Tracking and Streaks

## 1. Feature Identification
* **Feature ID**: `F076`
* **Feature Name**: Habit Creation, Daily Check-in & Streak Engine
* **Domain**: Habit Tracking
* **Evidence Standard**: `[CODE-CONFIRMED]` via REA JADX / `HabitDao` / `HabitCheckInDao` / `AllHabitListActivity`

---

## 2. Functional Description
Enables users to build positive routines by defining recurring habits with customizable frequencies (Daily, Weekly, Interval), quantitative daily targets (e.g. 2000 ml water, 30 pages reading), one-tap completion rings, monthly completion heatmaps, and streak tracking.

---

## 3. Entry Points & User Invocations
1. Habits Tab on primary bottom navigation bar (`AllHabitListActivity`).
2. Add Habit button (+) on Habit Dashboard (`HabitAddActivity`).
3. Today list view (if `prefkey_habit_show_in_today` is enabled).
4. Home screen Habit Widget (`AppWidgetHabitConfigActivity`).

---

## 4. Input Fields & Configuration Properties
| Property | Type | Required | Default Value | Description & Options |
| :--- | :--- | :--- | :--- | :--- |
| `name` | Text | Yes | `""` | Name of habit (e.g. "Read Book", "Meditation"). Max 64 chars. |
| `icon` | String | Yes | `"ic_habit_default"` | Habit icon identifier from 60+ vector icon catalog. |
| `color` | String (Hex) | Yes | `"#2196F3"` | Color theme assigned to the habit ring and card. |
| `frequencyType`| Integer | Yes | `0` (Daily) | `0` = Daily, `1` = Specific Days of Week, `2` = X times per Week/Month. |
| `frequencyDays`| Bitmask/Array | No | `[1,2,3,4,5,6,7]`| Active days of the week (Mon=1 ... Sun=7). |
| `goalType` | Integer | Yes | `0` (Check-off) | `0` = Simple check-off, `1` = Quantitative Target. |
| `targetValue` | Double | No | `1.0` | Target metric value (e.g. `2000.0` for water, `30.0` for minutes). |
| `unit` | Text | No | `""` | Unit of measurement (e.g. "ml", "pages", "min", "km"). |
| `reminders` | Array | No | `["08:00"]` | Daily reminder times for habit notification prompts. |
| `sectionId` | String | No | `"default"` | Category grouping (e.g. Morning Routine, Evening Routine). |

---

## 5. Free vs. Pro Limitations
* **Free Tier**: Maximum **5 Active Habits**.
* **Pro Tier**: **Unlimited Active Habits**. Full historical calendar heatmap beyond 30 days.

---

## 6. Habit Check-in UI & Micro-Interaction
```
+-------------------------------------------------------+
|  [ICON]  Drink 2,000 ml Water                         |
|  Streak: 14 Days [FLAME] | Target: 1,500 / 2,000 ml   |
|                                                       |
|                     [ ( 75% ) ]                       |
|                 Tap to add 250 ml                     |
+-------------------------------------------------------+
```

* **Tap Action**:
  * For simple check-off habits: One tap fills the ring to 100%, draws checkmark, plays chime, fires haptic pulse, and increments streak count.
  * For quantitative habits: Tapping adds the configured incremental step value (e.g. +250 ml). Reaching `targetValue` marks the daily goal complete.
* **Long Press Action**:
  * Opens check-in log sheet (`activity_habit_record.xml`) allowing manual entry of exact value, diary journal text, and photo attachment.

---

## 7. Data Model & Database Persistence
```sql
-- Habit Entity Definition
INSERT INTO HABIT (
    SID, NAME, ICON, COLOR, FREQUENCY_TYPE, TARGET_VALUE, UNIT, 
    STATUS, CREATED_TIME, SORT_ORDER
) VALUES (
    'habit_water_123',
    'Drink Water',
    'ic_habit_water',
    '#2196F3',
    0,
    2000.0,
    'ml',
    0,
    1714980000000,
    100
);

-- Check-in Record for Today
INSERT INTO HABIT_CHECK_IN (
    SID, HABIT_ID, CHECK_IN_DATE, VALUE, NOTE, CREATED_TIME
) VALUES (
    'checkin_uuid_456',
    'habit_water_123',
    '2026-11-13',
    500.0,
    'Drank bottle after morning workout',
    1715012400000
);
```

---

## 8. Streak Recalculation Algorithm
```python
def calculate_streak(habit_id, check_in_dates, scheduled_days):
    """
    Computes current continuous streak.
    scheduled_days: set of weekday integers (e.g. {1, 3, 5} for Mon/Wed/Fri)
    """
    streak = 0
    current_day = today()
    
    # If today has not been checked in yet, check if yesterday was valid
    if current_day not in check_in_dates:
        current_day = current_day - 1 day
        
    while True:
        # If current_day is not a scheduled day, skip it without breaking streak
        if current_day.weekday() not in scheduled_days:
            current_day = current_day - 1 day
            continue
            
        if current_day in check_in_dates:
            streak += 1
            current_day = current_day - 1 day
        else:
            break
            
    return streak
```

---

## 9. Verification & Test Criteria
1. Create a habit with Mon/Wed/Fri schedule. Verify it only prompts reminders on those specific days.
2. Complete habit for 3 consecutive scheduled days. Verify streak counter displays 3 with flame icon.
3. Test Free tier habit limit: Create 5 habits. Attempting to create the 6th habit must trigger `GetProActivity`.

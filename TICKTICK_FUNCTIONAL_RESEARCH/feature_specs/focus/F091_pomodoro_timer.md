# Feature Specification: F091 - Focus and Pomodoro Engine

## 1. Feature Identification
* **Feature ID**: `F091`
* **Feature Name**: Pomodoro Timer, Stopwatch & Focus Analytics
* **Domain**: Focus & Productivity
* **Evidence Standard**: `[CODE-CONFIRMED]` via REA JADX / `PomodoroDao` / `PomodoroActivity` / `FloatingPomoService`

---

## 2. Functional Description
Implements the Pomodoro Technique and open-ended focus stopwatch tracking. Features rotary dial duration adjustment, task association, white noise audio playback, Strict Mode app lock, flip-to-focus accelerometer triggers, floating PiP timer ball, and daily/weekly focus analytics.

---

## 3. Entry Points & User Invocations
1. Focus Tab on primary bottom navigation bar (`PomodoroActivity`).
2. Swipe action "Start Pomo" on any task row in `TaskListFragment`.
3. Task detail menu option: "Start Focus".
4. Deep Link URI: `ticktick://focus/start?taskId=...&duration=25`.

---

## 4. Focus Modes & Configurations
| Parameter | Default | Configurable Range | Description |
| :--- | :--- | :--- | :--- |
| **Timer Mode** | Pomodoro | Pomodoro (Countdown) vs. Stopwatch (Countup) | Switchable via top toggle bar. |
| **Focus Duration** | 25 min | 5 min to 180 min | Configurable in increments of 5 minutes via dial drag. |
| **Short Break** | 5 min | 1 min to 30 min | Rest duration between standard focus sessions. |
| **Long Break** | 15 min | 5 min to 60 min | Rest duration after completing a cycle of Pomodoros. |
| **Long Break Interval** | 4 sessions | 2 to 8 sessions | Number of completed Pomodoro sessions before long break. |
| **Auto-Start Break** | `false` | `true` / `false` | Automatically starts break countdown when focus ends. |
| **Strict Mode** | `false` | `true` / `false` | Locks user within TickTick; penalizes app switches as interruptions. |
| **Flip to Focus** | `true` | `true` / `false` | Turning phone facedown on a desk starts the timer. |

---

## 5. Focus Screen Interface & Micro-Interactions
```
+-------------------------------------------------------+
|  [ POMODORO ]               |        [ STOPWATCH ]    |
|                                                       |
|                     . - ~ ~ - .                       |
|                 . '             ' .                   |
|               /      25 : 00        \                 |
|              |   Writing Article     |                |
|               \                     /                 |
|                 . '             ' .                   |
|                     ' - ~ ~ - '                       |
|                                                       |
|        [ SOUND: Rain ]          [ STRICT MODE: Off ]  |
|                                                       |
|                      [ START ]                        |
+-------------------------------------------------------+
```

* **Rotary Dial Physics**: Dragging the circular bead rotates the countdown duration smoothly, updating the central minutes counter with subtle click haptic feedback at each minute mark.
* **Flip-to-Focus**: Uses `Sensor.TYPE_ACCELEROMETER`. Resting the device horizontally face-down triggers a 100ms vibration and starts countdown automatically.
* **OLED Anti-Burn-In**: Fullscreen dark mode jitters digital clock coordinates by ±3px every 60 seconds to protect AMOLED displays.
* **Floating Timer Ball**: When backgrounded with `SYSTEM_ALERT_WINDOW` permission, renders a small circular countdown widget that docks against screen edges.

---

## 6. Data Model & Database Persistence
```sql
INSERT INTO POMODORO (
    SID, START_TIME, END_TIME, DURATION, TASK_ID, 
    STATUS, INTERRUPTION_COUNT, IS_MANUAL
) VALUES (
    'pomo_session_789',
    1715011200000,
    1715012700000,
    1500, -- 25 minutes in seconds
    'task_article_uuid',
    1, -- STATUS_FINISHED
    0,
    0
);
```

---

## 7. Verification & Test Criteria
1. Start a 25-minute Pomodoro with Rain ambient noise. Verify audio loops continuously with screen turned off.
2. Verify session completion triggers `PomoPopupActivity` with sound chime and option to "Start 5 min Break".
3. Verify completed session increments the associated task's total focus time and appears in `FocusTimelineActivity`.
4. Enable Strict Mode; verify switching to another non-whitelisted app displays warning overlay and logs an interruption.

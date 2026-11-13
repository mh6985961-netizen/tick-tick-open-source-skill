# Screen Specification: SCR-HAB-001 - Habit Dashboard

### Screen ID
`SCR-HAB-001`

### Screen Name
Habit Dashboard & Grid (`AllHabitListActivity`)

### Purpose
Central interface for monitoring active daily habits, tracking ongoing streaks, executing one-tap completions, and reviewing current progress towards daily routines.

### Entry Points
1. "Habits" tab on the primary bottom navigation bar (`TabBar`).
2. Habit home screen widget tap action (`AppWidgetHabitConfigActivity`).
3. Deep link: `ticktick://habit/dashboard`.

### Screen Contents
* **Top Header Bar**:
  * Title: "Habits".
  * Section Selector / Filter dropdown (All, Morning, Afternoon, Evening).
  * Right Action Buttons: Calendar View toggle, Section Manage button, Add Habit (+).
* **Weekly Date Strip**:
  * Horizontal scrolling 7-day strip displaying weekdays and dates, with dots indicating completion status across all habits for past days.
* **Habit List / Grid (`habit_rv`)**:
  * Categorized by sections (e.g. "Morning Routine", "Afternoon", "Evening Routine").
  * **Habit Card Item**:
    * Habit Category Icon (Vector icon with habit color background).
    * Habit Title (e.g. "Drink Water", "Read 30 mins").
    * Streak Counter with Flame Icon (e.g. "14 Days Streak").
    * Target Progress Metric (e.g., "1,500 / 2,000 ml" or "Check-off").
    * **Circular Progress Ring / Check Button**:
      * Circular hit target rendering current completion percentage.
      * Tapping fills the circle with checkmark animation and particle burst.

### Available Actions
1. **Single Tap on Circular Ring**: Executes daily check-in (marks completed or adds increment).
2. **Long Press on Habit Card**: Opens `SCR-HAB-005` (Habit Check-in Record / Log Note sheet).
3. **Single Tap on Habit Card Title**: Opens `SCR-HAB-004` (Habit Detail & Calendar Heatmap).
4. **Tap Add (+) Button**: Navigates to `SCR-HAB-002` (Habit Creation & Presets).
5. **Drag Card**: Reorder habits manually within sections.

### Interaction Behavior
* Completing a habit triggers:
  * Circular stroke sweeps to 100% via overshoot interpolator (350ms).
  * Plays audio chime (`habit_complete.ogg`).
  * Emits tactile vibration (`long[] {0, 80, 50, 80}`).
  * Streak counter increments with vertical roll animation.

### Input Fields
* No direct text inputs on the dashboard surface.

### Navigation
* Tapping habit card navigates to `SCR-HAB-004` (`HabitDetailActivity`).
* Tapping (+) navigates to `SCR-HAB-002` (`HabitAddActivity`).
* Tapping Section Manager navigates to `HabitSectionManageActivity`.

### Different States
* **Default State**: Lists active habits grouped by section with completion status for selected date.
* **All Done State**: When all habits for the day are checked, displays celebratory card: *"You've completed all habits today! Keep it up!"*.
* **Empty State**: Displays welcoming illustration (`img_empty_habit.png`), copy: *"Build a positive routine. Track your first habit."*, and a large "Add Habit" action button.

### Data Requirements
* Active `HABIT` rows where `STATUS = 0` (Active).
* `HABIT_CHECK_IN` records matching selected date.

### Related Features
* Habit Creation (`F076`), Habit Streaks (`F077`), Habit Heatmap (`F081`).

### Subscription Restrictions
* Free tier limits user to **5 active habits**. Attempting to add a 6th habit prompts `GetProActivity`.

### Evidence
* `com.ticktick.task.activity.habit.AllHabitListActivity`
* `res/layout/activity_habit_all_list.xml`
* `res/layout/item_habit_row.xml`

### Confidence
Confirmed `[CODE-CONFIRMED]`.

### Unknowns
* None; decompiled habit activity verified.

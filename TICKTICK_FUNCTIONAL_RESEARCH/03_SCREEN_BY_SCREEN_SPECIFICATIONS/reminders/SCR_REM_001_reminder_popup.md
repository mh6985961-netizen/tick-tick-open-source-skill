# Screen Specification: SCR-REM-001 - Fullscreen Alarm & Persistent Alert

### Screen ID
`SCR-REM-001`

### Screen Name
Fullscreen Alarm Window (`ReminderPopupActivity`)

### Purpose
Implements the high-urgency, lockscreen-surviving alarm display fired when a scheduled task alarm or Annoying Alert triggers, demanding immediate user interaction (Complete, Snooze, Won't Do).

### Entry Points
1. `AlarmManager` wake-up intent via `ReminderReceiver` when a task alarm triggers.
2. `AlertActionDispatchActivity` invoking fullscreen intent on lockscreen.

### Screen Contents
* **Window Configuration**:
  * Configured with `WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED` and `FLAG_TURN_SCREEN_ON`.
  * Background: Dark semi-transparent blur or primary theme background.
* **Header Area**:
  * Current Time in large digital clock font (e.g. `16:30`).
  * Current Date (e.g. "Friday, November 13").
  * Project / List tag pill (e.g. "Work").
* **Central Task Card**:
  * High-contrast Task Title in prominent 22sp bold text.
  * Checklist Preview: Shows up to 3 checklist items if the task contains subtasks.
  * Task Description snippet (if present).
  * Priority flag banner.
* **Action Buttons Bar**:
  * **[ COMPLETE ]** (Large Green button with Checkmark).
  * **[ SNOOZE ]** (Large Blue button with Snooze Clock icon).
  * **[ WON'T DO ]** (Secondary outline button with Circle-Slash).
  * **"Open in App"** link button at bottom.

### Available Actions
1. **Tap "Complete"**: Marks task status `COMPLETED (2)`; terminates alarm audio; dismisses window.
2. **Tap "Snooze"**: Opens `SCR-REM-002` (`SnoozePopupActivity`) or applies default 15-minute snooze interval; reschedules alarm; terminates audio; dismisses window.
3. **Tap "Won't Do"**: Marks task status `WON'T DO (3)`; terminates audio; dismisses window.
4. **Tap "Open in App"**: Unlocks device and navigates directly to `SCR-TASK-002` (`TaskDetailActivity`).

### Interaction Behavior
* Plays continuous looping ringtone (`AudioManager.STREAM_ALARM`) and vibrates device motor until one of the primary action buttons is tapped.
* If Annoying Alert is enabled (Pro), ignoring the alarm will re-trigger the fullscreen popup every 2 minutes.

### Input Fields
* No text inputs on this alert surface.

### Navigation
* Actions dismiss the window; tapping "Open in App" leads to `TaskDetailActivity`.

### Different States
* **Single Task Alarm State**: Normal view as described above.
* **Multi-Task Alarm State**: If multiple tasks are scheduled for the exact same minute, displays a swipeable pager of cards with "Complete All" and "Snooze All" options.

### Data Requirements
* Task `SID` passed via Intent Extra.
* Query `Tasks2` and `CHECKLIST_ITEM` rows from SQLite.

### Related Features
* Reminders (`F036`), Annoying Alert (`F040`), Snooze (`F039`).

### Subscription Restrictions
* Persistent repeating loop ("Annoying Alert") is restricted to Pro tier.

### Evidence
* `com.ticktick.task.activity.ReminderPopupActivity`
* `res/layout/activity_reminder_popup.xml`

### Confidence
Confirmed `[CODE-CONFIRMED]`.

### Unknowns
* None; verified in decompiled reminder receiver and activity code.

# Screen Specification: SCR-CAL-001 - Calendar Multi-View Container

### Screen ID
`SCR-CAL-001`

### Screen Name
Calendar Multi-View Container (`CalendarViewActivity`)

### Purpose
Provides a comprehensive scheduling hub where tasks and external calendar events are unified across Month, Week, Day, 3-Day, and Agenda layouts with direct drag-and-drop time blocking.

### Entry Points
1. "Calendar" tab on bottom navigation bar (`TabBar`).
2. Tapping a calendar shortcut widget on Android home screen.
3. Deep link: `ticktick://calendar`.

### Screen Contents
* **Top App Bar**:
  * Left Navigation Hamburger (drawer toggle).
  * Center Date Title (e.g., "November 2026") with mini-calendar picker dropdown.
  * Right Action Buttons: Today button (Calendar icon with current day number), View Mode Switcher icon, Calendar Manager (Subscriptions).
* **View Mode Sub-Header Tabs**:
  * Segmented tabs: **[ MONTH ] [ WEEK ] [ 3-DAY ] [ DAY ] [ AGENDA ]**.
* **Primary Viewport Area**:
  * Dynamically hosts the selected calendar view fragment:
    * **Month Grid**: 7x6 month table with colored task chips in day cells.
    * **Week / 3-Day / Day Grids**: Vertical 24-hour time axes with event rectangles rendered according to `START_TIME` and `DUE_DATE`. All-day tasks span across the top banner.
    * **Agenda Feed**: Continuous chronological list of tasks grouped by date headers.
* **Expandable Unscheduled Tasks Drawer**:
  * Bottom pull-up tray listing all tasks scheduled for the date without specific times, ready for drag-and-drop placement onto the hourly grid.

### Available Actions
1. Switch between Month, Week, 3-Day, Day, and Agenda views.
2. Tap "Today" to jump to current date.
3. Drag unscheduled task chip from tray onto time block on Day/Week grids.
4. Drag bottom resize handle of an event block to adjust duration.
5. Tap any task or external event to open its detail sheet.
6. Tap "+" to create a new task or calendar event pre-filled with the selected date/hour.

### Interaction Behavior
* Dragging an unscheduled task onto the timeline snaps to 15-minute intervals with haptic feedback, instantly updating `Tasks2.START_TIME` and `Tasks2.DUE_DATE`.

### Input Fields
* No text input directly on the calendar surface; creation opens Quick Add or Event dialog.

### Navigation
* Tapping a task navigates to `SCR-TASK-002` (`TaskDetailActivity`).
* Tapping Calendar Manager navigates to `SCR-CAL-003` (`CalendarManagerActivity`).
* Tapping Calendar Options navigates to `CalendarViewOptionsActivity`.

### Different States
* **Default State**: Renders scheduled tasks and synced external calendar events.
* **Empty Time Slot**: Tapping an empty slot highlights a 30-minute block and opens quick event creation modal.

### Data Requirements
* Active date range (start timestamp to end timestamp).
* `Tasks2` rows within date range.
* External `CalendarContract` event rows from Android provider.

### Related Features
* Calendar Multi-Views (`F056`), Drag Scheduling (`F060`), External Sync (`F063`).

### Subscription Restrictions
* Free tier is restricted to **Agenda view** and limited Day view.
* Pro tier unlocks **Month, Week, 3-Day views**, two-way sync, and URL subscriptions.

### Evidence
* `com.ticktick.task.activity.CalendarViewActivity`
* `res/layout/activity_calendar_view.xml`

### Confidence
Confirmed `[CODE-CONFIRMED]`.

### Unknowns
* None; verified in decompiled calendar views.

# Feature Specification: F058 - Calendar Multi-Views & Scheduling

## 1. Feature Identification
* **Feature ID**: `F058`
* **Feature Name**: Calendar Multi-View Engine & Direct Scheduling
* **Domain**: Calendar System
* **Evidence Standard**: `[CODE-CONFIRMED]` via REA JADX / `CalendarViewActivity` / `CalendarViewOptionsActivity`

---

## 2. Functional Description
Unified calendar system displaying scheduled tasks and external calendar events across 5 viewing modes: Month, Week, Day, 3-Day, and Agenda. Features direct drag-and-drop scheduling of unscheduled tasks from a bottom tray onto hourly time blocks, duration handle resizing, external calendar integration (Google, Outlook, Exchange, iCloud, CalDAV), and academic timetable schedules.

---

## 3. Entry Points & User Invocations
1. Calendar Tab on primary bottom navigation bar (`CalendarViewActivity`).
2. Date picker modal "View in Calendar" shortcut.
3. Android Home Screen Month/Week/Today Calendar Widgets.
4. Deep Link URI: `ticktick://calendar?view=month`.

---

## 4. Multi-View Specifications
* **Month View**: 7x5 or 7x6 monthly grid displaying day cells with task pills, color-coded by project/list. Tapping a day cell expands a bottom agenda sheet showing tasks for that selected date.
* **Week View (7 Days)**: Horizontal multi-column timeline grid with hourly horizontal lines (00:00 to 24:00, or user configured range e.g. 08:00 to 22:00). Shows all-day events across the top banner.
* **Day & 3-Day Views**: High-granularity vertical timelines with 15-minute snapping increments. Unscheduled tasks appear in an expandable bottom drawer ("Unscheduled").
* **Agenda View**: Chronological continuous scrolling feed grouped by date headers ("Today", "Tomorrow", "Thursday, Nov 15").

---

## 5. Direct Drag-and-Drop Scheduling
* **Unscheduled Tray**: Bottom drawer queries tasks where `ALL_DAY = 1` or `DUE_DATE IS NULL`.
* **Dragging Chip**: Holding an unscheduled task chip elevates it and allows dropping onto an hourly block on Day/Week views.
* **Drop Mutation**: Sets `Tasks2.START_TIME` and `Tasks2.DUE_DATE`.
* **Duration Resize**: Dragging the bottom edge of an event block stretches its time block, updating duration in increments of 15 minutes.

---

## 6. Free vs. Pro Limitations
* **Free Tier**: Basic Agenda view and limited Day view.
* **Pro Tier**: Full Month, Week, 3-Day, and Day views. Two-way external calendar sync. URL `.ics` WebCal subscriptions.

# Functional Requirements Document (FRD)

## 1. System Scope & Core Requirements

This document defines the functional requirements and acceptance criteria for building the open-source alternative application.

---

## 2. Detailed Functional Requirements by Module

### 2.1 Task Management (FR-TASK)
* **FR-TASK-01**: The system shall support creating tasks with title (mandatory), description (optional markdown), due date/time (optional), priority flag (None, Low, Medium, High), and list assignment.
* **FR-TASK-02**: The system shall support hierarchical subtasks (checklist items) with independent completion states and progress indicators.
* **FR-TASK-03**: The system shall support custom manual drag-and-drop reordering when Sort Mode is set to Custom Sorting.
* **FR-TASK-04**: The system shall provide customizable left and right swipe gestures on task rows supporting Complete, Due Date, Priority, Pin, Won't Do, and Delete.
* **FR-TASK-05**: The system shall provide batch multi-select operations allowing bulk edits to due dates, priorities, lists, and deletions.

### 2.2 Recurrence Engine (FR-REC)
* **FR-REC-01**: The system shall evaluate recurrence rules defined in RFC-5545 iCalendar syntax (`FREQ=DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`).
* **FR-REC-02**: The system shall support recurrence from Due Date (`repeatFrom = 0`) and recurrence from Completion Date (`repeatFrom = 1`).
* **FR-REC-03**: The system shall clamp month-end dates to the last day of shorter months (e.g., 31st clamping to Feb 28/29 or Apr 30).
* **FR-REC-04**: The system shall support skipping specific occurrences without terminating the recurrence chain, logging skipped dates in `EX_DATE`.

### 2.3 Reminders & Alarms (FR-REM)
* **FR-REM-01**: The system shall schedule exact notifications using platform alarm mechanisms, guaranteed to wake up during battery optimization / Doze mode.
* **FR-REM-02**: The system shall support relative reminder offsets (0 min, 5 min, 15 min, 30 min, 1 hour, 1 day before).
* **FR-REM-03**: The system shall automatically re-register upcoming alarms following system reboot or timezone transitions.
* **FR-REM-04**: The system shall provide notification actions (Complete, Snooze, Won't Do) executable directly from the notification shade without opening the UI.

### 2.4 Calendar System (FR-CAL)
* **FR-CAL-01**: The system shall render scheduled tasks and external calendar events across Month, Week, Day, 3-Day, and Agenda layouts.
* **FR-CAL-02**: The system shall allow direct drag-and-drop scheduling of unscheduled tasks from a bottom tray onto the hourly Day/Week grid, snapping to 15-minute intervals.
* **FR-CAL-03**: The system shall allow duration resizing by dragging the bottom edge of calendar time blocks.

### 2.5 Habit Tracking (FR-HAB)
* **FR-HAB-01**: The system shall support creating habits with frequency rules (Daily, Specific Days of Week, Monthly), custom icons, colors, and daily quantitative targets.
* **FR-HAB-02**: The system shall support one-tap check-in with circular animation and celebratory haptics.
* **FR-HAB-03**: The system shall calculate consecutive active streaks based strictly on scheduled days, allowing retroactive check-ins to repair broken streaks.

### 2.6 Focus & Pomodoro (FR-FOC)
* **FR-FOC-01**: The system shall provide a rotary dial countdown Pomodoro timer and an open-ended countup stopwatch.
* **FR-FOC-02**: The system shall support playing seamless looping ambient white noise audio during active sessions.
* **FR-FOC-03**: The system shall detect facedown phone orientation via accelerometer to automatically trigger Flip-to-Focus countdowns.
* **FR-FOC-04**: The system shall log completed focus durations to local database storage linked to specific tasks.

### 2.7 Prioritization (FR-MAT)
* **FR-MAT-01**: The system shall render an Eisenhower 2x2 decision matrix mapping tasks into 4 quadrants based on urgency and importance.
* **FR-MAT-02**: Dragging tasks between quadrants shall automatically update the task's priority and due date according to quadrant rules.
* **FR-MAT-03**: The system shall allow users to customize quadrant filter rules combining priority, due dates, projects, and tags.

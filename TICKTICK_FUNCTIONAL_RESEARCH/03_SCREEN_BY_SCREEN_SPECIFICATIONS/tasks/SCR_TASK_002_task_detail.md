# Screen Specification: SCR-TASK-002 - Task Detail View

### Screen ID
`SCR-TASK-002`

### Screen Name
Task Detail Screen (`TaskDetailActivity`)

### Purpose
Provides full inspection and editing capabilities for every property, subtask, attachment, and comment associated with a specific task entity.

### Entry Points
1. Tapping any task item card in `SCR-TASK-001` (`TaskListFragment`).
2. Tapping a task block in Calendar multi-views (`SCR-CAL-001`).
3. Tapping a task row in Eisenhower Matrix quadrants (`SCR-MAT-001`).
4. Notification shade tap action or Deep Link (`ticktick://task/open?id={sid}`).

### Screen Contents
* **Top Navigation Bar**:
  * Back navigation arrow.
  * Project / List selector button (shows folder/list title and color indicator).
  * Overflow menu (3 vertical dots): Duplicate, Pin to Top, Copy Link, Share as Image/Text, Convert to Note, Task Activities (History), Delete.
* **Header Area**:
  * Large Completion Checkbox button.
  * Task Title `EditText` (multiline, auto-growing).
* **Metadata Action Row**:
  * **Due Date Chip**: Displays scheduled date/time or "Set Due Date" (Calendar Clock icon).
  * **Reminder Chip**: Shows active reminder count/times (Bell icon).
  * **Priority Flag**: Toggles High (Red), Medium (Orange), Low (Blue), None (Grey).
  * **Tag Pill Container**: Horizontal list of attached tags with "+" tag adder.
* **Content Body**:
  * Switcher between **Checklist Subtasks** and **Markdown Description Text**.
  * **Checklist View**: Reorderable list of subtasks with individual checkboxes, add-subtask input field, and progress counter ("2/5").
  * **Markdown View**: Rich text editor with formatting toolbar (Bold, Italic, Strikethrough, Heading, Bullet List, Code Block, Link).
* **Attachments Section**:
  * Grid of attached photos, voice audio clips, and documents with file size and thumbnail.
* **Activity & Comment Stream**:
  * Chronological feed of collaborator comments with avatars and system edit audit records (e.g. "Due date changed to Tomorrow by Mahim").
  * Comment input box with @mention button and attachment paperclip.

### Available Actions
1. Edit task title and description.
2. Add, reorder, check off, or delete subtasks.
3. Open date picker to modify due date and recurrence rules.
4. Add reminders (up to 5 for Pro).
5. Attach photos, record audio clips, or upload documents.
6. Post comments and mention list members.
7. Tap "Start Focus" to launch `PomodoroActivity` bound to this task.

### Interaction Behavior
* Edits auto-save immediately to SQLite `Tasks2` without requiring an explicit "Save" button tap.
* Navigating back commits pending changes and writes a dirty record to `Tasks2_SYNCED_JSON`.

### Input Fields
* Title: String, max 1024 chars.
* Description: Markdown text, max 32KB.
* Subtask title: String, max 256 chars.
* Comment text: String, max 2048 chars.

### Navigation
* Back arrow returns to referring screen (`SCR-TASK-001`, `SCR-CAL-001`, etc.).
* Tapping Date chip summons `DatePickerDialog`.
* Tapping "Task Activities" in overflow menu launches `TaskActivitiesWebViewActivity`.

### Different States
* **Active Task State**: Normal editable controls.
* **Completed Task State**: Title struck through; completion timestamp displayed; option to "Uncomplete".
* **Won't Do State**: Title styled in dimmed italics with circle-slash badge.

### Data Requirements
* Full `Tasks2` row joined with `PROJECT`, `CHECKLIST_ITEM`, `ATTACHMENT`, and `COMMENT` rows.

### Related Features
* Subtasks (`F004`), Attachments (`F020`), Comments (`F021`), Priority (`F005`), Reminders (`F036`).

### Subscription Restrictions
* Free tier limits attachments to 1 per task (max 10MB/day).
* Free tier limits reminders to 1.
* Free tier caps checklist items at 19 items.

### Evidence
* `com.ticktick.task.activity.TaskDetailActivity`
* `res/layout/activity_task_detail.xml`
* `res/layout/item_checklist_row.xml`

### Confidence
Confirmed `[CODE-CONFIRMED]`.

### Unknowns
* None; decompiled detail layout and GreenDAO entity mappings verified.

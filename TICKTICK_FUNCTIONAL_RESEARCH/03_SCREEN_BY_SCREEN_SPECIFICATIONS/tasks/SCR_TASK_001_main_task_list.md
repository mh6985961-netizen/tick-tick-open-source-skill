# Screen Specification: SCR-TASK-001 - Main Task List

### Screen ID
`SCR-TASK-001`

### Screen Name
Main Task List Screen (`TaskListFragment`)

### Purpose
Serves as the primary operational hub where users review, organize, schedule, and complete their actionable tasks within the currently selected List, Smart List, or Filter view.

### Entry Points
1. Default landing view upon application startup via `TaskActivity`.
2. Selecting any List, Folder, Tag, or Smart List (Today, Next 7 Days, Inbox) from `NavDrawerFragment`.
3. Tapping the "Tasks" icon on the bottom navigation `TabBar`.

### Screen Contents
* **Top Toolbar**:
  * Left Navigation Hamburger icon (toggles `DrawerLayout`).
  * Center List Title with optional Project Color indicator dot.
  * Right Action Icons: Search magnifying glass, Sort & Grouping button, Context Menu overflow (3 dots).
* **Sectioned RecyclerView (`task_list_view`)**:
  * Group / Section Dividers (e.g. "Overdue", "Today", "Tomorrow", "Completed (X)").
  * Task Item Cards displaying:
    * Left Checkbox (circular hit target).
    * Task Title text with strike-through when completed.
    * Priority Flag (Red/Orange/Blue for High/Medium/Low).
    * Due Date / Time badge with clock icon (highlighted red if overdue).
    * Recurrence icon (looping arrows) if recurring.
    * Checklist progress pill (e.g., "2/5") if subtasks exist.
    * Tag pills (`#tag`).
    * Reorder grip handle (visible in custom sort mode).
* **Floating Action Button (+)**: Primary accent circular button positioned at bottom-right corner.

### Available Actions
1. **Single Tap on Task Card**: Opens `SCR-TASK-002` (Task Detail View).
2. **Tap Checkbox**: Immediately marks task completed (`Tasks2.STATUS = 2`).
3. **Short / Long Swipes**: Left/Right gestures trigger configured actions (Complete, Due Date, Priority, Delete).
4. **Long Press on Task**: Activates `SCR-TASK-004` (Batch Multi-Select Mode).
5. **Tap FAB (+)**: Summons `SCR-TASK-003` (Quick Add Bottom Sheet).
6. **Pull-to-Refresh**: Initiates delta synchronization with cloud servers.

### Interaction Behavior
* Checking off an item draws a smooth vector checkmark, applies strike-through to the title text, waits 400ms, and animates the row collapsing and moving into the "Completed" section.
* Reversible via an undo `Snackbar` that persists for 3.5 seconds.

### Input Fields
* No direct text inputs on the main list surface; input is delegated to Quick Add or Detail modals.

### Navigation
* Tapping a task navigates to `SCR-TASK-002` (`TaskDetailActivity`).
* Tapping FAB navigates to `SCR-TASK-003` (`QuickAddBottomSheet`).
* Tapping Sort button opens `SortOptionBottomFragment`.

### Different States
* **Default State**: Lists active tasks categorized into collapsible sections.
* **Empty State**: Renders empty-state graphic (`img_empty_task.png`) with contextual encouragement (e.g., "All done for today! Take a break.") and an "Add a Task" prompt.
* **Loading State**: Shimmer skeleton layout while loading from SQLite.
* **Search / Filter Active**: Displays filter dismiss chip at top of list.

### Data Requirements
* Active `PROJECT` SID.
* List of `Tasks2` rows where `DELETED = 0` and `PROJECT_ID = currentProject.SID` (or Smart List filter criteria).

### Related Features
* Task Creation (`F001`), Quick Add (`F002`), Custom Sorting (`F014`), Smart Lists (`F110`).

### Subscription Restrictions
* None on basic list rendering. Free tier enforces a cap of 99 active tasks per list.

### Evidence
* `com.ticktick.task.fragment.TaskListFragment`
* `res/layout/fragment_task_list.xml`
* `res/layout/item_task_row.xml`

### Confidence
Confirmed `[CODE-CONFIRMED]` via REA JADX inspection and APK layout parsing.

### Unknowns
* None; primary list architecture fully verified.

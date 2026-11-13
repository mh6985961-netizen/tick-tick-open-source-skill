# Screen Specification: SCR-MAT-001 - Eisenhower Matrix 2x2 Grid

### Screen ID
`SCR-MAT-001`

### Screen Name
Eisenhower Matrix 2x2 Grid (`MatrixManageActivity`)

### Purpose
Visualizes and prioritizes tasks across a 4-quadrant decision matrix based on urgency and importance, allowing direct drag-and-drop re-prioritization and quadrant filtering.

### Entry Points
1. Left Navigation Drawer item: "Eisenhower Matrix".
2. Optional bottom `TabBar` slot if added by user.
3. Home screen Matrix widget (`AppWidgetMatrixConfigActivity`).

### Screen Contents
* **Top Header Bar**:
  * Navigation Hamburger icon.
  * Matrix Profile selector dropdown (e.g. "Default Matrix", "Work Matrix").
  * Right Action Buttons: Profile Switcher icon, Quadrant Rule Settings (Pro gear icon).
* **2x2 Quadrant Grid Layout (`matrix_grid_view`)**:
  * **Quadrant 1 (Top-Left, Red Accent)**:
    * Title: "Urgent & Important" ("Do It Now").
    * Task list preview with priority flags and checkboxes.
    * "+" Quick Add button anchored inside quadrant.
  * **Quadrant 2 (Top-Right, Yellow/Orange Accent)**:
    * Title: "Not Urgent & Important" ("Plan to Do").
    * Task list preview.
    * "+" Quick Add button.
  * **Quadrant 3 (Bottom-Left, Blue Accent)**:
    * Title: "Urgent & Not Important" ("Delegate / Assign").
    * Task list preview.
    * "+" Quick Add button.
  * **Quadrant 4 (Bottom-Right, Green/Grey Accent)**:
    * Title: "Not Urgent & Not Important" ("Eliminate / Won't Do").
    * Task list preview.
    * "+" Quick Add button.

### Available Actions
1. **Drag Task Between Quadrants**: Dragging across quadrant boundaries automatically mutates task priority and due date.
2. **Tap Checkbox**: Completes task within quadrant.
3. **Tap "+" Inside Quadrant**: Opens quick add pre-filled with that quadrant’s priority and date rules.
4. **Tap Quadrant Title / Header**: Opens `SCR-MAT-002` (Expanded Single Quadrant Detail List).
5. **Tap Rule Settings**: Opens `SCR-MAT-003` (`MatrixConditionEditActivity`) to customize auto-sorting conditions.

### Interaction Behavior
* Dragging an item lifts it with elevation 6dp. Dropping into Q1 sets `Tasks2.PRIORITY = 5` (High) and `DUE_DATE = Today`. Dropping into Q4 clears priority to `0` (None).

### Input Fields
* No text input on grid surface; delegated to quick add sheet.

### Navigation
* Tapping a task navigates to `SCR-TASK-002` (`TaskDetailActivity`).
* Tapping Quadrant Title navigates to `MatrixQuadrantDetailActivity`.
* Tapping Rule Settings navigates to `SCR-MAT-003` (`MatrixConditionEditActivity`).

### Different States
* **Default State**: Populates all 4 quadrants based on current active tasks.
* **Empty Quadrant State**: Displays subtle icon with prompt: *"No tasks in this quadrant"*.

### Data Requirements
* Active `MATRIX_PROFILE` and 4 `MATRIX_QUADRANT` definitions.
* Filtered `Tasks2` rows evaluated against each quadrant's rule set.

### Related Features
* Eisenhower Matrix (`F138`), Priority (`F005`), Task Scheduling (`F006`).

### Subscription Restrictions
* Free tier supports 1 default matrix profile with fixed, un-editable quadrant rules.
* Pro tier unlocks **custom matrix profiles** and **custom quadrant rule builders**.

### Evidence
* `com.ticktick.task.activity.matrix.MatrixManageActivity`
* `res/layout/activity_matrix_manage.xml`
* `res/layout/item_matrix_quadrant.xml`

### Confidence
Confirmed `[CODE-CONFIRMED]`.

### Unknowns
* None; verified in decompiled matrix package.

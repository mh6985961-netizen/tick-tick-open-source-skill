# Feature-to-Screen Mapping

## 1. Overview
This document provides a complete cross-reference mapping every discovered feature (`F001` to `F206`) to its primary screen, modal, preference, or service component.

---

## 2. Master Mapping Table

| Feature Domain | Feature Range | Primary Screen ID | Primary Android Component Class |
| :--- | :--- | :--- | :--- |
| **Task Creation & Editing** | `F001` – `F005` | `SCR-TASK-001`, `SCR-TASK-002`, `SCR-TASK-003` | `TaskListFragment`, `TaskDetailActivity`, `QuickAddBottomSheet` |
| **Subtasks & Checklists** | `F004`, `F007` | `SCR-TASK-002` | `TaskDetailActivity` |
| **Task Reordering & Drag** | `F013`, `F014` | `SCR-TASK-001` | `TaskListFragment` (ItemTouchHelper) |
| **Batch Multi-Select** | `F017` | `SCR-TASK-004` | `BatchEditTaskActivity` |
| **Task Activity History** | `F019` | `SCR-TASK-007` | `TaskActivitiesWebViewActivity` |
| **Task Comments & Attachments**| `F020`, `F021` | `SCR-TASK-002`, `SCR-TASK-005` | `TaskCommentActivity` |
| **Exact Reminders & Alarms** | `F036` – `F040` | `SCR-REM-001`, `SCR-REM-002` | `ReminderPopupActivity`, `SnoozePopupActivity` |
| **Geofenced Reminders** | `F042` | `SCR-REM-004` | `LocationPickerActivity`, `GeofenceBroadcastReceiver` |
| **Calendar Multi-Views** | `F056` – `F060` | `SCR-CAL-001`, `SCR-CAL-002` | `CalendarViewActivity`, `CalendarViewOptionsActivity` |
| **Calendar Subscriptions** | `F063` | `SCR-CAL-003` | `CalendarManagerActivity` |
| **Course Timetable** | `F067` – `F071` | `SCR-CAL-005`, `SCR-CAL-006` | `CourseDetailActivity`, `CourseImportActivity` |
| **Habit Tracking & Streaks** | `F076` – `F081` | `SCR-HAB-001`, `SCR-HAB-004` | `AllHabitListActivity`, `HabitDetailActivity` |
| **Habit Creation & Presets** | `F083`, `F084` | `SCR-HAB-002`, `SCR-HAB-003` | `HabitAddActivity`, `HabitEditActivity` |
| **Habit Section Organizer** | `F086` | `SCR-HAB-006` | `HabitSectionManageActivity` |
| **Pomodoro & Stopwatch** | `F091`, `F092` | `SCR-FOC-001` | `PomodoroActivity` |
| **Ambient Sounds** | `F093` | `SCR-FOC-002` | `ChoosePomoSoundActivity` |
| **Strict Mode App Lock** | `F094` | `SCR-FOC-001` | `PomodoroActivity` |
| **Focus Analytics** | `F096` | `SCR-FOC-004`, `SCR-FOC-005` | `FocusTimelineActivity`, `FocusTimelineEditActivity` |
| **Lists, Folders & Kanban** | `F104` – `F109` | `SCR-ORG-001`, `SCR-ORG-002`, `SCR-ORG-003`| `ProjectDetailActivity`, `ProjectEditActivity`, `ProjectGroupManageActivity` |
| **Tag Hierarchy** | `F107` | `SCR-ORG-004` | `TagManageActivity` |
| **Custom Smart Lists** | `F110` | `SCR-ORG-005` | `SmartListRuleEditActivity` |
| **Natural Language Parsing** | `F118`, `F119` | `SCR-TASK-003` | `QuickAddBottomSheet`, `QuickAddEditText` |
| **Global Search** | `F120`, `F121` | `SCR-SEARCH-001` | `SearchActivity` |
| **Shared Lists & Collaboration**| `F128` – `F132` | `SCR-COLLAB-001` | `ShareActivity`, `InviteTeamMemberActivity` |
| **Eisenhower Matrix Grid** | `F138` – `F140` | `SCR-MAT-001`, `SCR-MAT-002` | `MatrixManageActivity`, `MatrixQuadrantDetailActivity` |
| **Matrix Custom Rules (Pro)** | `F141` | `SCR-MAT-003` | `MatrixConditionEditActivity` |
| **Theme Store & Custom Colors**| `F151`, `F152` | `SCR-SET-002` | `CustomThemeActivity` |
| **Swipe Gesture Customizer** | `F155` | `SCR-SET-003` | `CustomSwipePreference` |
| **App Lock & Biometrics** | `F158` | `SCR-SET-004` | `ChooseLockPattern`, `ConfirmLockPattern` |
| **Offline Backup & CSV Export**| `F165`, `F167` | `SCR-SET-001` | `data_import_preferences.xml` |
| **Pro Upgrade Paywalls** | `F200` – `F203` | `SCR-PRO-001`, `SCR-PRO-002`, `SCR-PRO-003`| `GetProActivity`, `ProFeaturesActivity`, `ProExpiredActivity6130` |

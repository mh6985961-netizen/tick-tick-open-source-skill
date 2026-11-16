# MASTER AI BUILDER PROMPT: COMPLETE PRODUCTION-GRADE PRODUCTIVITY APPLICATION

```markdown
# MISSION BRIEF: AUTONOMOUS PRODUCTION-GRADE PRODUCTIVITY APP IMPLEMENTATION

You are a Principal Mobile Architect, Lead Full-Stack Engineer, and Senior UX Systems Developer.
Your objective is to independently build, wire, test, and deliver a 100% complete, polished, production-ready, open-source productivity application inspired by TickTick, utilizing all pre-researched blueprints, specifications, database schemas, and Material 3 design assets available in this workspace.

Every single feature, interaction, animation, edge case, and data model must be fully operational. There are ZERO mockups, ZERO placeholders, ZERO stubbed "TODO" functions, and ZERO paid/subscription restrictions. Everything is 100% unlocked, local-first, robust, and functional.

---

## 1. REPOSITORY ASSETS & KNOWLEDGE INGESTION

Before writing application code, you must thoroughly ingest and cross-reference the research and design files present in this workspace:

1. **Material 3 Design Prototypes & Assets (`stitch_stitch_material_3_productivity/`)**:
   - Contains 49 complete screen designs across 12 modules.
   - Each screen subfolder contains:
     - `code.html`: Exact HTML5/Tailwind/Material 3 structure, semantic layouts, button actions, form inputs, and hierarchy.
     - `DESIGN.md`: Layout anatomy, component specifications, token usage, and behavior.
     - `screen.png`: Visual design reference demonstrating exact proportions, layout, and visual fidelity.
2. **Screen-by-Screen Functional Content Specification (`TickTick_Research/10_FINAL_HANDOFF/GOOGLE_STITCH_COMPLETE_SCREEN_SPECIFICATION.md` or `TICKTICK_FUNCTIONAL_RESEARCH/10_FINAL_HANDOFF/GOOGLE_STITCH_COMPLETE_SCREEN_SPECIFICATION.md`)**:
   - Exhaustive 11-part functional specification for all 49 screens: Screen ID, Purpose, Navigation Source/Destinations, Layout Sections, Input Fields & Validation, Interactive Elements, Dynamic States (Default, Empty, Loading, Error), Business Logic & Computation, Data Fields & Schema Mapping, Zero-Paywall Behavior, and Edge Cases.
3. **Core Engineering Research Blueprints (`TICKTICK_FUNCTIONAL_RESEARCH/research/`)**:
   - `03_MASTER_FEATURE_INVENTORY.md`: All 206 features (F001–F206) across 12 domains.
   - `05_INTERACTION_AND_MICRO_BEHAVIOR.md`: Gesture physics (15% trigger / 45% execute swipe thresholds, drag-and-drop mechanics, flip-to-focus sensor rules, NLP inline chip tokens).
   - `06_COMPLETE_USER_WORKFLOWS.md`: End-to-end task, habit, calendar, focus, and matrix flows.
   - `07_SETTINGS_AND_CONFIGURATION.md`: Complete preference key schema and defaults.
   - `08_DATA_ARCHITECTURE.md` & `evidence/code_references/schema.sql`: 98 SQLite tables (Tasks, Checklist Items, Projects/Lists, Habits, Habit Records, Matrix Profiles/Quadrants, Focus Summaries, Tags, Filters, Reminders, and Sync Queues).
   - `11_NOTIFICATIONS_AND_BACKGROUND_SYSTEMS.md`: Exact alarm scheduling, snooze behavior, persistent notification channels, and reboot recovery.
   - `14_EDGE_CASES_AND_ERROR_HANDLING.md`: RFC-5545 recurrence leap-year rules, month-end date clamping, timezone transitions, and hardware event handling.
   - `16_IMPLEMENTATION_SPECIFICATIONS.md`: Clean-room algorithms for recurrence calculation, NLP smart parsing, and search indexing.

---

## 2. THE BIDIRECTIONAL RECONCILIATION RULE (MANDATORY)

You must adhere strictly to these two invariant reconciliation principles:

### RULE A: FUNCTIONAL SPEC SUPREMACY
If a functionality, setting, modal, filter, or data field is specified in the Functional Blueprint (`GOOGLE_STITCH_COMPLETE_SCREEN_SPECIFICATION.md` or `TICKTICK_FUNCTIONAL_RESEARCH/`) but is not explicitly visible in that screen's `code.html` or `screen.png`:
- **You MUST implement it.**
- Derive its visual presentation, controls, and dialogs directly from the established Material 3 design language used across the rest of the application.
- Never omit or compromise any functional requirement because it was missing from a static prototype.

### RULE B: VISUAL DESIGN INTEGRITY
If a UI element, button, toggle, menu item, card, chip, or visual affordance is depicted in `code.html` or `screen.png` but is omitted from the functional text specification:
- **You MUST build complete functional business logic for it.**
- **DO NOT alter, simplify, or remove the visual design.**
- Wire the control to corresponding database state, action handlers, and transitions so that every clickable element performs a meaningful, bug-free operation.

---

## 3. CORE ARCHITECTURE & SYSTEM DESIGN

### A. Architectural Pattern
- Employ **Clean Architecture** with strict layer separation:
  1. **Domain Layer**: Pure business entities, use cases, recurrence engines, NLP tokenizers, and repository interfaces.
  2. **Data Layer**: Local SQLite database, GreenDAO-equivalent schema migrations, Data Access Objects (DAOs), key-value settings storage, and repository implementations.
  3. **Presentation Layer**: Reactive state management (BLoC / Riverpod / Redux / Zustand depending on platform), declarative UI components matching the 49 screen specs, view models, and navigation routers.

### B. Offline-First Database Engine
- Implement the local SQLite database according to `evidence/code_references/schema.sql` and `08_DATA_ARCHITECTURE.md`:
  - `TASKS2`: 53 fields including `ID`, `TITLE`, `CONTENT`, `DUE_DATE`, `START_DATE`, `ALL_DAY`, `TIME_ZONE`, `REMINDER`, `REPEAT_FLAG`, `STATUS`, `PRIORITY`, `PROJECT_ID`, `PARENT_SID`, `CHILD_IDS`, `SORT_ORDER`, `PIN`, `PROGRESS`, and shadow sync timestamps.
  - `CHECKLIST_ITEM`: Subtasks with parent bindings and completion timestamps.
  - `PROJECT`: Lists, Folders, Colors, View Modes (List, Kanban, Timeline), and Kind.
  - `HABIT` & `HABIT_RECORD`: Daily/weekly frequency targets, streak counters, check-in logs, and time-of-day sections.
  - `MATRIX_PROFILE` & `MATRIX_QUADRANT`: Eisenhower 4-quadrant custom coordinate mappings and filters.
  - `FOCUS_SUMMARY`: Pomodoro sessions, stopwatch durations, estimated vs. actual pomodoros, and tags.
  - `TAG`, `FILTER`, `ATTACHMENT`, and `REMINDER` relational tables.
- All mutations must be transactional (`ACID`) and write through local persistence immediately.

### C. Core Functional Engines
1. **Recurrence Engine (RFC-5545 Compliant)**:
   - Evaluates `RRULE` strings (Daily, Weekly on specific days, Monthly on nth day/weekday, Yearly).
   - Handles `repeatFrom` flag: Recurrence from Scheduled Due Date (`repeatFrom=0`) vs. Completion Date (`repeatFrom=1`).
   - Handles month-end date clamping (Jan 31 -> Feb 28/29 -> Mar 31) and leap year safety.
2. **Natural Language Processing (NLP) Parser**:
   - Parses inline titles for dates, times, recurrence, lists, and tags (e.g., "Submit report every Friday at 5pm #Work !high").
   - Converts parsed entities into interactive chips in the quick-add bar with one-tap dismissal/reversion.
3. **Eisenhower Matrix Engine**:
   - Dynamic classification of tasks into 4 quadrants (Urgent & Important, Important not Urgent, Urgent not Important, Neither).
   - Drag-and-drop between quadrants updates the task's priority and due date automatically.
4. **Focus & Pomodoro Engine**:
   - Configurable work duration (default 25m), short break (5m), long break (15m), and long break interval (4 cycles).
   - Background timer execution using local system notifications and wake-lock / background service.
   - White noise / ambient sound player state engine.
   - Flip-to-Focus accelerometer sensor trigger (if device supports sensor, otherwise graceful fallback).
5. **Habit Tracking Engine**:
   - Daily/weekly goal evaluation, current streak and best streak calculations, completion rate percentages, and calendar heatmaps.
6. **Smart Notification & Alarm Scheduler**:
   - Exact alarm scheduling for task reminders, advance reminders (5m, 30m, 1d before), location reminders (geofence mockable/ready), and habit check-in prompts.
   - Snooze options: 5 min, 10 min, 1 hour, tomorrow morning, or custom time.

### D. Zero-Paywall / 100% Open-Source Guarantee
- Absolutely NO features may be locked, disabled, or hidden behind paywalls:
  - Unlimited habits, unlimited custom lists, unlimited checklists, unlimited attachments, full multi-view calendar (Day, 3-Day, Week, Month, Multi-Month), custom matrix profiles, full white-noise library, and complete historical statistics are **100% active and unlocked**.

---

## 4. SCREEN IMPLEMENTATION BLUEPRINT (ALL 49 SCREENS)

Implement all 49 screens categorized across the 12 core functional modules, strictly matching the HTML structure in `stitch_stitch_material_3_productivity/` and the behavior in `GOOGLE_STITCH_COMPLETE_SCREEN_SPECIFICATION.md`:

- **Module 01: Core Task Management**
  - `SCR-001`: Tasks / Main List View
  - `SCR-002`: Task Detail View
  - `SCR-003`: Quick Add Bar & Full Task Creator Modal
  - `SCR-004`: Task Search & Global Filter
  - `SCR-005`: Multi-Select & Batch Actions Bar
- **Module 02: List & Folder Organization**
  - `SCR-006`: Navigation Drawer / Sidebar
  - `SCR-007`: List / Folder Creator & Editor
  - `SCR-008`: Kanban Board View
  - `SCR-009`: Smart List Configuration (Today, Tomorrow, Next 7 Days, Assigned to Me)
- **Module 03: Calendar & Scheduling**
  - `SCR-010`: Calendar Month View
  - `SCR-011`: Calendar Day & Timeline View
  - `SCR-012`: Calendar 3-Day & Week View
  - `SCR-013`: Arrange Tasks / Unscheduled Drawer
  - `SCR-014`: External Calendar Integration & Subscription Manager
- **Module 04: Habit Tracking**
  - `SCR-015`: Habit Tracker Main Dashboard
  - `SCR-016`: Habit Creation & Edit Screen
  - `SCR-017`: Habit Statistics & Heatmap View
  - `SCR-018`: Habit Check-In Log & Archive
- **Module 05: Focus & Time Tracking**
  - `SCR-019`: Focus / Pomodoro Timer Screen
  - `SCR-020`: Stopwatch Screen
  - `SCR-021`: Focus Ambient Sound Selector
  - `SCR-022`: Focus Records & Historical Analytics
- **Module 06: Eisenhower Matrix**
  - `SCR-023`: Eisenhower Matrix 4-Quadrant Dashboard
  - `SCR-024`: Matrix Settings & Quadrant Mapping Customizer
- **Module 07: Note-Taking & Rich Text**
  - `SCR-025`: Note Mode Editor (Markdown & WYSIWYG)
  - `SCR-026`: Note List & Archive View
- **Module 08: Productivity Analytics & Gamification**
  - `SCR-027`: Achievement & Gamification Level Dashboard
  - `SCR-028`: Productivity Statistics & Summary Charts
- **Module 09: Collaboration & Sharing**
  - `SCR-029`: Shared List Management & Member Permission Panel
  - `SCR-030`: Task Activity & Comment Thread View
- **Module 10: Import, Export & Data Backup**
  - `SCR-031`: Data Backup & Restore Center
  - `SCR-032`: Third-Party Importer (Todoist, Wunderlist, CSV, JSON)
- **Module 11: Settings & Customization**
  - `SCR-033`: Global Settings Menu
  - `SCR-034`: Theme & Visual Appearance Customizer (Full Palette, Fonts, Compactness)
  - `SCR-035`: Sound & Vibration Notification Settings
  - `SCR-036`: Date, Time & Recurrence Preferences
  - `SCR-037`: App Lock & Biometric Security Setup
  - `SCR-038`: Quick Add & Smart Recognition Preferences
  - `SCR-039`: Navigation & Tab Bar Customizer
- **Module 12: Dialogs, Sheets & Micro-Surfaces**
  - `SCR-040`: Date & Time Picker Modal (with Recurrence Picker)
  - `SCR-041`: Priority Selector Dialog
  - `SCR-042`: Tag Selector & Manager Sheet
  - `SCR-043`: Move Task to List/Section Sheet
  - `SCR-044`: Reminder Configuration Dialog (Custom Alarms & Snooze)
  - `SCR-045`: Attachment Preview & Upload Dialog
  - `SCR-046`: Filter Builder Dialog
  - `SCR-047`: Custom Soundscape Mixer Sheet
  - `SCR-048`: Trash / Recycle Bin Screen
  - `SCR-049`: Context Action Bottom Sheet

---

## 5. INTERACTION & MICRO-BEHAVIOR SPECIFICATIONS

Implement exact gesture physics and interactions according to `05_INTERACTION_AND_MICRO_BEHAVIOR.md`:
1. **Swipe Actions on Task Items**:
   - `0% to 15%` drag: Elastic resistance pull.
   - `15% to 45%` drag: Icon reveal and color threshold.
   - `>45%` drag: Threshold crossed; on release, trigger action (Swipe Right = Complete / Date Picker; Swipe Left = Delete / Move). Configurable in Settings.
2. **Drag-and-Drop Reordering**:
   - Long-press (300ms) with haptic feedback elevates card with z-index shadow.
   - Smooth reordering with auto-scroll when dragged near top/bottom edges.
3. **Checklist & Nested Subtasks**:
   - Checking a subtask strikes through text and increments parent task progress bar.
   - Checking parent task prompts to complete all subtasks.

---

## 6. PHASE-BY-PHASE EXECUTION PROTOCOL

Follow this sequential execution plan without skipping steps:

- **STEP 1: REPOSITORY DISCOVERY & AUDIT**
  - Read all 49 screen folders in `stitch_stitch_material_3_productivity/`.
  - Read `GOOGLE_STITCH_COMPLETE_SCREEN_SPECIFICATION.md` and `evidence/code_references/schema.sql`.
  - Validate your environment, package dependencies, and development tools.

- **STEP 2: DATABASE & DATA ARCHITECTURE SETUP**
  - Create the SQLite database schema matching the 98 tables and entities.
  - Implement full CRUD operations, transaction wrappers, and initial seed data (default lists: "Inbox", "Personal", "Work"; default matrix profiles).

- **STEP 3: BUSINESS LOGIC ENGINES & SERVICES**
  - Implement the RFC-5545 Recurrence calculation engine.
  - Implement the Smart NLP text parser for quick-add.
  - Implement the Pomodoro & Stopwatch timer background services.
  - Implement the Habit streak and history computation engine.
  - Implement the local Notification & Alarm scheduling manager.

- **STEP 4: SCREEN IMPLEMENTATION (MODULES 01 THROUGH 12)**
  - Implement each of the 49 screens following the visual anatomy of `code.html`/`screen.png` and the functional logic of `GOOGLE_STITCH_COMPLETE_SCREEN_SPECIFICATION.md`.
  - Apply the Bidirectional Reconciliation Rule on every single screen.

- **STEP 5: COMPREHENSIVE INTEGRATION & TESTING**
  - Wire all navigation routes, deep links, dialogs, bottom sheets, and global search.
  - Verify edge cases: leap year recurrences, month-end dates, offline data survival, timezone shifts, and empty states.
  - Execute end-to-end user workflows: task creation -> NLP parsing -> recurrence triggering -> habit check-in -> focus session -> statistics update.

---

## 7. FINAL ACCEPTANCE CRITERIA

The app is complete and accepted ONLY when:
1. All 49 screens exist, render cleanly, match the visual design reference, and are reachable via proper navigation.
2. Every button, menu, input, chip, and toggle is wired to working logic—no dead ends or non-functional controls.
3. Database mutations persist across app reboots with full data integrity.
4. Recurrence, notifications, habit tracking, focus timer, and Eisenhower matrix are completely operational.
5. Zero paywalls or artificial limitations exist.
```

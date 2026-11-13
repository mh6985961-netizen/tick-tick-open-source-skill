# Development Agent Handoff & Build Protocol

## 1. Directive for the Autonomous Development Agent

You are tasked with building an independent, open-source productivity application inspired by TickTick.

This workspace contains the complete reverse engineering and architectural blueprint extracted from the original Android application.

**You must strictly follow this build protocol:**

---

## 2. Step-by-Step Build Sequence

```
+-------------------------------------------------------------------------------+
|  PHASE 1: PERSISTENCE LAYER INITIALIZATION                                    |
|  - Ingest SQLite schema from evidence/code_references/schema.sql               |
|  - Implement DAOs and local repositories for TASKS2, PROJECT, HABIT, POMODORO |
|  - Setup shadow change queue (TASKS2_SYNCED_JSON) for offline mutations       |
+-------------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------------+
|  PHASE 2: CORE DOMAIN & BUSINESS ENGINES                                      |
|  - Implement RFC-5545 iCalendar Recurrence Engine (see research/06 & 16)      |
|  - Implement Real-Time NLP Tokenizer (see feature_specs/smart_features/F118)  |
|  - Implement Habit Streak Calculator (see feature_specs/habits/F076)          |
|  - Implement Eisenhower Matrix Rule Evaluator (see productivity/F138)         |
+-------------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------------+
|  PHASE 3: PLATFORM SERVICES & HARDWARE INTEGRATION                            |
|  - Register exact alarms with AlarmManager and boot re-registration           |
|  - Implement Ambient Audio Player for white noise playback                    |
|  - Setup Accelerometer SensorEventListener for Flip-to-Focus                  |
+-------------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------------+
|  PHASE 4: UI PRESENTATION & MICRO-INTERACTIONS                                |
|  - Build Navigation Shell (Drawer + Bottom TabBar)                            |
|  - Implement TaskListFragment with 15%/45% swipe threshold gestures          |
|  - Implement QuickAddBottomSheet with live NLP chip span rendering            |
|  - Implement Calendar Multi-Views with drag-to-schedule                       |
|  - Implement Pomodoro Dial with rotary touch physics                          |
+-------------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------------+
|  PHASE 5: VERIFICATION AGAINST TEST MATRICES                                  |
|  - Run Unit Test Suites from research/17_TESTING_AND_VERIFICATION.md          |
|  - Verify Doze mode alarm precision and habit streak boundary edge cases      |
+-------------------------------------------------------------------------------+
```

---

## 3. Key Reference Documents for Code Generation

| Development Task | Ground-Truth Research Document to Consult |
| :--- | :--- |
| **Database Tables & Fields** | [`evidence/code_references/schema.sql`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/evidence/code_references/schema.sql) |
| **Entity Relationships** | [`research/08_DATA_ARCHITECTURE.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/08_DATA_ARCHITECTURE.md) |
| **Screen Layouts & Views** | [`03_SCREEN_BY_SCREEN_SPECIFICATIONS/screen_inventory.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/03_SCREEN_BY_SCREEN_SPECIFICATIONS/screen_inventory.md) |
| **Swipe & Gestures** | [`research/05_INTERACTION_AND_MICRO_BEHAVIOR.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/05_INTERACTION_AND_MICRO_BEHAVIOR.md) |
| **End-to-End Lifecycles**| [`research/06_COMPLETE_USER_WORKFLOWS.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/06_COMPLETE_USER_WORKFLOWS.md) |
| **Settings & Keys** | [`research/07_SETTINGS_AND_CONFIGURATION.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/07_SETTINGS_AND_CONFIGURATION.md) |
| **REST APIs & WebSockets**| [`research/09_NETWORK_AND_BACKEND.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/09_NETWORK_AND_BACKEND.md) |
| **Offline Synchronization**| [`research/10_OFFLINE_ONLINE_BEHAVIOR.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/10_OFFLINE_ONLINE_BEHAVIOR.md) |
| **Alarms & Background** | [`research/11_NOTIFICATIONS_AND_BACKGROUND_SYSTEMS.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/11_NOTIFICATIONS_AND_BACKGROUND_SYSTEMS.md) |
| **Free vs Pro Boundaries**| [`research/13_PREMIUM_FEATURES_AND_RESTRICTIONS.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/13_PREMIUM_FEATURES_AND_RESTRICTIONS.md) |
| **Edge Cases & Resilience**| [`research/14_EDGE_CASES_AND_ERROR_HANDLING.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/14_EDGE_CASES_AND_ERROR_HANDLING.md) |
| **QA Verification Tests**| [`research/17_TESTING_AND_VERIFICATION.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/17_TESTING_AND_VERIFICATION.md) |

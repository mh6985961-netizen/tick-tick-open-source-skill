# TickTick APK Reverse Engineering & Functional Research

> **Complete, platform-independent, evidence-based technical and functional blueprint for building an open-source productivity platform.**

---

## 1. Project Overview

This workspace contains the exhaustive reverse engineering and architectural analysis of the **TickTick Android Application** (`com.ticktick.task`, version `8.3.0.1`, version code `8301`).

The goal of this research project is **strictly investigative and functional**: to discover, trace, extract, and document every feature, screen, interaction, workflow, database schema, background mechanism, network endpoint, and business rule to empower an independent development agent to build an open-source alternative.

**Ground-Truth Subject**: `TickTick_To+Do+List+&+Calendar_8.3.0.1_APKPure.xapk`  
**Standard of Evidence**: Every finding is backed by `[CODE-CONFIRMED]` bytecode analysis (via JADX and REA) or `[RESOURCE-CONFIRMED]` decoded XML resources.

---

## 2. Master Documentation Directory

All research documentation is organized under [`TICKTICK_FUNCTIONAL_RESEARCH/`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH):

| Document | Description | Key Contents |
| :--- | :--- | :--- |
| [`01_APK_OVERVIEW.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/01_APK_OVERVIEW.md) | Technical APK Profile | Package metadata, 61 permissions, 3 DEX files, 227 manifest activities, SDK dependencies. |
| [`02_ANALYSIS_TOOLS.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/02_ANALYSIS_TOOLS.md) | Reverse-Engineering Stack | REA v6.7.0, JADX Headless MCP v0.7.1, Zulu JDK 17, Apktool v3.0.3, Androguard. |
| [`03_MASTER_FEATURE_INVENTORY.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/03_MASTER_FEATURE_INVENTORY.md) | Master Feature Catalog | **206 features** (`F001`–`F206`) cataloged across 12 functional domains with evidence tags. |
| [`04_SCREEN_AND_NAVIGATION_INVENTORY.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/04_SCREEN_AND_NAVIGATION_INVENTORY.md) | Complete Screen Inventory | 332 Activities, 343 Fragments, 137 Dialogs, XML layouts, controls, and deep links. |
| [`05_INTERACTION_AND_MICRO_BEHAVIOR.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/05_INTERACTION_AND_MICRO_BEHAVIOR.md) | Micro-Interactions & UX | Swipe gesture thresholds (15%/45%), drag-and-drop physics, flip-to-focus, NLP chips. |
| [`06_COMPLETE_USER_WORKFLOWS.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/06_COMPLETE_USER_WORKFLOWS.md) | End-to-End User Workflows | 7 lifecycle workflows with Mermaid sequence diagrams (Tasks, Habits, Pomo, Calendar, Sync). |
| [`07_SETTINGS_AND_CONFIGURATION.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/07_SETTINGS_AND_CONFIGURATION.md) | Settings & Preferences Audit | All 46 preference XML files, keys, defaults, titles, and functional behaviors. |
| [`08_DATA_ARCHITECTURE.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/08_DATA_ARCHITECTURE.md) | Database & Entity Model | Complete ER diagrams, GreenDAO ORM structures, and primary entity definitions. |
| [`09_NETWORK_AND_BACKEND.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/09_NETWORK_AND_BACKEND.md) | REST APIs & WebSockets | 105 API endpoints, regional routing (Global vs China), headers, and push frames. |
| [`10_OFFLINE_ONLINE_BEHAVIOR.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/10_OFFLINE_ONLINE_BEHAVIOR.md) | Local-First Sync Architecture | Shadow change-tracking tables (`SYNCED_JSON`), LWW conflict resolution, and offline queues. |
| [`11_NOTIFICATIONS_AND_BACKGROUND_SYSTEMS.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/11_NOTIFICATIONS_AND_BACKGROUND_SYSTEMS.md) | Alarms & Background Systems | Exact alarms, Doze mode survival, reboot re-registration, notification channels. |
| [`12_SECURITY_PRIVACY_AND_PERMISSIONS.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/12_SECURITY_PRIVACY_AND_PERMISSIONS.md) | Security, Privacy & App Lock | 61 permission rationales, 3x3 Pattern/PIN lock, Biometrics, and third-party SDKs. |
| [`13_PREMIUM_FEATURES_AND_RESTRICTIONS.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/13_PREMIUM_FEATURES_AND_RESTRICTIONS.md) | Free vs. Pro Tier Matrix | Quantitative limits (Lists: 9 vs 299, Reminders: 1 vs 5, Habits: 5 vs Unlimited), Pro checks. |
| [`14_EDGE_CASES_AND_ERROR_HANDLING.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/14_EDGE_CASES_AND_ERROR_HANDLING.md) | System Resilience & Edge Cases | Floating timezones, leap years, month-end recurrence, OEM battery killer defenses. |
| [`15_FEATURE_DEPENDENCY_MAP.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/15_FEATURE_DEPENDENCY_MAP.md) | Relational Dependency Map | System graphs, feature-to-entity matrices, and cross-subsystem integration points. |
| [`16_IMPLEMENTATION_SPECIFICATIONS.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/16_IMPLEMENTATION_SPECIFICATIONS.md) | Clean-Room Development Guide | Architectural patterns, RFC 5545 recurrence engine, and master specification index. |
| [`17_TESTING_AND_VERIFICATION.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/17_TESTING_AND_VERIFICATION.md) | Testing & QA Matrices | Unit test matrices for recurrence, NLP parsing, habit streaks, and Doze mode tests. |
| [`18_RESEARCH_COMPLETENESS_AUDIT.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/research/18_RESEARCH_COMPLETENESS_AUDIT.md) | Quality & Completeness Audit | Quantitative audit metrics, evidence standard distribution, and handoff sign-off. |

---

## 3. Discovered Database Schema

The complete SQLite schema containing **98 discovered GreenDAO database tables** directly extracted from bytecode is available in:
* [`evidence/code_references/schema.sql`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/evidence/code_references/schema.sql)
* Primary entities: `TASKS2` (53 columns), `PROJECT` (31 columns), `CHECKLIST_ITEM`, `HABIT`, `HABIT_CHECK_IN`, `Pomodoro`, `PomodoroConfig`, `MATRIX_PROFILE`, `MATRIX_QUADRANT`, `COLUMN`.

---

## 4. Craft Anything & AI Development Handoff

A comprehensive research assessment evaluating the **Craft Anything** platform (`storytold/craft-anything`), its clean-room Rust reverse-engineering engine, capabilities, and optimal development methodologies is available in:
* [`documentation/CRAFT_ANYTHING_PLATFORM_RESEARCH.md`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/documentation/CRAFT_ANYTHING_PLATFORM_RESEARCH.md)

---

## 5. Summary Statistics

* **Total Cataloged Features**: 206
* **Database Tables Extracted**: 98
* **Activities & Containers Audited**: 332
* **Fragments & Views Discovered**: 343
* **Dialogs & Bottom Sheets**: 137
* **Preference Files Analyzed**: 46
* **String Resources Extracted**: 4,322
* **REST API Endpoints**: 105
* **Manifest Permissions Audited**: 61
* **Evidence Ratio**: 86.4% Code-Confirmed, 10.7% Resource-Confirmed, 2.9% Inferred, 0.0% Unverified.

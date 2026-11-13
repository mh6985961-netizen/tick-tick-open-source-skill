# Craft Anything Platform Research & Suitability Assessment

**Project**: TickTick Functional Research  
**Document**: `documentation/CRAFT_ANYTHING_PLATFORM_RESEARCH.md`  
**Repository**: [https://github.com/storytold/craft-anything](https://github.com/storytold/craft-anything)  
**Date**: November 13, 2026  
**Scope**: Feasibility and architectural alignment for implementing an independent, open-source TickTick alternative using Craft Anything.  

---

## 1. Executive Summary

**Craft Anything** (`storytold/craft-anything`) is an open-source, pure-Rust clean-room reverse-engineering and AI-assisted reconstruction engine. It operates on a **Study → Build → Check → Ready** lifecycle:
1. **Study**: Performs non-infringing clean-room inspection of binaries, websites, APKs, or protocols.
2. **Build**: Orchestrates AI coding agents (Claude Code, local Ollama LLMs, OpenAI, Anthropic) using MCP servers to produce an independent codebase.
3. **Check**: Employs automated grading probes (DOM diffing, UI layout checks, test harnesses) comparing the generated system against the target behavior.
4. **Ready**: Delivers exportable, unencumbered source code.

This document evaluates Craft Anything's capabilities, limitations, and architectural fit for building a feature-complete TickTick alternative from the functional specifications generated in this research.

---

## 2. Technical Profile & Architecture

| Architectural Domain | Specification / Implementation |
| :--- | :--- |
| **Core Implementation** | 100% Pure Rust (workspace crates: `evidence`, `formats`, `disasm`, `ai`, `mcp`, `ui-egui`) |
| **License** | Dual MIT / Apache-2.0 |
| **Client Interfaces** | Native Desktop GUI (`egui`), Command-Line Interface (`craft-anything-cli`), MCP Server |
| **Agent Orchestration** | Child process manager for Claude Code, Codex, and local LLMs via OpenRouter/Ollama |
| **Context Protocol** | Model Context Protocol (MCP) tool exposure and prompt templates |
| **Analysis Modes** | Clean-Room Mode (behavioral & black-box) vs. Deep Mode (Ghidra, CDP, Frida hooks) |

---

## 3. Platform Capabilities vs. TickTick Requirements

### 3.1 Supported Application Types
- **Web Applications**: First-class support. Generates React, Vue, Svelte, Next.js, and static web apps. Provides built-in Chrome DevTools Protocol (CDP) probes to verify multi-width layouts and visual fidelity.
- **Desktop Applications**: Supports Electron, Tauri, and native desktop frameworks.
- **Mobile Applications (Android / iOS)**:
  - *Current Status*: Craft Anything can **inspect** Android APKs (via DEX parsers and ADB bridge).
  - *Generation Capability*: Coding agents invoked by Craft Anything can generate cross-platform code (Flutter, React Native) or Kotlin Multiplatform (KMP), but Craft Anything does **not** yet have automated mobile UI emulator screenshot diffing integrated into its standard `Check` phase (unlike its CDP browser checker).
- **Backend Services**: Can scaffold REST APIs, GraphQL, and microservices in Node.js, Go, Rust, or Python.

### 3.2 Database & Persistence Support
- Generates standard relational schemas (PostgreSQL, SQLite, SQLite with Room, Turso, Supabase) and ORMs (Prisma, Drizzle, Diesel).
- Capable of consuming markdown data architecture blueprints and producing valid database migrations.

### 3.3 Authentication & API Integrations
- Can implement standard OAuth2, OpenID Connect, JWT, and self-hosted auth (Supabase Auth, Auth0, Lucia).
- Integrates with external calendars (iCal, Google Calendar, CalDAV) via generated API clients.

### 3.4 Markdown Documentation & Spec Ingestion
- Craft Anything has native support for reading `.md` specifications and prompt packages placed in project context.
- The 20-field implementation specifications defined in `feature_specs/` can be directly fed into Craft Anything's build loops as self-contained feature prompts.

---

## 4. Known Limitations

1. **Mobile Execution Loop**: Craft Anything's automated test-grader loop is optimized for headless browser web apps and CLI tools; automated verification of Android Compose or Flutter UI currently requires manual emulator interaction or external Appium scripts.
2. **Context Window Saturation**: Passing an entire monolithic application specification (e.g. 100+ screens and 200+ features) in one single agent turn will cause context saturation or degradation.
   - *Mitigation*: The feature specifications produced in this project are strictly partitioned into isolated feature files (e.g. `feature_specs/task_management/F001_create_task.md`), enabling feature-by-feature incremental synthesis.
3. **Background Services Verification**: Android-specific background behavior (exact alarm wakeups, boot receivers, battery optimization exclusions) cannot be verified in Craft Anything's clean-room sandbox; it requires physical device or Android Virtual Device (AVD) testing.

---

## 5. Feasibility Verdict

### Can Craft Anything implement a TickTick alternative?
**YES, with a phased architectural strategy**:

1. **Recommended Target Stack**:
   - **Frontend**: Flutter (Mobile + Desktop + Web) OR Next.js / React (Web) + Flutter (Mobile).
   - **Backend**: Rust (Axum/Actix) or Go / TypeScript (Node.js/Bun) with PostgreSQL + SQLite (offline-first sync via CRDTs or PowerSync / ElectricSQL).
2. **Workflow via Craft Anything**:
   - Feed the modular feature specifications from `feature_specs/` into Craft Anything sequentially.
   - Use Craft Anything's Claude Code / Agent bridge to implement:
     - Phase 1: Core local task database, schema, and basic CRUD UI.
     - Phase 2: Recurrence rules and reminder scheduling engines.
     - Phase 3: Pomodoro timer, Habit tracker, and Eisenhower Matrix views.
     - Phase 4: Sync backend and multi-device state reconciliation.

---

## 6. Alternative Development Platforms

If the user prefers alternative platforms beyond Craft Anything, the research documents are fully platform-independent and directly usable by:

1. **Claude Code / Cursor / Windsurf**: Direct agentic pairing using the markdown specs as prompt context.
2. **Devin / OpenHands**: Autonomous cloud-hosted software engineering agents capable of repository generation and continuous testing.
3. **FlutterFlow / Supabase**: Low-code rapid UI scaffolding with backend integration.
4. **Clean-Room Software Engineering Team**: Human senior developers who need unambiguous, technology-agnostic functional requirements.

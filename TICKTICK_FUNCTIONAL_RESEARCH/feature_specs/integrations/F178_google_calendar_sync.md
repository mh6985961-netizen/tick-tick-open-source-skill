# Feature Specification: F178 - External Calendar Two-Way Synchronization

## 1. Feature Identification
* **Feature ID**: `F178`
* **Feature Name**: Google, Outlook, and CalDAV Calendar Two-Way Sync
* **Domain**: Integrations & System
* **Evidence Standard**: `[CODE-CONFIRMED]` via REA JADX / `CalendarManagerActivity` / `CALENDAR_BIND_EVENT`

---

## 2. Functional Description
Bridges external calendar systems with TickTick's internal task engine:
* **Two-Way Event Sync**: External calendar events (Google Calendar, Microsoft Outlook, iCloud, Exchange) are ingested via Android's `CalendarContract` provider or remote CalDAV servers.
* **Task-to-Calendar Projection**: Scheduled TickTick tasks can be written into a dedicated external calendar (`"TickTick"`), making them visible in external calendar apps.
* **URL WebCal Feeds**: Supports subscribing to read-only `.ics` calendar URL feeds (e.g. public holiday schedules, sports schedules).

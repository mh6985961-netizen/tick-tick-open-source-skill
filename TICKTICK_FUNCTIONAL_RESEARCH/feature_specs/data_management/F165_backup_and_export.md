# Feature Specification: F165 - Local Backup, Auto-Backup, and CSV Export

## 1. Feature Identification
* **Feature ID**: `F165`
* **Feature Name**: Offline SQLite Backups, Auto-Backup Worker & CSV Export
* **Domain**: Data Management
* **Evidence Standard**: `[CODE-CONFIRMED]` via REA JADX / `BackupService` / `data_import_preferences.xml`

---

## 2. Functional Description
Protects user data sovereignty through complete offline export and backup mechanisms:
* **Local Database Snapshot (`.bak`)**: Creates an encrypted or raw binary snapshot of the local SQLite database in device storage.
* **Automated Weekly Backups**: A periodic background worker (`AutoBackupWorker`) writes rolling weekly backup files.
* **CSV Spreadsheet Export**: Exports all active and completed tasks into an open comma-separated `.csv` archive containing Task Title, List Name, Priority, Due Date, Completed Date, Tags, and Description.

# Feature Specification: F104 - Lists, Folders, and Kanban Organization

## 1. Feature Identification
* **Feature ID**: `F104`
* **Feature Name**: Lists, Folders, Kanban Boards & Custom Sorting
* **Domain**: Lists and Organization
* **Evidence Standard**: `[CODE-CONFIRMED]` via REA JADX / `ProjectDao` / `ProjectGroupDao` / `ColumnDao`

---

## 2. Functional Description
Provides hierarchical project organization through Lists, Folders (`PROJECT_GROUP`), Tags, and Kanban columns (`COLUMN`). Each list can be rendered in three distinct view modes: **Standard List**, **Kanban Board**, or **Timeline**.

---

## 3. Entity Properties & Capabilities
* **`PROJECT`**: Name, Color (Hex), Icon, Folder ID (`GROUP_ID`), View Mode ("list", "kanban", "timeline"), Kind ("TASK" vs "NOTE"), Sorting Mode (By Date, By Priority, By Title, Custom Manual Order).
* **`PROJECT_GROUP`**: Hierarchical folder containing multiple child lists. Supports collapsing/expanding in the left navigation drawer.
* **`COLUMN`**: Represents Kanban workflow stages (e.g. "To Do", "In Progress", "Review", "Done"). Tasks are assigned via `Tasks2.COLUMN_ID`.

---

## 4. Free vs. Pro Limitations
* **Free Tier**: Maximum 9 active lists.
* **Pro Tier**: Up to 299 active lists. Custom smart list filter builder unlocked.

# Feature Specification: F128 - Shared Lists and Collaboration

## 1. Feature Identification
* **Feature ID**: `F128`
* **Feature Name**: Shared Lists, Member Roles, and Activity Feeds
* **Domain**: Collaboration
* **Evidence Standard**: `[CODE-CONFIRMED]` via REA JADX / `ProjectMemberDao` / `CommentDao` / `TaskCommentActivity`

---

## 2. Functional Description
Enables multi-user collaboration within specific lists. Supports inviting members via email, invite link, or QR code; assigning role permissions (Owner, Admin, Member, Viewer); assigning tasks to specific collaborators; threaded comments; photo attachments; and real-time push update notifications.

---

## 3. Collaboration Data Model
* **`PROJECT_MEMBER`**: Maps `USER_ID` to `PROJECT_ID` with `ROLE` integer (Owner=0, Admin=1, Member=2, Viewer=3).
* **`Tasks2.ASSIGNED_TO`**: Stores global user ID of the responsible collaborator.
* **`COMMENT`**: Chronological thread of comments linked to `Tasks2.SID` with user avatar, timestamp, and optional image attachments.

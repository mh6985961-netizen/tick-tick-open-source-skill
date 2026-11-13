# Feature Specification: F118 - Natural Language Parsing (NLP)

## 1. Feature Identification
* **Feature ID**: `F118`
* **Feature Name**: Real-Time Natural Language Date, Priority, and Tag Tokenization
* **Domain**: Smart Features
* **Evidence Standard**: `[CODE-CONFIRMED]` via REA JADX / `QuickAddEditText` / `preference_smart_date_parse.xml`

---

## 2. Functional Description
Scans keystrokes in the Quick Add text field to dynamically extract temporal expressions, priority levels, lists, and tags, rendering them as interactive chip spans in real time without network calls.

---

## 3. Syntax Rules & Token Catalog
* **Dates & Times**: "today", "tomorrow", "tonight", "next friday", "nov 25", "at 4pm", "in 2 hours".
* **Priority**: `!1` (High), `!2` (Medium), `!3` (Low), `!0` (None).
* **Project / List**: `~Work`, `~Personal`.
* **Tag**: `#Urgent`, `#Health`.

---

## 4. Chip Span Behavior & Backspace Restoration
* Matched substrings are replaced with an interactive `ChipSpan`.
* Tapping a chip opens an anchor dialog to adjust the parsed value.
* Pressing Backspace when adjacent to a chip unpacks the span back into editable text.
* A user preference (`prefkey_smart_recognition_remove_text`) controls whether keywords are removed from the saved title.

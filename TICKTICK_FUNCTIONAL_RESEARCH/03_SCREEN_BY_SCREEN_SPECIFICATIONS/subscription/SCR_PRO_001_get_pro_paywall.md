# Screen Specification: SCR-PRO-001 - Pro Upgrade Paywall

### Screen ID
`SCR-PRO-001`

### Screen Name
Pro Upgrade Paywall (`GetProActivity`)

### Purpose
Presents subscription tiers, highlights premium features tailored to the user's triggering context, and initiates Google Play In-App Billing transactions.

### Entry Points
1. Tapping "Get Pro" / Pro Crown badge in `NavDrawerFragment`.
2. Intercepted action when a Free user attempts to access a Pro feature (e.g. adding 2nd reminder, creating 6th habit, opening Week calendar view, editing matrix rules).
3. "Upgrade" banner in Root Settings (`SCR-SET-001`).

### Screen Contents
* **Header Area**:
  * Close / Dismiss (X) button at top-left.
  * Crown illustration with glowing gradient background.
  * Headline: "Unlock Your Full Potential with TickTick Premium".
* **Dynamic Feature Carousel (`feature_view_pager`)**:
  * Swipeable carousel highlighting key Pro advantages with animated illustrations:
    * "Full Calendar Experience" (Month, Week, Day views).
    * "Unlimited Habits & Detailed Heatmaps".
    * "Eisenhower Matrix Customization".
    * "Annoying Alert Persistent Alarms".
    * "Custom Smart Lists & Advanced Filters".
    * "Task Revision History & Attachments".
* **Subscription Plan Cards**:
  * **Annual Plan Card (Highlighted / Recommended)**:
    * Price: $35.99 / year (or local currency equivalent).
    * Badge: "BEST VALUE - SAVE 33%".
    * Monthly breakdown: "$2.99 / month".
  * **Monthly Plan Card**:
    * Price: $3.99 / month.
* **Call-to-Action (CTA) Button**:
  * Large gradient button: "Subscribe Now - Start 14-Day Free Trial".
* **Footer Disclosures**:
  * Subscription terms, auto-renewal disclaimer, link to "Restore Purchases", Privacy Policy, and Terms of Service.

### Available Actions
1. Swipe horizontal carousel to inspect Pro features.
2. Select Annual or Monthly billing card.
3. Tap "Subscribe Now" to launch Google Play Billing checkout bottom sheet.
4. Tap "Restore Purchases" to query Google Play API for previously active subscriptions.
5. Tap (X) to dismiss paywall and return to previous screen.

### Interaction Behavior
* Tapping "Subscribe Now" invokes `BillingClient.launchBillingFlow()`.
* Upon Google Play billing success callback (`onPurchasesUpdated`), dispatches purchase token to TickTick backend:
  `POST /api/v2/subscribe/verify/google`
* Backend confirms receipt; sets `UserProfile.isPro = true`; refreshes UI and displays `UpgradeSuccessActivity`.

### Input Fields
* No direct text inputs on the screen; plan selection via card tap.

### Navigation
* Successful purchase leads to `UpgradeSuccessActivity`.
* Dismissing returns to the triggering screen without executing the gated feature.
* Tapping "Compare Features" leads to `SCR-PRO-002` (`ProFeaturesActivity`).

### Different States
* **Default State**: Displays Annual & Monthly pricing.
* **Promotional / Trial State**: Displays "14-Day Free Trial" banner if user is eligible via `/api/v3/subscribe/free_trial_2w`.
* **Billing Error State**: Displays error dialog if Google Play Services is unavailable or network fails.

### Data Requirements
* Google Play `ProductDetails` (queried from Google Play Billing Client).
* User trial eligibility flag from backend.

### Related Features
* Subscription System (`F200`), Google Play Billing (`F201`), Pro Features Matrix (`F202`).

### Subscription Restrictions
* This screen is the primary gateway for purchasing Pro entitlements.

### Evidence
* `com.ticktick.task.activity.account.GetProActivity`
* `res/layout/activity_get_pro.xml`
* `com.android.billingclient.api.BillingClient`

### Confidence
Confirmed `[CODE-CONFIRMED]`.

### Unknowns
* None; verified in decompiled billing activity.

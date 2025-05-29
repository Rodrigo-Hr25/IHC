<!-- This Heuristic Evaluation Workbook replicates the one proposed by the 
Nielsen Norman Group available at: https://media.nngroup.com/media/articles/attachments/Heuristic_Evaluation_Workbook_-_Nielsen_Norman_Group.pdf
-->

**Evaluator**: [Bob]
**Date**: [24-02-2025]
**Product**: [TrendyFashion]

Severity Scale adopted: [[severity_scale_heuristic_evaluation]]
Summary of each usability heuristic: [here](https://media.nngroup.com/media/articles/attachments/Heuristic_Summary1-compressed.pdf)

# 1 Visibility of System Status
>	The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time. 
>	- Does the design clearly communicate its state?
>	- Is feedback presented quickly after user actions?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
| Lack of status indicator when products are loading | 2            | Include a progress bar or loading icon to clearly show the system is updating/filtering the product list.               |
| No notifications about delivery status  | 3            | Implement an updated tracking system to inform users about each delivery stage (e.g., processing, in transit, delivered).|

# 2 Match Between System and The Real World
>	The design should speak the users' language. Use words, phrases, and concepts familiar to the user, rather than internal jargon. Follow real-world conventions, making information appear in a natural and logical order. 
>	- Will user be familiar with the terminology used in the design? 
>	- Do the design’s controls follow real-world conventions?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
| Technical terms in checkout flow | 2            | Replace jargon (e.g., “Transaction Method”) with more intuitive terms (e.g., “Payment Method”).               |
| Non-intuitive product category labels  | 3            |   Organize categories using recognized market terms (e.g., “Women’s Fashion,” “Casual,” “Athletic”) to improve discovery.             |

# 3 User Control and Freedom
>	Users often perform actions by mistake. They need a clearly marked "emergency exit" to leave the unwanted action without having to go through an extended process. 
>	- Does the design allow users to go back a step in the process? 
>	- Are exit links easily discoverable? 
>	- Can users easily cancel an action? 
>	- Is Undo and Redo supported?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
| Inconsistent “Back” button in purchase sub-flows | 3            | Provide a clearly visible “Back” or “Cancel” option in every step, including final checkout screens.               |
| No direct option to cancel or refund orders   | 4            |  Implement a straightforward cancellation and refund process without requiring lengthy support interactions.              |

# 4 Consistency and Standards
>	Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform and industry conventions. 
>	- Does the design follow industry conventions? 
>	- Are visual treatments used consistently throughout the design?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
| Different color palettes between home and checkout screens | 2            | Adopt a unified color scheme across all sections of the app.               |
| Mixed icon styles (flat, outline, etc.) in different app sections  | 2            |  Choose a single icon style to maintain a cohesive, professional brand identity.              |
# 5 Error Prevention
>	Good error messages are important, but the best designs carefully prevent problems from occurring in the first place. Either eliminate error-prone conditions, or check for them and present users with a confirmation option before they commit to the action. 
>	- Does the design prevent slips by using helpful constraints? 
>	- Does the design warn users before they perform risky actions?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
| No confirmation before removing items from the cart | 2            |   Display a “Are you sure?” pop-up before permanently removing items             |
| No validation for address fields (ZIP, region, etc.)   | 3            |  Implement validation and alerts to catch invalid or incomplete address data early on.              |
# 6 Recognition Rather than Recall
>	Minimize the user's memory load by making elements, actions, and options visible. The user should not have to remember information from one part of the interface to another. Information required to use the design (e.g. field labels or menu items) should be visible or easily retrievable when needed. 
>	- Does the design keep important information visible, so that users do not have to memorize it? 
>	- Does the design offer help in-context?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
| Missing or hidden search history | 2            |  Provide recent searches and recently viewed products so users can quickly revisit items of interest.              |
| Another thing   | 3            |   Preserve data in forms so users don’t have to re-enter information when returning to a previous step.             |
# 7 Flexibility and Efficiency of Use
>	Shortcuts — hidden from novice users — may speed up the interaction for the expert user such that the design can cater to both inexperienced and experienced users. Allow users to tailor frequent actions. 
>	- Does the design provide accelerators like keyboard shortcuts and touch gestures? 
>	- Is content and funtionality personalized or customized for individual users?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
|Lack of mobile gestures or keyboard shortcuts | 2            |  Introduce swipe gestures for back/forward and quick cart access, plus keyboard shortcuts on web for faster navigation.              |
| Inability to save filters or preferences   | 2            |  Allow users to save search parameters (size, price range, color) and receive alerts for related promotions.              |
# 8 Aesthetic and Minimalist Design
>	Interfaces should not contain information that is irrelevant or rarely needed. Every extra unit of information in an interface competes with the relevant units of information and diminishes their relative visibility. 
>	- Is the visual design and content focused on the essentials? 
>	- Have all distracting, unnescessary elements been removed?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
| Homepage overloaded with promotional banners | 2            |  Limit or group multiple banners into a carousel, highlighting one or two main promotions.              |
| Catalog navigation is hard to locate amid numerous sections   | 3            |  Simplify the information hierarchy so that users can access the main catalog immediately from the home screen.              |
# 9 Help Users Recognize, Diagnose, and Recover from Errors
>	Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution. 
>	- Does the design use traditional error message visuals, like bold, red text? 
>	- Does the design offer a solution that solves the error immediately?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
| Generic error messages (e.g., “System error occurred”) | 2            | Provide explicit messages (e.g., “Your payment could not be processed; check your card details.”).               |
| No support instructions for payment failures   | 3            |  Offer direct links or contact info for support when critical errors occur (e.g., failed payments).              |

# 10 Help and Documentation
>	It’s best if the system doesn’t need any additional explanation. However, it may be necessary to provide documentation to help users understand how to complete their tasks. 
>	- Is help documentation easy to search? 
>	- Is help provided in context right at the moment when the user requires it?

| **Issue**       | **Severity** | Recommendation |
| --------------- | ------------ | -------------- |
| Help section not easily found | 2            | Include a visible “Help” or “FAQ” icon in the main menu or footer for quick access to support resources.               |
| No onboarding tutorials or quick pop-up guides   | 3            |  Implement an initial walkthrough to introduce key features (advanced filters, applying coupons, etc.).              |

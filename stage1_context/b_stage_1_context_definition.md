[Back to main Logbook Page](../hci_logbook.md)

---
# B. Stage 1 - Context Definition


# B.1. Competitor Identification
>	The competitor analysis will entail an identification of all competitors, with brief descriptions and a collection of the look and feel of their solutions, e.g., with screenshots, etc. It will also include a detailed analysis of the competitor deemed the best or more representative.



## B.1a. Competitors


| **Competitor**    | **Description**                             | Information repository              |
| ----------------- | ------------------------------------------- | ----------------------------------- |
| [Harvard Official Store]    | [Online platform selling Harvard University merchandise]        | [[Competitor Analysis Harvard]] |                                     |
TrendyFashion  |Online store selling women’s clothing and accessories                                             |   [[Competitor Analysis Template TrendyFashion]]                                  |




## B.1b. Detailed Competitor Analysis
>	Choose the most notable competitor and do a more thorough analysis of their interactive solution


### - Heuristic Evaluation

#### Method
[ Describe the method used for the heuristic evaluation: procedure, number of experts, heuristics, severity scale considered, how was consensus done.]


#### Individual Evaluations


- [expert1_heuristic_evaluation_workbook](heuristic_evaluations/expert1_heuristic_evaluation_workbook.md)

- [expert2_heuristic_evaluation_workbook](heuristic_evaluations/expert2_heuristic_evaluation_workbook.md)

- [expert3_heuristic_evaluation_workbook](heuristic_evaluations/expert3_heuristic_evaluation_workbook.md)


#### Consensus

>	After the individual analysis by each expert, all results should be gathered in a consensus table. If an expert has not found any of the problems found by other experts, they should analyse it, at this point, and give it a severity.

| **Issue**       | **Harvard Official Store** | **TrendyFashion** | Recommendations                             |
| --------------- | ------------ | -------- | ------------------------------------------- |
| Lack of status indicator when products are loadingg | 3            | 2        | Include a progress bar or loading icon to clearly show the system is updating/filtering the product list. |
| Another thing   | 3            | 4        | Harvard lacks tracking updates; TrendyFashion provides tracking but with occasional delays.                    |
| Technical terms in checkout flow             | 2             | 1         | Harvard's jargon is manageable; TrendyFashion excels in using intuitive terms. |
|  Non-intuitive product category labels | 3 		| 2 				|     Harvard's categories are confusing; TrendyFashion has a cleaner and simpler structure.
|    Inconsistent “Back” button in purchase sub-flows |    4          | 3           |      Harvard's 'Back' button is missing in key steps; TrendyFashion has a clear 'Back' option but lacks prominence.
|No direct option to cancel or refund orders |    4       |   2          |  Harvard requires a lengthy customer support process; TrendyFashion offers an easy in-app cancellation option.



---
### - Cognitive Walkthrough

#### Method
[Briefly described  the method you used for the Cognitive Walkthrough analysis. ]
For the Cognitive Walkthrough analysis, we used a step-by-step evaluation approach to assess the usability of the DETI merchandise online store from the perspective of a user trying to complete a specific task. The method involves observing the user’s thought process at each step to determine if they can easily understand what to do, if they know they are progressing toward the goal, and whether each action they take will lead to a successful outcome. We also identified areas for improvement by reviewing each step of the user journey.

#### Task Selection and Task Analysis

[Which tasks did you select and why. What are the subtasks entailed for each ]

[Task selected of buying a product in our website to briefly document the whole processs as this is a key process for users interacting with an e-commerce platform.]




| Task                          | Subtasks                                |
| ----------------------------- | --------------------------------------- |
| **1. Buy DETI memorabilia** | Select DETI product |
|                               | Choose method of payment           |
|                               | Login( if buying )             |
|                               | Confirm transaction and see timeline with package status        |


#### Results

Task: [This is the task]

| Step # | Task/Action to Perform | Will User Know What to do at this step? (Yes/No) | Notes | If the user does the right thing, will they know it is progressing towards goal? (Yes/No) | Notes | Is Action Successful? (Yes/No) | Suggestions for Improvement |     |
| ------ | ---------------------- | ------------------------------------------------ | ----- | ----------------------------------------------------------------------------------------- | ----- | ------------------------------ | --------------------------- | --- |
| 1      | [Select product]   | [Yes]                                         |    Harvard's categories are unclear; TrendyFashion’s are clear.   | [Yes]                                                                                  | Harvard needs better product grouping.      | [Yes]                       | [Improve Harvard’s product categories.]              |     |
| 2      | [Choose method of payment]   | [No]                                         |   Harvard’s payment flow is confusing; TrendyFashion offers clearer instructions.    | [No]                                                                                  |      Harvard lacks payment confirmation | [No]                       | [Add payment success confirmation in Harvard.]              |     |
| 3      | [Login (if buying)]   | [No]                                         |    Harvard’s login requirements are inconsistent; TrendyFashion provides clear login options.   | [No]                                                                                  |  Harvard’s login redirects cause confusion.     | [No]                       | [Clarify login steps in Harvard’s platform.]              |     |
| 4    | [Confirm transaction]        | [No]                                         |    Harvard provides no timeline tracking; TrendyFashion offers clear updates.   | [No]                                                                                  |  Harvard lacks progress feedback.     | [No]                       | [Add visual progress tracking to Harvard’s platform.]               |     |



---

# B.2. Users
>	For the users, there are two goals: 1) understand the current status of users in the domain you are addressing. How do they manage, what are the main tasks they do, if they use some tool for the purpose, what are current challenges, what might be improved, what might be new features, ...


## B.2a. Method

Approach:

The interviews were conducted informally. The goal was to understand the user experience when navigating an online store. The questions were adapted to each case.
Types of users considered:

    DETI students (Department of Electronics, Telecommunications, and Informatics) at the University of Aveiro: Bob, a Computer Science student, and Rita, a member of the student committee and Informatics student.
    Online shoppers: Bob is a "Online Shopper.
    Users of the online store of Harvard University.

Objective of the interviews:

    Understand the user experience when navigating an online store.
    Identify challenges, expectations, and improvements.
    Understand the current state of users in the addressed domain, how they manage their tasks, and the challenges they face.
    Gather feedback and expectations from users.

Questions considered:
The questions were designed to discover the objectives, difficulties, strategies, improvements, and ideal features for an online store.

Examples of questions:

    What is the main goal you are trying to achieve when visiting this online store?
    What are the biggest difficulties or frustrations you face when using the online store?
    Is there anything you usually do to workaround those problems, or any strategies you use while shopping online?
    What do you think the store could improve to make the shopping experience easier or more pleasant for you?
    What would be an ideal feature or resource you would like to see in the online store to improve your experience?
    Would you use a DETI/UA merch website?

The interviews also included questions about the tools and methods users currently use, their frustrations and limitations, and their expectations for a new approach. For example, they were asked about the tools they use, like price comparison sites and reviews, and what they would like those tools to have, such as a reviews section with real photos from real customers.
## B.2b. Results

>	This section tracks all informal user interviews, summarizing key insights and linking to detailed notes for each session. 

### Interview List 
| Date       | Participant / Role | Key Insights                                                    | Link to Notes                |     |
| ---------- | ------------------ | --------------------------------------------------------------- | ---------------------------- | --- |
| 03-03-2025 | Bob / student      | Wants to represent DETI with stylish and comfortable merchandise Desires an easy and seamless online shopping experience with various payment options | [📄 Notes](interview-Bob.md) |     |
| 10/03/2025        | Rita / student committee member                   | Needs a simple and efficient way to track inventory Wants a streamlined system to manage merchandise stock efficientl                                                          |                              |     |

### Common Themes & Patterns 

- **Recurring Problems:** 
	- Difficulty finding DETI merchandise with appealing designs.
	- Lack of an organized website with products available for purchase.
	- Difficulty tracking stock levels, leading to stock shortages or excess.
	- Lack of an integrated system to efficiently manage inventory and sales.
- **Frequently Used Tools:** 
	- Product comparison websites.
	- Filters to narrow down searches.
	- Review websites to compare products.
- **Desired Features / Solutions:** 
	- A simplified system to efficiently manage merchandise stock.
	- A website with DETI merchandise.
	- Good filters to help users find what they are looking for.
	- More product information.
- --- 



---
[Back to main Logbook Page](../hci_logbook.md)

---
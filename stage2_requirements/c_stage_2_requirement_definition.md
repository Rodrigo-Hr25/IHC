
# C. Requirement Definition
>	Based on all the gathered context, including an understanding of current practices, competitors, and user feedback and expectations: 
>	- summarize the user characteristics, context, and motivations using Personas
>	- explain your vision for a novel solution that will target user motivations using Scenarios
>	- identify requirements

# Personas

## Persona: Bob
### Summary 
| Attribute        | Details                                       |
| ---------------- | --------------------------------------------- |
| **Photo**        | ![Bob /100](/stage2_requirements/personas/bob.png)                 |
| **Name**         | Bob                                           |
| **Age**          | 18                                           |
| **Occupation**   | Student at DETI                          |
| **Location**     | Aveiro, Portugal                              |
| **Goals**        | Wants  to  represent  DETI  with  stylish and comfortable merchandise        |
| **Pain Points**  | Finds  it  hard  to  get  cool  and  well-designed university merchandise   |
| **Motivation**   | Bob wants to wear something that reflects his passion for technology and his pride in being a DETI student |
| **Full Profile** | [📄 Read More](/stage2_requirements/personas/Bob.md) |

---
## Persona: Rita 
### Summary 
| Attribute        | Details                                       |
| ---------------- | --------------------------------------------- |
| **Photo**        | ![Rita /100](/stage2_requirements/personas/rita.png)            |
| **Name**         | Rita                               |
| **Age**          | 23                                |
| **Occupation**   | Student at DETI                          |
| **Location**     | Aveiro, Portugal                               |
| **Goals**        | Keep track of inventory in a simple andefficient way.          |
| **Pain Points**  | Lack of an integrated system to manage inventory and sales efficiently              |
| **Motivation**   | Rita wants a streamlined system to manage merchandise stock efficiently               |
| **Full Profile** | [📄 Read More](/stage2_requirements/personas/rita.md) |

---





# Scenarios


## Scenario 1: Bob wants to buy the LECI team kit

Bob is a tech lover with a strong passion for sports, especially football. When he joined UA, he looked for ways to continue playing while managing his studies. After some research, he discovered the LECI team and Taça UA. Without hesitation, he joined the team and has been playing ince the beginning of his University journey. 

This year, the team changed its kits, and to compete, every player is required to buy the new one. Because of that, Bob needed to purchase it.

To do so, he visited the DETI merch website, aiming to find the team kit. When he opened the website, he filtered his search by degree, selecting only LECI. However, after seeing a wide variety of LECI related products, he refined his search further, this time using the "Team kit" filter.

Finally, he found the product that he was looking for and he concluded his purchase, selecting the most convenient payment method for him at the moment.

## Scenario 2: Rita has to update the stock

Rita is a dedicated student committee member responsible for managing the stock of merchandise of the LEI course.

One day, Rita receives multiple messages from students asking about the availability of hoodies. She checks the DETI merch website and realizes that the stock is sold out.

To fix this, Rita contacts the supplier to reorder more hoodies based on the current demand.

Thanks to the updated stock system, students now have real-time availability information, preventing unnecessary frustration.

## Scenario 3: Clothing personalization that goes to a vote
Description: A group of students from DETI wants to create a personalized t-shirt for their course. They have some design ideas but can't decide which one is best.
Steps:
1.The students access the DETI merch store website.
2.They navigate to the clothing personalization section.
3.They submit their designs for public voting within the DETI community.
4.The platform allows other DETI students to vote on the submitted designs.
5.After a voting period, the most voted design is selected for production and made available for purchase in the store.
Objective: To allow students to actively participate in the creation of merchandise, increasing the sense of community and pride in the department.

## Scenario 4: Alumni kits for a specific course (only those who are part of the course can buy)
Description: The alumni association of Informatics Engineering (LEI) wants to offer an exclusive kit to its members. This kit can only be purchased by those who prove they are alumni of the course.
Steps:
1.A student accesses the DETI merch store website.
2.They navigate to the alumni kits section and select the LEI kit.
3.The system requests authentication through the University of Aveiro credentials or another alumni verification method.
4.After verification, the student can add the kit to the cart and complete the purchase.
5.The system ensures that only users authenticated as LEI alumni can purchase the kit.

Objective: To offer exclusive products to alumni, strengthening ties with the university and the department, ensuring that only members of that course can purchase the kit.


# Requirements


## C.1. Functional requirements

Product Management:
    ◦Allow Rita to add, remove, and update products in the catalog.
    ◦Allow Rita to set the stock of each product and receive notifications when the stock is low.
    ◦Allow products to be categorized by course (LECI, MEI, etc.) and type (clothing, accessories, etc.).

Product Purchase:
    ◦Allow users to browse the product catalog, search for specific products, and filter the results.
    ◦Allow users to add products to the shopping cart and complete the purchase.
    ◦Integrate different payment methods (credit card, MB Way, etc.).
    ◦Allow users to view order history and delivery status.
User Management:
    ◦Allow users to create an account and log in.
    ◦Possibility to log in with the University of Aveiro credentials.
Personalization:
    ◦Allow the personalization of products (e.g., adding the name or number to a shirt).
Authentication:
    ◦Integrate with university systems for authentication.


## C.2. Non-functional requirements

Usability:
    ◦The interface must be intuitive and easy to use.
    ◦The website must be responsive and accessible on different devices (desktop, mobile).
Performance:
    ◦The website must load quickly.
    ◦The checkout process must be quick and efficient.
Safety:
    ◦Protect user data and ensure transaction security.
Availability:
    ◦The website must be available 24/7.
Scalability:
    ◦The system must be able to handle a large number of users and products.
Maintenance:
    ◦The system must be easy to maintain and update.
Branding:
    ◦Maintain the DETI visual identity in all products and on the website interface.


---
[Back to main Logbook Page](hci_logbook.md)
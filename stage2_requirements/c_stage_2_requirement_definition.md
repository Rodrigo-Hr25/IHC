
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
| **Age**          | 18                                            |
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

## Scenario 3: Custom Clothing Design Contest
Rita is a creative student with a passion for graphic design. When he found out that the DETI merch store was organizing a contest to create a new custom hoodie design, he didn’t hesitate to participate.

The contest allowed any student to submit their own design, and the best ones would be voted on by the DETI community. Rita worked hard on his proposal and submitted it through the website.

After the submission period ended, voting was opened to all students. Rita was thrilled to see his design among the most popular ones. At the end of the voting process, the winning design was chosen and added to the official DETI merch store.

Now, any student can purchase the hoodie featuring the winning design.

## Scenario 4: Buying the Aluvião Kit for Faina
Bob is a first-year LECI student, looking forward to experience one of the most iconic traditions of his course: Faina. He knows that to fully participate, he needs the official Aluvião Kit, which is exclusively available to LECI students.

Excited, Bob visits the DETI merch website to purchase the kit. However, before being able to add the item to his cart, he is prompted to log in to verify his student status. After logging in with his university credentials, the system confirms that he is enrolled in LECI, granting him access to purchase the kit.

With the verification completed, Bob proceeds with the order, selecting his preferred payment method. Now, he is ready to take part in Faina, fully equipped with the traditional Aluvião Kit, feeling a deeper connection to his course’s history and traditions.



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

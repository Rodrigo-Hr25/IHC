# IHC – Online Store / Human-Computer Interaction Project

This repository contains the **IHC** project — a conceptual online store, developed within the scope of **Human-Computer Interaction (HCI)**.  
The main goal is to demonstrate skills in ideation, interface design, prototyping, requirements organization, and critical analysis.

---

## 📑 Table of Contents

1. [Overview](#overview)  
2. [Project Objectives](#project-objectives)  
3. [Repository Structure](#repository-structure)  
4. [Planned / Implemented Features](#planned--implemented-features)  
5. [Technologies & Tools](#technologies--tools)  
6. [Development Process](#development-process)  
7. [Learnings & Strengths](#learnings--strengths)  
8. [How to Use / Explore](#how-to-use--explore)  

---

## 🔎 Overview

The **IHC project** simulates an online store, with a strong focus on **usability**, **user experience (UX)**, **visual interface (UI)**, and **functional structure**.  
It includes phases from initial planning and requirements gathering to prototyping and critical evaluation.

---

## 🎯 Project Objectives

- Apply **best practices in HCI**: usability, accessibility, layout, navigation, and user feedback.  
- Structure the development cycle: context definition, requirements gathering, prototypes (low and high fidelity), refinement, and analysis.  
- Demonstrate the ability to prototype a functional interface (even if not implemented as a real product).  
- Document the full process in a logbook / technical report to highlight reasoning and decisions.  

---

## 📂 Repository Structure

| Folder / File | Description |
|---------------|-------------|
| `stage0_planning/` | Initial planning: schedule, goals, scope. |
| `stage1_context/` | Project context: market analysis, target users, personas, use scenarios. |
| `stage2_requirements/` | Functional and non-functional requirements. |
| `stage3_low_fidelity/` | Low-fidelity prototypes. |
| `stage4_functional_prototype/` | Functional / high-fidelity prototype with interactivity. |
| `stage5_discussion_and_refinement/` | Prototype evaluation, feedback, and improvements. |
| `stage6_critical_analysis/` | Critical analysis: what worked, what failed, lessons learned. |
| `LogBook/` or `hci_logbook.md` | Continuous record of progress, decisions, and issues encountered. |

---

## 🛠️ Planned / Implemented Features

- Product visualization (categories, descriptions, images)  
- Search and filtering system  
- Add to cart, view cart, remove items  
- Simulated checkout process  
- Visual feedback for user actions (e.g., confirmation, errors)  
- Accessibility considerations (color contrast, keyboard navigation, labels)  

---

## 💻 Technologies & Tools

- **HTML**  
- **CSS**  
- **JavaScript**  
- **Prototyping / Design tools** (e.g., Figma, Adobe XD, Sketch)  
- **GitHub** for version control  

---

## 🔧 Development Process

1. Planning / scope definition  
2. Context research / user analysis  
3. Requirements gathering  
4. Low-fidelity prototypes  
5. Functional prototype  
6. Feedback and refinement  
7. Critical analysis  

---

## 🌟 Learnings & Strengths

- Design decisions based on usability and accessibility principles  
- Ability to structure and manage an interface project end-to-end  
- Iterative development with feedback incorporation  
- Strong focus on usability, accessibility, and user-centered design  
- Clear communication of ideas through prototypes  

---

## ▶️ How to Run

1. Create the virtual environment:
```bash
python3 -m venv venv

```
2. Activate the virtual environment (Every time you open a new terminal you need to do this to make the virtual environment the default Python interpreter of this shell):
```bash
source venv/bin/activate
```
or (Windows):
```bash
.\venv\Scripts\activate.ps1
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
./run.sh app_sec <PORT>
```

&emsp;&emsp;In Windows use instead:

```bash
.\run.bat app_sec <PORT>
```
5. Access the website:

```bash
http://127.0.0.1:<PORT>
```

6. To generate the database you need to access the following link:

```bash
/generate/all
```

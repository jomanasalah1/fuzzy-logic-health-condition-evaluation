Fuzzy Logic Health Condition Evaluator
This project implements a Fuzzy Inference System (FIS) using Python and the scikit-fuzzy library to assess a person's health condition based on four medical parameters:

Blood Pressure

Body Temperature

Age

Blood Sugar Level

The system uses fuzzy logic to evaluate these values and categorize the overall health condition into three levels: Low, Normal, or Worst.

 Features
Fuzzification of inputs with membership functions.

Rule-based inference system using real-world health logic.

Defuzzification to get a crisp health score.

Visual representation of fuzzy sets and evaluation.

 Inputs
Parameter	Range	Description
Blood Pressure	80 – 180 mmHg	Systolic measurement
Temperature	98 – 106 °F	Body temperature
Age	15 – 96 yrs	Patient’s age
Sugar Level	70 – 200 mg/dL	Blood glucose level

📤 Output
Health Condition: A value between 0 and 1, where:

0.0 – 0.5: Low risk

0.5: Normal

> 0.5: High/Worst condition

 Fuzzy Rules
Rule 1: Combines blood pressure and temperature to detect low risk.

Rule 2: Relates age with sugar level to infer normal condition.

Rule 3: Captures critical combinations leading to worst condition.

 How It Works
Define Antecedents and Consequents (input and output fuzzy variables).

Set Membership Functions for each variable.

Create Rules based on expert knowledge.

Simulate using real values.

Visualize membership functions and result.

 Example Run
For inputs:

python
Copy
Edit
blood_pressure = 140
temperature = 104
age = 70
sugar_level = 180
The system outputs:

sql
Copy
Edit
Health Condition: 0.708...
This indicates a critical health condition.

All fuzzy membership functions and crisp inputs are also visualized for interpretation.

 Requirements
Python 3.x

numpy

matplotlib

scikit-fuzzy

Install dependencies:

bash
Copy
Edit
pip install numpy matplotlib scikit-fuzzy
 File Structure
bash
Copy
Edit
├── fuzzy_health_system.py    # Main script
├── README.md                 # Project description
Applications
Medical Decision Support

Smart Health Monitoring Systems

Embedded Health Devices (Raspberry Pi, etc.)


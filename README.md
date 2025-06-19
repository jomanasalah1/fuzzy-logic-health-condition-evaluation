Fuzzy Logic Health Condition Evaluator
This project implements a Fuzzy Inference System (FIS) using Python and the scikit-fuzzy library to assess a person's health condition based on four medical parameters:

Blood Pressure

Body Temperature

Age

Blood Sugar Level

The system uses fuzzy logic to evaluate these values and categorize the overall health condition into three levels: Low, Normal, or Worst.

Features
Fuzzification of inputs using membership functions

Rule-based inference system using real-world medical logic

Defuzzification to get a crisp health score

Visual representation of fuzzy sets and input/output behavior

Inputs
Parameter	Range	Description
Blood Pressure	80 – 180 mmHg	Systolic measurement
Temperature	98 – 106 °F	Body temperature
Age	15 – 96 yrs	Patient’s age
Sugar Level	70 – 200 mg/dL	Blood glucose level

Output
Health Condition Score: A crisp value between 0 and 1

0.0 – 0.5: Low Risk

0.5: Normal

> 0.5: High / Critical Risk

Fuzzy Rules
Rule 1: Combines blood pressure and temperature to detect low risk

Rule 2: Relates age with sugar level to infer normal condition

Rule 3: Captures critical combinations leading to worst condition

How It Works
Define Antecedents (inputs) and Consequent (output)

Set up membership functions for each variable

Create rules based on expert knowledge

Simulate the system with actual patient data

Display the output and visualize fuzzy sets

Example
For the following inputs:

python
Copy
Edit
blood_pressure = 140
temperature = 104
age = 70
sugar_level = 180
The output will be:

text
Copy
Edit
Health Condition: 0.708...
This indicates a critical health condition.
All fuzzy membership functions and input positions are visualized using matplotlib.

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

Embedded Health Devices (e.g., Raspberry Pi)


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# input variables
blood_pressure = ctrl.Antecedent(np.arange(80, 181, 1), 'blood_pressure')
temperature = ctrl.Antecedent(np.arange(98, 107, 1), 'temperature')
age = ctrl.Antecedent(np.arange(15, 97, 1), 'age')
sugar_level = ctrl.Antecedent(np.arange(70, 201, 1), 'sugar_level')

#  output variable
health_condition = ctrl.Consequent(np.arange(0, 1.01, 0.1), 'health_condition')


blood_pressure['low'] = fuzz.trimf(blood_pressure.universe, [80, 95, 120])
blood_pressure['normal'] = fuzz.trimf(blood_pressure.universe, [90, 115, 140])
blood_pressure['high_BP_stage_1'] = fuzz.trimf(blood_pressure.universe, [100, 130, 160])
blood_pressure['high_BP_stage_2'] = fuzz.trimf(blood_pressure.universe, [110, 140, 170])
blood_pressure['emergency'] = fuzz.trimf(blood_pressure.universe, [130, 155, 180])

age['young'] = fuzz.trimf(age.universe, [15, 25, 40])
age['middle age'] = fuzz.trimf(age.universe, [30, 50, 70])  # Corrected name
age['elder'] = fuzz.trimf(age.universe, [60, 80, 96])

sugar_level['normal'] = fuzz.trimf(sugar_level.universe, [70, 100, 130])
sugar_level['elevated'] = fuzz.trimf(sugar_level.universe, [110, 140, 170])
sugar_level['high'] = fuzz.trimf(sugar_level.universe, [150, 180, 200])

temperature['low'] = fuzz.trimf(temperature.universe, [98, 98, 100])
temperature['normal'] = fuzz.trimf(temperature.universe, [98, 100, 102])
temperature['high_1'] = fuzz.trimf(temperature.universe, [100, 102, 104])
temperature['high_2'] = fuzz.trimf(temperature.universe, [102, 104, 106])
temperature['emergency'] = fuzz.trimf(temperature.universe, [104, 106, 106])

health_condition['low'] = fuzz.trimf(health_condition.universe, [0, 0, 0.5])
health_condition['normal'] = fuzz.trimf(health_condition.universe, [0, 0.5, 1])
health_condition['worst'] = fuzz.trimf(health_condition.universe, [0.5, 1, 1])

# fuzzy rules
#
rule1 = ctrl.Rule(
    antecedent=(
        (blood_pressure['low'] & temperature['low']) |
        (blood_pressure['normal'] & temperature['normal']) |
        (blood_pressure['high_BP_stage_1'] & temperature['high_1'])
    ),
    consequent=health_condition['low']
)

rule2 = ctrl.Rule(
    antecedent=(
        (age['young'] & sugar_level['normal']) |
        (age['middle age'] & sugar_level['elevated']) |
        (age['elder'] & sugar_level['high'])
    ),
    consequent=health_condition['normal']
)

rule3 = ctrl.Rule(
    antecedent=(
        (blood_pressure['high_BP_stage_2'] & temperature['high_2']) |
        (age['elder'] & sugar_level['high']) |
        (temperature['emergency'] & sugar_level['elevated'])
    ),
    consequent=health_condition['worst']
)

# Create a control system and add the rules
health_condition_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])


health_condition_simulation = ctrl.ControlSystemSimulation(health_condition_ctrl)
# Simulate the fuzzy inference system
blood_pressure_input = 140
temperature_input = 104
age_input = 70
sugar_level_input = 180

# Set input values
health_condition_simulation.input['blood_pressure'] = blood_pressure_input
health_condition_simulation.input['temperature'] = temperature_input
health_condition_simulation.input['age'] = age_input
health_condition_simulation.input['sugar_level'] = sugar_level_input

# Compute the output
health_condition_simulation.compute()

# Get the crisp output
output_value = health_condition_simulation.output['health_condition']

# Print the result
print(f"Health Condition: {output_value}")
blood_pressure.view()
plt.axvline(x=blood_pressure_input, color='k', linestyle='-')
temperature.view()
plt.axvline(x=temperature_input, color='k', linestyle='-')
age.view()
plt.axvline(x=age_input, color='k', linestyle='-')
sugar_level.view()
plt.axvline(x=sugar_level_input, color='k', linestyle='-')
health_condition.view()
plt.show()

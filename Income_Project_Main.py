from Income_Project_Dicts import fed_tax_dict as fed_tax
from Income_Project_Dicts import state_tax_dict as state_tax

#Functions
def marginal_f_income_taxes(income):
    left_to_tax = income
    fed_taxes = fed_tax['Single']
    left_to_tax = income
    amount_to_pay = 0
    for i in fed_taxes:
        if i[1] > left_to_tax:
            return amount_to_pay + (i[0] * left_to_tax)
        else:
            amount_to_pay += (i[0] * i[1])
            left_to_tax -= i[1]
def marginal_s_income_taxes(income, state):
    left_to_tax = income
    amount_to_pay = 0
    tax_range = state_tax[state]
    if tax_range == [[0, 0]]:
        return 0
    for i in tax_range:
        if i[1] > left_to_tax:
            return amount_to_pay + (i[0] * left_to_tax)
        else:
            amount_to_pay += (i[0] * i[1])
            left_to_tax -= i[1]
def effective_s_taxes(income, state):
    effective_tax_rate = marginal_s_income_taxes(income, state) / income
    return income * effective_tax_rate
def effective_f_taxes(income):
    effective_tax_rate = marginal_f_income_taxes(income) / income
    return income * effective_tax_rate
def bonus_amount(income, perc):
    try:
        return income * (perc / 100)
    except ValueError:
        return 0

def total_calc(income, perc, state):
    return income - effective_f_taxes(income) - effective_s_taxes(income, state) + bonus_amount(income, perc)
#----------------------------------------------------------------
#User Inputs
user_inputs = {}
base_income = 0
bonus_perc = 0
state_choice = ""

while "base_income" not in user_inputs.keys():
    base_income = input("Base Income? ")
    if base_income.isnumeric():
        user_inputs["base_income"] = int(base_income)
        base_income = user_inputs["base_income"]
    else:
        print("----You need an actual number dipshit----")

#Bonus Choice and Bonus Perc
while "bonus_perc" not in user_inputs.keys():
    bonus_choice = input("You got a bonus perc (y/n) ")
    if bonus_choice == "y":
        user_inputs["bonus_perc"] = int(input("Bonus Percentage? "))
        bonus_perc = user_inputs["bonus_perc"]
    elif bonus_choice == "n":
        user_inputs["bonus_perc"] = 0
        bonus_perc = user_inputs["bonus_perc"]
    else:
        print("----Not an option dipshit----")

while "state_choice" not in user_inputs.keys():
    state_choice = input("What state do you live in? (ex: CA) ")
    if state_choice in state_tax.keys():
        user_inputs["state_choice"] = state_choice
    else:
        print("----Figure out where you live you fool----")


print(total_calc(base_income, bonus_perc, state_choice))





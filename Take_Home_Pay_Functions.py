from Income_Project_Dicts import fed_tax_dict as fed_tax
from Income_Project_Dicts import state_tax_dict as state_tax

class Tax_Calcs:
    def __init__(self, income, state, perc):
        self.income = income
        self.state = state
        self.perc = perc
    def marginal_f_income_taxes(self):
        left_to_tax = self.income
        fed_taxes = fed_tax['Single']
        left_to_tax = self.income
        amount_to_pay = 0
        for i in fed_taxes:
            if i[1] > left_to_tax:
                return amount_to_pay + (i[0] * left_to_tax)
            else:
                amount_to_pay += (i[0] * i[1])
                left_to_tax -= i[1]
    def marginal_s_income_taxes(self):
        left_to_tax = self.income
        amount_to_pay = 0
        tax_range = state_tax[self.state]
        if tax_range == [[0, 0]]:
            return 0
        for i in tax_range:
            if i[1] > left_to_tax:
                return amount_to_pay + (i[0] * left_to_tax)
            else:
                amount_to_pay += (i[0] * i[1])
                left_to_tax -= i[1]
    def bonus_amount(self):
        try:
            return self.income * (self.perc / 100)
        except ValueError:
            return 0
    def total_ss_medic(self):
        return self.income * .0765
    def total_calc(self):
        return self.income - self.marginal_f_income_taxes() - self.marginal_s_income_taxes() - self.total_ss_medic()+ self.bonus_amount()

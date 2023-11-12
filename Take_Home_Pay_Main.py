from Income_Project_Dicts import state_tax_dict as state_tax
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from Take_Home_Pay_Functions import Tax_Calcs

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/take_home_pay_calculator")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})

@app.post("/take_home_pay_calculator")
def form_post(request: Request, base_income: int = Form(None), bonus_percentage: int = Form(None), state: str = Form(None)):
    #establish local empty variables
    error = ''
    gross = ""
    amount_received = ""
    state_tax_amount = ""
    federal_tax_amount = ""
    medicare_SS = ""
    bonus = ""
    if base_income is None:
        error = "ERROR: Not Valid Base Income"
    elif bonus_percentage is None:
        error = "ERROR: Not Valid Bonus Percentage"
    elif state not in state_tax.keys():
        error = "Please enter valid state & format? (ex: CA, WA, MA, etc.) "
    else:
        c1 = Tax_Calcs(base_income, state, bonus_percentage)
        state_tax_amount = round(c1.marginal_s_income_taxes(), 2)
        federal_tax_amount = round(c1.marginal_f_income_taxes(), 2)
        medicare_SS = round(c1.total_ss_medic(), 2)
        bonus = round(c1.bonus_amount(), 2)
        amount_received = round(c1.total_calc(), 2)
        gross = base_income
    return templates.TemplateResponse('form.html',
                                      context={'request': request,
                                               'Error': error,
                                               "Gross" : gross,
                                               "SIT": state_tax_amount,
                                               "FIT": federal_tax_amount,
                                               "SS": medicare_SS,
                                               "Bonus": bonus,
                                               "result": amount_received,})

#----------------------------------------------------------------------------------------------------------------------

'''

Run "uvicorn Take_Home_Pay_Project:app --reload" in terminal to load program

URL: http://localhost:8000/take_home_pay_calculator

'''


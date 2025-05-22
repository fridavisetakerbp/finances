import numpy as np
import matplotlib.pyplot as plt

yearly_salary_after_tax = 536000
monthly_salary = yearly_salary_after_tax/12
print(f"monthly_salary: {monthly_salary}")

highest_other_bid = 4300000
our_bid = 4470000
cash_out_now = 2000000
omkostninger = 132260
fellesgjeld = 379444
total_price = our_bid + fellesgjeld
predicted_selling_price = highest_other_bid
inskudd = cash_out_now - omkostninger
eierandel_hus = (inskudd/total_price)
mortgage = our_bid + omkostninger - inskudd
monthly_fixed_costs = 7081
predicted_profit = predicted_selling_price - mortgage - inskudd


#Print some initial conditions
print("-----------------------------WE BEGIN--------------------------------------")
print(f"Year: {2025}")
print(f"How rich are we? {inskudd + predicted_profit}, so that's {(inskudd + predicted_profit)/2} per person")
print(f"That is because we ourselves saved {inskudd/2} kr per person, and gained {predicted_profit/2} kr per person from investing in the house" )
print(f"Predicted selling price: {predicted_selling_price}")
print(f"Owned percentage of house: {eierandel_hus}")
print(f"Mortgage: {mortgage}")

#Settings rates
expected_price_growth = 0.02 
interest_rate = 0.056*(1-0.22)
total_costs = 0
taxation_reduction_interest = 0.22

#Yearly saving spending
yearly_spending = 700000

#First iteration - we do nothing
for year in range(5):

    print("-------------------------------------------------------------------")
    if mortgage> 0:
        interest = mortgage*interest_rate
    else:
        interest = 0
    yearly_costs = interest + monthly_fixed_costs*12
    total_costs = total_costs + interest + monthly_fixed_costs*12

    predicted_selling_price = (1+expected_price_growth)*predicted_selling_price
    predicted_profit = predicted_selling_price - mortgage - inskudd

    this_years_downpayment = (yearly_spending-interest)

    if this_years_downpayment > mortgage:
        this_years_downpayment = mortgage
    monthly_downpayment = this_years_downpayment/12
    monthly_interest = interest/12

    inskudd = inskudd + this_years_downpayment
    mortgage = mortgage - this_years_downpayment
    eierandel_hus = (inskudd/total_price)

    #Yearly summary
    print(f"Year: {2026+year}")
    print(f"How rich are we? {inskudd + predicted_profit}, so that's {(inskudd + predicted_profit)/2} per person")
    print(f"That is because we ourselves saved {inskudd/2} kr per person, and gained {predicted_profit/2} kr per person from investing in the house" )
    print(f"Predicted selling price: {predicted_selling_price}")
    print(f"Owned percentage of house: {eierandel_hus}")
    print(f"Mortgage: {mortgage}")
    print(f"Yearly costs (interest + common costs): {yearly_costs}")
    print(f"Monthly salary: {monthly_salary}")
    print(f"Monthly spending per person: {(monthly_interest+monthly_fixed_costs+monthly_downpayment)/2}")
    print(f"Monthly remaining personal budget: {monthly_salary - (monthly_interest+monthly_fixed_costs+monthly_downpayment)/2}")
    

#Summary parameters:
print("-------------------SUMMARY--------------------------")
print(f"Total costs: {total_costs}")
print(f"Predicted net profit upon selling house: {predicted_profit}")
print(f"Predicted brutto profit upon selling house: {predicted_profit-total_costs}")
print(f"How rich are we? {inskudd + predicted_profit}, so that's {(inskudd + predicted_profit)/2} per person")
print(f"That is because we ourselves saved {inskudd/2} kr per person, and gained {predicted_profit/2} kr per person from investing in the house" )


print("-------------------THAT'S ALL--------------------------")
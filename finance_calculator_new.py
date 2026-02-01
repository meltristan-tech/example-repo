import math
main_question = input("Do you want to calculate your investment interest or bond repayment( Choose Investment or Bond)?  ").lower()
if main_question == "investment":
    principal = int(input("What amount do you want to invest ?"))
    rate = int(input("What is the interest rate ? "))
    years = int(input("How many years do you want to invest your money ? "))
    interest_type = input("Do you want simple or compound interest ? ").lower()
    if interest_type == "simple":
        simple_amount = principal * (1 + (rate/100) * years)
        print("Your investment comes to R", simple_amount)
    elif interest_type == "compound":
        compound_amount = principal * math.pow((1 + (rate/100)), years)
        print("Your amount invested comes to R", compound_amount)
elif main_question == "bond":
    house_value = int(input("What is the value of the House ? "))
    interest_rate_annual = int(input("What is the interest rate on the bond ? "))
    months = int(input("Over how many months are you going to pay off the Bond ? "))
    interest_rate_monthly = (interest_rate_annual/100)/12
    loan_amount = (interest_rate_monthly * house_value)/(1 - (1 + interest_rate_monthly)**(-months))
    print("Your monthly bond repayment amount comes to R", loan_amount)
else:
    print("Wrong input")
    

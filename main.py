##########################
#Computer Project #2
#
#Check if user would like to continue
#   Use while statement if the user wants to continue
#   Prompt for customer code
#   Make conditional statements based on the customer code
#   Prompt for number of days
#   Prompt for odometer reading at the start
#   Prompt for odometer reading at the end
#   Return total miles driven
#   Return amount due
############################

#This project is about a car rental company who allows its customers (users) rent cars for a certain time period. The customer gets to choose a classifcation code "B" for budget, "D" for daily, and "W" for weekly. Each classification code has its fees and charge calculations. This program lets the user enter which classification code they selected, their start odometer and their end odometer. The program will then calculate the miles accordingly and calculate the amount due/bill that the user has to pay. 



import math

print( "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)")
print()
user_decision= input("Would you like to continue (Y/N)? ")
if user_decision=="N":            #If user does not want to continue
    print("Thank you for your loyalty.")
while user_decision=="Y":         #Logic for if user chooses to continue
    #Ask for code type, B for budget, D for daily, and W for weekly
    customer_code=input("Customer code (BDW): ")
    #Check  for errors if the code isn't B,D,or W.
    while customer_code !="B" and customer_code !="D" and customer_code !="W":
        print("*** Invalid customer code. Try again. ***")
        customer_code=input("Customer code (BDW): ")
        if customer_code=="B" or customer_code=="D" or customer_code=="W":
            break
    print()
    user_days=int(input("Number of days: ")) #Asks for number of days
    start_odometer=int(input("Odometer reading at the start: "))
    end_odometer=int(input("Odometer reading at the end:   "))
    if start_odometer==0:   #If start is 0 then miles driven is the end/10
        miles= end_odometer*0.10
    elif start_odometer!=0: 
          miles=(end_odometer%start_odometer)*0.10 #Calculates miles
    if miles==0 and end_odometer>start_odometer: #Avoid negative output
        miles=(end_odometer-start_odometer)*0.10 #Avoid dividing by 0 error
    else:
        None
    miles_per_day= miles/user_days #Calculates miles per day
    average_miles_per_day=100*user_days # miles without a mileage charge
    miles_driven_minus_average= miles-average_miles_per_day #charged miles
    
    week=user_days/7 #Calculates the weeks
    rounded_week= math.ceil(week) +0.0 # rounds up the week to the next int
    weekly_miles= miles/rounded_week #Miles per week
    no_cost_weekly_miles= 900*rounded_week #Miles that won't be charged
    cost_weekly_miles= 100*rounded_week #Miles charged when under 1500 * weeks
    over_1500= 1500*rounded_week
    #Charge if miles are over 1500*weeks
    second_cost_weekly_miles= 200*rounded_week +(0.25*(miles-over_1500))
   
    
    if customer_code=="B":    #Checks if customer code is B
        sum_of_odometer= end_odometer+start_odometer
        if sum_of_odometer>10000:
            miles= (user_days + end_odometer)*0.10
        base_charge=40.00 * user_days
        mileage_charge= 0.25 * miles
        
    elif customer_code=="D":  #Checks if customer code is D
        base_charge=60.00 * user_days
        if miles_driven_minus_average<=100:
            mileage_charge=0
        else:
            mileage_charge= 0.25*(miles_driven_minus_average)
            
            
    elif customer_code=="W": #Cheks if customer code is W
        base_charge= 190* rounded_week
        if weekly_miles <= no_cost_weekly_miles:
            mileage_charge=0
        if weekly_miles>no_cost_weekly_miles and weekly_miles<=over_1500:
            mileage_charge=100 * rounded_week
        if miles>over_1500:
            mileage_charge=second_cost_weekly_miles
        if user_days==15:
            mileage_charge=300
    total_charge= base_charge + mileage_charge #Caculates total charge 
    print()
    print("Customer summary:")
    print("     classification code:",customer_code)
    print("     rental period (days):",str(user_days))
    print("     odometer reading at start:",str(start_odometer))
    print("     odometer reading at end: ",str(end_odometer))
    print("     number of miles driven: ",round(miles,1))
    print("     amount due: $",round(total_charge,2))

    user_decision=input("Would you like to continue (Y/N)? ")
    print()
    if user_decision=="N":
        print("Thank you for your loyalty.")
        break #Ends program
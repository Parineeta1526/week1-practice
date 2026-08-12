def calculate_salary(basic_salary,bonus_percentage=5):
    bonus=(basic_salary*bonus_percentage)/100
    final_salary=basic_salary+bonus
    return bonus,final_salary
employee_name=input("Enter employee name:")
basic_salary=int(input("Enter basic salary:"))

special_bonus=input("Does the employee have a special bonus percentage?")
if special_bonus=="yes":
        bonus_percentage=int(input("Enter bonus percentage:"))
        bonus_amount,final_salary=calculate_salary(basic_salary,bonus_percentage)
else:
    bonus_percentage=5
    bonus_amount,final_salary=calculate_salary(basic_salary)
    print(f"Employee name: {employee_name}")
    print(f"Basic Salary: {basic_salary}")
    print(f"Bonus Percentage: {bonus_percentage}")
    print(f"Bonus Amount: {bonus_amount}")
    print(f"Final Salary: {final_salary}")   

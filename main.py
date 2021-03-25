
class Budget:
    def __init__(self):
        self.expenses = []
        self.Income = []
        self.money_in_bank = []
    def income(self):
        self.user_income = int(input("enter the your $$Income: "))
        self.Income.append(self.user_income)
        self.Total = sum(self.Income)
        print(f"Your Income is ${self.Total}")
        print("")

    def rent(self):
        self.rent = int(input("enter the money you spent for rent :"))
        self.expenses.append(self.rent)
        print("")

    def expense_of_food(self):
        self.FoodExpense = int(input("enter the Amount that you spent for food: "))
        self.expenses.append(self.FoodExpense)
        print("")

    def expense_of_entertainment(self):
        self.entertainment = int(input("enter the amount you spent for entertainment: "))
        self.expenses.append(self.entertainment)
        print("")

    def expense_for_clothing(self):
        self.clothing = int(input("enter the amount you spent for clothes: "))
        self.expenses.append(self.clothing)
        self.expense_total = sum(self.expenses)
        print(f"Your Total expense is ${self.expense_total}")
        print("")

    def tax(self):
        self.taxmoney = self.Total / 100 * 40
        print(f"The tax for you is ${self.taxmoney}")
        print("")

    def savings(self):
        self.Totalexpense = self.expense_total + self.taxmoney
        self.saved_money = self.Total - self.Totalexpense
        print(f"The money saved by you is ${self.saved_money}")
        print("")

    def adding_bank(self):
        self.question = input("Do you want to put your savings in your bank?,yes-Y or no-N: ").upper()
        print("")
        if self.question == "Y":
            self.money_in_bank.append(self.saved_money)
            print("$",sum(self.money_in_bank), "is deposited in bank account.Thank you!")
        elif self.question == "N":
            print("Thank you!")
        else:
            print("wrong input,sorry!")

Money = Budget()
Money.income()
Money.rent()
Money.expense_of_food()
Money.expense_of_entertainment()
Money.expense_for_clothing()
Money.tax()
Money.savings()
Money.adding_bank()

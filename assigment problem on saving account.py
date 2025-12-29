 # create bank account class with 2 attibutes balance and account no. create method. for deposit, with draw and print the balance and create another class called saving account and create a method called and inseret and print the final balance by using the inneritance concept?
  class Account:
      def __init_(self,balance,accno):
          self.balance =balance
          self.acco =accno
          def debit(self,amount):
              if self.balance >amount:
                  self.balance_=amount:
                  print(f"{Amount}is debited,bal is{self.gettingbal()}")
              else:
                  print("insufficient funcs")
          def credit (self,amount):
                    self.balance+=amount
                  print(*f"{amount}is credited,bal is {self.getbal()}")
          def getbal (self):
                  return self.balance 
class Saving Account(Account):
          def __init_(self,interest):
                self.inseret=inseret=interest
                Super().__init_(1000,"acc12")
          def inserest rate(self):
                inserest 1=self.balance*(self.inserest/100)
                self.balance+=interest 1000print(self.getbal())
                print(self.getbal())
                    
                    
          acc1=Savings Account(5)
          acc1.credit(500)
          acc1.interestrate()
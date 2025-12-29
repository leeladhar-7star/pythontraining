 # create account class with 2 attributes balance and account no created method for debit, credit and print in no the balance.
  def __init_(self,balance,accno):
          self.balance =balance
          self.acco =accno
          def debit(self,amount):
              if self.balance >amount:
                  self.balance_=amount:
                  print(f"{amount}is debited,bal is{self.gettingbal()}")
              else:
                  print("insufficient funcs")
          def credit (self,amount):
                    self.balance+=amount
                  print(*f"{amount}is credited,bal is {self.getbal()}")
          def getbal (self):
                  return self.balance 
        acc1=Account(1000,"acc123")
        acc1.credit(500)
        acc1.debit(100)
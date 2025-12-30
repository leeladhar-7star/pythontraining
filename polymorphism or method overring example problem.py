class MethodOverriding:
    def display(self):
        print("method invoked frombase class")
class MethodOverride2(MethodOverriding):
     def display(self):
         print("method invoked from derivedclass")
ob=MethodOverride2()
ob.display()
                
            
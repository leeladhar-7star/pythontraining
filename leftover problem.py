#you are given two string A and B . your task is to find and return a string repersenting the a leftover string in A after removing all the letter that exist in string B .return "Empty"if the outputs does not contain any value?
def leftover(a,b):
    left=""
    remove =set(b)
    for ch in  a:
       if ch not in remove:
          left +=ch
       if left:
         print(left)
    else:
            print("empty")
a="bde"
b="bde"
leftover(a,b)
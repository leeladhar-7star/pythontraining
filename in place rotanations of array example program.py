''' x=[1,2,3,4,5]
l=0
r=len(x)-1
while l<r:
 x[1],x[r]=x[r],x[1]
 l+=1 
 r-=1 
 print(x)'''
def movezeroes(nums):
     x=[]
     y=[]
     for i in range (len(nums)):
        if nums[i]==0:
          x.append(nums[i])
        else:
          y.append(nums[i])
        z=y+x
        print(z)
nums=[0,1,0,3,12]
movezeroes(nums)
                 
def maxSum(arr,l,m,h) :
    sm = 0; left_sum = -10000
    for i in range(m,l-1,-1) :
         sm = sm + arr[i]
    if(sm>left_sum) :
        left_sum = sm
    sm = 0; right_sum = -1000
    for i in range(m+1,h+1) :
        sm = sm + arr[i]
    if(sm>right_sum) :
     right_sum = sm
    return left_sum+right_sum;
def maxSubArraySum(arr,l,h) :
    if(l == h) :
     return arr[l]
    m = (l+h)//2
    return max(maxSubArraySum(arr,l,m),
     maxSubArraySum(arr,m+1,h),
     maxSum(arr,l,m,h))
Filename=input()
file = open(Filename)
arr=[]
for x in file:
      arr.appened(int(x))
m=maxSubArraySum(arr,0,Len(arr)-1)
print("Maximum sub sequence sum is ",m)
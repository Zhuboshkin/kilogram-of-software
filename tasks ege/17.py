# def f(x):
#     if len(str(x))==5 and abs(x)%100==43:
#         return 1
#     else:
#         return 0
# arr=[int(x) for x in open('1.txt')]
# cnt=0
# ma=0
# marr=max([x for x in arr if f(x)==1])
# for i in range(2,len(arr)):
#     if (f(arr[i-2]) +f(arr[i-1]) +f(arr[i]))>0:
#         if arr[i-2]**2+arr[i-1]**2+arr[i]**2<marr**2:
#             cnt+=1
#             ma=max(ma,arr[i-2]**2+arr[i-1]**2+arr[i]**2)
# print(cnt,ma)


cnt=0
m=0
arr=[int(x) for x in open('1.txt')]
arrot=sum([x for x in arr if x<0])
for i in range(2,len(arr)):
    if max(arr[i-2],arr[i-1],arr[i])*min(arr[i-2],arr[i-1],arr[i])>arrot:
        cnt+=1
        m=max(((arr[i-2]+arr[i-1]+arr[i])),m)
print(cnt,abs(m))
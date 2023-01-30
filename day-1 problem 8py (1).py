def findGuest(guests,N):
   count=0
   for i in range(N):
      if guests[i]<=count:
         count +=1
   return count
N=2
guests=[1,0,2,1,3]
totalGuests=findGuest(guests,N)
print(totalGuests)

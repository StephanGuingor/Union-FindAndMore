#lazy approach
#quicker method, 
#find takes atmost lgN
#union constant time given roots,
#union and find have lgN time

class QuickUnionW:
  def __init__(self,N):
    self.__setUp(N)

  def __setUp(self,N):
    #i => index , i => max val in root
    self.arr = [[i,i] for i in range(N)]
    self.sizeA = [1 for i in range(N)]

  def __getRoot(self,x):
    while (x != self.arr[x][0]):
      self.arr[x][0] = self.arr[self.arr[x][0]][0]
      x = self.arr[x][0]
        
    return self.arr[x][0],self.arr[x][1]
    
  def union(self,p,q):
    pr = self.__getRoot(self.arr[p][0])[0]
    #flat tree
    qr = self.__getRoot(self.arr[q][0])[0]
    
    if pr == qr:
      return 
    if self.sizeA[qr] > self.sizeA[pr]:
      self.arr[pr][0] = qr

      #checks an adds +
      max = self.isMore(self.arr[qr][1],self.arr[pr][1])
      self.arr[qr][1] = max

      self.sizeA[qr] += self.sizeA[pr]

    else:
      self.arr[qr][0] = pr

      #checks an adds +
      max = self.isMore(self.arr[qr][1],self.arr[pr][1])
      self.arr[pr][1] = max
     
      self.sizeA[pr] += self.sizeA[qr]

    
  def isMore(self,q,p):
    if q > p:
      return q
    else:
      return p
      
  def find(self,x):
    # _,max = self.__getRoot(x)
    return self.__getRoot(self.arr[x][0])[1]

  def connected(self,p,q):
    pr = self.__getRoot(self.arr[p][0])[0]
    qr = self.__getRoot(self.arr[q][0])[0]
    return pr == qr



weight = QuickUnionW(10)
weight.union(1,2)
weight.union(3,4)
weight.union(5,6)
weight.union(3,6)
weight.union(1,4)
weight.union(1,9)

print(weight.connected(1,3))
print(weight.connected(1,6))


print(weight.find(6))



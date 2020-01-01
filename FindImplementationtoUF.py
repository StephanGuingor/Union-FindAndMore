
class QuickUnionW:
  
  def __init__(self,N):
    self.__setUp(N)

   #Creates the needed arrays
  def __setUp(self,N):
    #i => index , i => max val in root
    self.arr = [[i,i] for i in range(N)]
    self.sizeA = [1 for i in range(N)]

    #By traversing the tree, return root
  def __getRoot(self,x):
    while (x != self.arr[x][0]):
      #The line below help flatten the tree (sets parent point to the parent grandfather)
      self.arr[x][0] = self.arr[self.arr[x][0]][0]
      x = self.arr[x][0]
        
    return self.arr[x][0],self.arr[x][1]
    
   #connects different nodes or trees based on how many items they contain. (Smaller will connect to larger tree) 
  def union(self,p,q):
    pr = self.__getRoot(self.arr[p][0])[0]
    
    qr = self.__getRoot(self.arr[q][0])[0]
    
    if pr == qr:
      return 
    if self.sizeA[qr] > self.sizeA[pr]:
      self.arr[pr][0] = qr

      #check who has the biggest item, and replace the max value of the bigger tree root.
      max = self.isMore(self.arr[qr][1],self.arr[pr][1])
      self.arr[qr][1] = max

      self.sizeA[qr] += self.sizeA[pr]

    else:
      self.arr[qr][0] = pr

      #checks an adds +
      max = self.isMore(self.arr[qr][1],self.arr[pr][1])
      self.arr[pr][1] = max
     
      self.sizeA[pr] += self.sizeA[qr]

   #Assitant function
  def isMore(self,q,p):
    if q > p:
      return q
    else:
      return p
      
     #Checks the root of the tree in wich x is contained and return the max value that it contains.
  def find(self,x):
    # _,max = self.__getRoot(x)
    return self.__getRoot(self.arr[x][0])[1] #*

  def connected(self,p,q):
    pr = self.__getRoot(self.arr[p][0])[0]
    qr = self.__getRoot(self.arr[q][0])[0]
    return pr == qr

# *Note: each array index contains a max value (1 position) and it only takes into consideration himself and its children.
# For this reason we check the root max value.







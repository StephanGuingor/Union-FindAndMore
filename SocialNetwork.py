
class Node:
    #Enables ==
  def __eq__(self, other):
    if isinstance(other, Node):
        return self.name == other.name
    return False

  def __init__(self,name):
    print(f"New node initialized: {name}")
    self.name = name
    self.next = self
    self.rootVal = 1
    

class Network:

  def __init__(self):
    self.__rootDate = None
    self.__head = None #Track of root
    self.__dict = {}

  def union(self,val1,val2,timeStamp):

    #Checks is they are the same item
    if val1 == val2:
      return 
      
    #Check if existence, else create
    if not self.__checkRegister(val1):
      self.__dict.update({val1:Node(val1)})

    if not self.__checkRegister(val2):
      self.__dict.update({val2:Node(val2)})

    #Changes to Node
    val1 = self.__dict[val1]
    val2 = self.__dict[val2]
    #Log dict
    print(list(self.__dict))

    #Check Roots 
    v1r = self.__getRoot(val1)
    print(f"{val1.name} root is: {v1r.name} and has a rv of: {v1r.rootVal}")
    v2r = self.__getRoot(val2)
    print(f"{val2.name} root is: {v2r.name} and has a rv of: {v2r.rootVal}")

    #Check if joined
    if v1r == v2r and (v1r != None  and v2r != None):
      print("vl1 and vl2 are same")
      return

    #Checks for smaller tree
    if v1r.rootVal < v2r.rootVal:
      v1r.next = v2r
      self.head = v2r
      v2r.rootVal += v1r.rootVal
    else: #vl2 < vl1 or vl1 == vl2
      v2r.next = v1r
      self.head = v1r
      v1r.rootVal += v2r.rootVal

    #Might Set Time Stamp of Friendship
    self.__setTimeStamp(timeStamp)

  def __checkRegister(self,val):
    #Returns true if already exists
    
    return self.__dict.get(val) != None
    
  def __setTimeStamp(self,timeStamp):

    if self.__rootDate:
      #Checks if date is more recent 
      if self.__rootDate < timeStamp:
        self.__rootDate = timeStamp
    else:
        self.__rootDate = timeStamp
     

  def __getRoot(self,x):
    while (x.next != x):
      #Flat tree (path compression)
      x.next = x.next.next 
      x = x.next
    return x

  def getEarliestTime(self):
    if self.head.rootVal == len(list(self.__dict)):
        print("All nodes connected!")
    print(f"The earliest time is: {self.__rootDate}")
    return self.__rootDate
  
  def connected(self,p,q):
    pn = self.__dict[p]
    qn = self.__dict[q]
    print(f"Heaad items: {self.head.rootVal} vs {len(list(self.__dict))}")
    print(f"{p} and {q} are connected: {(self.__getRoot(pn) == self.__getRoot(qn))}")
    return self.__getRoot(pn) == self.__getRoot(qn)

myNetwork = Network()

myNetwork.union("Martin","Mike",1)
myNetwork.union("Martin","Fred",2)
myNetwork.union("Martin","Felipe",2)
myNetwork.union("Ale","Chemi",4)
myNetwork.union("Ale","Sam",5)
myNetwork.union("Ale","Felipe",2)


myNetwork.connected("Ale","Martin")

myNetwork.getEarliestTime()


print("Done")
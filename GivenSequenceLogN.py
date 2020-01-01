class Node:
    def __init__(self,x):
        self.value = x
        self.next = None
    
class GivSequence:
   
    def __init__(self,sequence):
        self.previous = None
        
        self.nodePointers = []
        self.__mergeSort(sequence)

        self.sequence = sequence
        # self.__linkNodes(sequence)
        # self.printLink()

        #recieves items, and sorts them into sequenceay. In logN.Checks half then half. Etc
        #initializes two lists, link to next big or equal, normal list and linked list,both ways
        
    def printLink(self):
        ini = self.nodePointers[0]
        while ini:
            print(ini.value)
            ini = ini.next

    def linkTheNodeForMerge(self,sequence,k):
        if self.previous != None:
            tmp = Node(sequence[k])
            self.previous.next =  tmp
            self.nodePointers.append(tmp)
            self.previous = tmp
        else:
            tmp = Node(sequence[k])
            self.previous = tmp
            self.nodePointers.append(tmp)

    def __mergeSort(self,sequence,main = True): 
        if len(sequence) > 1: 
            mid = len(sequence)//2 #Finding the mid of the sequenceay 
            L = sequence[:mid] # Dividing the sequenceay elements  
            R = sequence[mid:] # into 2 halves 
    
            self.__mergeSort(L,False) # Sorting the first half 
            self.__mergeSort(R,False) # Sorting the second half 
    
            i = j = k = 0
            
            
            # Copy data to temp sequenceays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    # print(sequence)
                    sequence[k] = L[i]

                    if main:
                        self.linkTheNodeForMerge(sequence,k)
                    
                    i+=1
                else: 
                    sequence[k] = R[j] 
                      
                    if main:
                        self.linkTheNodeForMerge(sequence,k)

                    j+=1
                k+=1
            
            # Checking if any element was left 
            while i < len(L): 
                sequence[k] = L[i]

                if main:
                    self.linkTheNodeForMerge(sequence,k)

                i+=1
                k+=1
            
            while j < len(R): 
                sequence[k] = R[j] 

                if main:
                    self.linkTheNodeForMerge(sequence,k)

                j+=1
                k+=1

    def __retrieveIndex(self,x,sequence):
        return sequence.index(x) if x in sequence else None
        

    def remove(self,x):
        #searches value in list in log N time, as the constructor, if it finds it then
        #changes root pointer to 0
        #previous pointer is set to next (linked list)

        idx = self.__retrieveIndex(x,self.sequence)
        
        if idx == None:
            print(f"{x} does not exist")
            return

        if idx == 0:
            self.nodePointers[idx].next = None
            self.sequence.pop(idx)
            self.nodePointers.pop(idx)

        elif idx < len(self.sequence) - 1:
            prevNode = self.nodePointers[idx - 1]
            prevNode.next = self.nodePointers[idx + 1]
            self.sequence.pop(idx)
            self.nodePointers.pop(idx)
        else:
            prevNode = self.nodePointers[idx - 1]
            prevNode.next = None
            self.sequence.pop(idx)
            self.nodePointers.pop(idx)

    def sucessor(self,x):
        #if not removed
        #recieve index,
        #check position in linked list a next, if there some.
        idx = self.__retrieveIndex(x,self.sequence)

        if idx != None:
            if idx == len(self.sequence) - 1:
                print(f"{x} has no sucessor")
                return None
            else:
                return self.nodePointers[idx].next.value
        print(f"{x} does exist")
        

a = [1,4,3,3,43,6]

b = GivSequence(a)

# b.printLink()
b.remove(2)
b.remove(4)
b.remove(90)
b.remove(6)
b.remove(3) #I could go even further and return an iterator.
b.printLink()

print(b.sucessor(3))
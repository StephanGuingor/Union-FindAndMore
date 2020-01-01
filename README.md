# Union-FindAndMore
This repository contains some examples of Union - Find algorithms,  with modifications in relationship to the typical one. And even some applications based on problems given by a Princeton University course.

## Find Implementation to UF:
###### Prompt:

###### <sub>"Union-find with specific canonical element. Add a method 𝚏𝚒𝚗𝚍() to the union-find data type so that 𝚏𝚒𝚗𝚍(𝚒) returns the largest element in the connected component containing ii. The operations, 𝚞𝚗𝚒𝚘𝚗(), 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍(), and 𝚏𝚒𝚗𝚍() should all take logarithmic time or better.

###### <sub>For example, if one of the connected components is \{1, 2, 6, 9\}, then the 𝚏𝚒𝚗𝚍() method should return 99 for each of the four elements in the connected components."

---
**Description:**

The *constructor* will recieve a value in order to generate a list from 0 to N - 1.

E.g:
```swift
QU = QuickUnionW(5)
```
It will generate (a tree):
    
Roots:&nbsp;&nbsp; 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
Indexes: 0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4
    
---

The ***union*** method will connect two values that are in the list. This way we can start creating our tree.

E.g:
```swift
QU.union(0,1)
```
Roots:&nbsp;&nbsp; 0&nbsp;  2&nbsp; 3&nbsp; 4
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;  | &nbsp; | &nbsp; | &nbsp; |
Indexes: 1&nbsp;  2&nbsp; 3&nbsp; 4

*Note: The root of a root is always itself. (in this case 0 has a root of 0)

Each Index contains the max value of the items they contain, so here is a more accurate description of the data:

E.g:
        Root|Max element in connected component (tree)
        
Roots and Max element:&nbsp;&nbsp; 0[1]&nbsp;  2[2]&nbsp; 3[3]&nbsp; 4[4]
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; |
Indexes: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1[1] &nbsp; &nbsp; 2 &nbsp; &nbsp; 3 &nbsp; &nbsp; &nbsp; 4


---

The ***find*** method returns the largest element in the connected component where x is.
The method will traverse the tree, and return the max element tht the root has.

E.g:

```swift
QU.find(0) //returns one
QU.find(1) //return one
QU.find(2) //return two
```
---

The *connected* method will return if two values are connected (are in the same tree)
The method will compare the roots of the given values, returning true if they share tree, otherwise false

E.g:

```swift
QU.connected(0,1) //returns true
QU.find(1,2) //return false
```

## Network

###### Prompt:
###### <sub>"Social network connectivity. Given a social network containing *n* members and a log file containing *m* timestamps at which times pairs of members formed friendships, design an algorithm to determine the earliest time at which all members are connected (i.e., every member is a friend of a friend of a friend ... of a friend). Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should be *mlogn* or better and use extra space proportional to *n*."

---
**Description:**

The main difference between the Network class and Union-Find typical class, is that in the Network class uses linked nodes instead of lists.

---
The *constructor* wont take parameters.

E.g:
```swift
NET = Network()
```

---

The *union* method will take two names and a time stamp (time when the became friends) *

```swift
NET.union("Alessandro","Chemi",13) //time stamp set up to 24h
NET.union("Mike","Chemi",15)
```

<sub>*Note: you can modify the class to fit the time stamp format as you need.

---

The *connected* method just as the typical Union-Find class, it will return wether A and B are connected or not.

Quick and simple example on how the network work:

Alessandro *is friends with* Chemi
Mike *is friends with* Chemi

Therefore Ale has a common friend with Mike (Chemi), so they are connected. (The function checks if a "path" exists)

E.g:

```swift
NET.connected("Alessandro", "Chemi") //returns true
NET.connected("Mike","Alessandro") //returns true

//Making a new connection
NET.union("Regina","Fred",2)

//Check connection
NET.connected("Alessandro","Regina") //returns false (they are in different "newtworks")
```

---

The *getEarliestTime* method will return the earliest hour in wich everyone connected.

E.g:

```swift
NET.getEarliestTime() // this will return None and print "Not everyone is connected"

//Connecting everone
NET.union("Regina","Alessandro",16)

//Checking again
NET.getEarliestTime() //returns 16 and prints "Everyone is connected"
```
# Given Sequence*

###### Prompt:

###### <sub>"Successor with delete. Given a set of *n* integers S = \{ 0, 1, ... , n-1 \}S={0,1,...,n−1} and a sequence of requests of the following form:

###### <sub>- Remove xx from SS
###### <sub>- Find the successor of *x*: the smallest *y* in S such that *y≥x*.

###### <sub>design a data type so that all operations (except construction) take logarithmic time or better in the worst case."

<sub>*Note: It's not a Union - Find implementation.

---

The *constructor* takes a sequence (doesn't have to be in order):

E.g:

```swift
a = [3,5,2,5,1,8]
GS = GivSequence(a)
````

After recieving the sequence, the constructor will sort the sequence using the *mergeSort* algorithm and at the same time will create an ordered *linked list*.

---

The *printLink* method will print the sequence in order.

```swift
GS.printLink() // outputs 1 2 3 5 5 8
```

---

The *remove* method will remove a value while maintaining it's structure.

```swift
GS.remove(3)
GS.printLink() // outputs 1 2 5 5 8
```

---

The *succesor* method will return the next value in relation to x that is equal or bigger.

```swift
GS.remove(3)
GS.printLink() // outputs 1 2 5 5 8
```
---

*<sub>Note: I could of just used list instead of the linked lists, but first of all I wanted to practice my manipulation of nodes and it does have a benefit. If you wanted translate this code to another language and had to use arrays, you could. That's because all of the management happends in the linked list, wich size is not fixed.

<sub>Although the space complexity grows a little bit becuase of new allocated memory but time complexity stays pretty much the same.

---

**Thank you,**

**Any suggestion would be greatly appreciated!**

**If you have questions feel free to ask!**

<sub>**-StephanGF**

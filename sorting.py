#bubble sort 
#o(n2) 
"""it has the capability to do something most sorting algorithms cannot. In particular, if during a pass
there are no exchanges, then we know that the list must be sorted. A bubble sort can be modified to stop
early if it finds that the list has become sorted. This means that for lists that require just a few passes,
a bubble sort may have an advantage in that it will recognize the sorted list and stop"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

#Selection Sort
#O(n2)
""" As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass,
the next largest is in place.One note about shifting versus exchanging is also important. In general, a shift operation
requires approximately a third of the processing work of an exchange since only one assignment is performed. In benchmark
studies, insertion sort will show very good performance. """

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

#Insertion Sort
#O(n2)
""". It always maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted”
back into the previous sublist such that the sorted sublist is one item larger"""
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)



#Shell Sort
#between O(n) and O(n2) 
"""improves on the insertion sort by breaking the original list into a number of smaller sublists. the shell sort
uses an increment i, sometimes called the gap, to create a sublist by choosing all items that are i items apart.  
It turns out, however, that this final insertion sort does not need to do very many comparisons (or shifts) since 
the list has been pre-sorted by earlier incremental insertion sorts, as described above. In other words, each pass
produces a list that is “more sorted” than the previous one. This makes the final pass very efficient."""

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

#Merge Sort
#Recall that the slicing operator is O(k) where k is the size of the slice. In order to guarantee that mergeSort will be O(nlogn)
"""Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list. """
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

def mergeSortRec(alist, start, end):


#Quick Sort
#okish senarios n log n worst O(n2)
"""The role of the pivot value is to assist with splitting the list. The actual position where the pivot
value belongs in the final sorted list, commonly called the split point, will be used to divide the list 
for subsequent calls to the quick sort.
Partitioning begins by locating two position markers—let’s call them leftmark and rightmark—at the 
beginning and end of the remaining items in the list. The goal of the 
partition process is to move items that are on the wrong side with respect to the pivot value while also 
converging on the split point 
we can attempt to alleviate some of the potential for an uneven division by using a technique called median 
of three. To choose the pivot value, we will consider the first, the middle, and the last element in the list."""

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
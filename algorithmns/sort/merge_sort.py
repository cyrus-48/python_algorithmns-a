import random
 
 #--------------------------[ Merge Sort ]--------------------------#
'''
     --------------------[concepts used]--------------------
        1. Divide and Conquer - > this is the idea of breaking a problem into smaller subproblems, solving the subproblems, and combining them to get the desired solution.
        2. Recursion - > this is the idea of a function calling itself.
        3. Merge - > this is the idea of combining two  or more sorted arrays into one sorted array.
        --------------------------------------------------------
        
        --------------------[Time Complexity]--------------------
        Worst Case: O(nlogn) ->  it takes O(n) time to merge two sorted arrays of size n/2 each and O(n) time to merge two sorted arrays of size n/4 each and so on.
        Therefore, the time complexity is O(nlogn).
        
        Best Case: O(nlogn) -> 
        Average Case: O(nlogn)
        
        --------------------------------------------------------
        
        --------------------[The algorithmn]--------------------
        
        
        
        
    
    
    '''
import random
def merge_sort(nlist): 
    print("Splitting  : ",nlist)
    if len(nlist) > 1:
        mid = len(nlist)//2 # get the middle of the list
        left = nlist[:mid]  # get the left half of the list
        right = nlist[mid:] # the right half of the list
        
        merge_sort(left) # sort the left half
        merge_sort(right) # sort the right half
        
        i=j=k =0
        
        while i <  len(left) and j < len(right):
            if left[i] < right[j]:
                nlist[k] = left[i]
                print("sorting : " , nlist)
                i +=1
            else:
                nlist[k] = right[j]
                print("Sorting : " , nlist)
                j +=1
            k +=1
            
        while i < len(left):
            nlist[k] = left[i]
            i=i+1;
            k = k +1
            
        while j < len(right):
            nlist[k] = right[j]
            j=j+1
            k = k +1
    print("Merging  : " , nlist)   
nlist = [ random.randint(0 , 100) for x in range(20)]
merge_sort(nlist)
print(nlist)
        
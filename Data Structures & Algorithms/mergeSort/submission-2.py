# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]: 
        if not pairs:
            return []
        return self.listsplit(pairs,0,len(pairs)-1)

    def listsplit(self,pairs,s,e):
        if s >= e:
            return pairs
            
        mid = (s+e)//2

        self.listsplit(pairs,s,mid)
        self.listsplit(pairs,mid+1,e)

        self.merge(pairs,s,mid,e)

        return pairs
        
    def merge(self,arr,s,m,e):

        l = arr[s:m+1]
        r = arr[m+1:e+1]

        i = 0
        j = 0
        k = s

        while i < len(l) and j < len(r):
            if l[i].key <= r[j].key:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
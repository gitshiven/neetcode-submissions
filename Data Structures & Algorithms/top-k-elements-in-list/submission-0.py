class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums: 
            hashmap[i] = 1+ hashmap.get(i,0)  
            
        sorted_answer = sorted(hashmap, key=hashmap.get, reverse=True) [:k]  
        return list(sorted_answer)
        
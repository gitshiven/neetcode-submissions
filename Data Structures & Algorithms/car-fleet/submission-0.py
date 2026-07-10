#O(nlogn)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack =[]
        pair = []      #pair aise bhi bana sakte the pair = [[p,s] for p,s in zip(position,speed)]
        for i in range(len(position)):
            pair.append([position[i], speed[i]])   #pair karne ka tareeka, zip bhi use kar sakte hai but vo easy hai

        for p,s in sorted(pair, reverse = True): #reverse sorted order. -> aise bhi sahi hai -> for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>1 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)

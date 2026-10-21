class Solution:
    def isValid(self, s: str) -> bool:
        # heap where you keep pushing until you see a closing bracket
        # then you pop off the heap and if the pairs match, yay, 
        # if not, return false
        heap = []
        closing = "}])"
        if len(s) % 2 != 0:
            return False
        for i in s:
            if not i in closing:
                heap.append(i)
            else:
                if heap == []:
                    return False
                elif i == ")" and heap[-1] and heap[-1] == "(":
                    heap.pop(-1)
                elif i == "}" and heap[-1] and heap[-1] == "{":
                    heap.pop(-1)
                elif i == "]" and heap[-1] and heap[-1] == "[":
                    heap.pop(-1)
                else:
                    return False
        if heap == []:
            return True
        else:
            return False
        
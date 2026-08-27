class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            new = []
            new.append([strs[0]])
            return new
        ## make each str into a dictionary of index + sorted string
        ## if 2 sorted str have same key, append into same array
        ## then replace each key:item pair with the str from og list

        new_strs = {}
        for i in range(len(strs)):
            listi = list(strs[i])
            listi.sort()
            i_string = "".join(listi)
            if i_string in new_strs:
                new_strs[i_string].append(i)
            else:
                new_strs[i_string] = [i]
        
        final_str = []
        for i in new_strs:
            new = []
            for j in new_strs[i]:
                new.append(strs[j])
            final_str.append(new)
        return final_str     

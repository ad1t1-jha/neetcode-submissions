class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## create a list of most common numbers in order
        ## maybe a dictionary and sort by # of #s
        ## then iteratre on the new list k times

        nums_dict = {}
        for i in range(len(nums)):

            if nums[i] in nums_dict:

                nums_dict[nums[i]]+= 1
            else:
                nums_dict[nums[i]] = 1
        
        ## now we should have smth like {(1:1), (2:2), (3:3)]}

        sorted_x = sorted(nums_dict.items(), key=lambda kv: kv[1], reverse = True)

        result = [t[0] for t in sorted_x]
        final_arr = []
        for i in range(k):
            final_arr.append(result[i])
        
        return final_arr

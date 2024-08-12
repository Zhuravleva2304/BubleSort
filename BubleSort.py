class BubleSort:
    def sort(self,nums:list[int])->list[int]:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums 
obj=BubleSort() 
print(obj.sort([8,15,2,7,4]))                  

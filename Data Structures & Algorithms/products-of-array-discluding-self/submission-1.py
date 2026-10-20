class Solution:
    def get_product(self, nums: List[int]) -> int:
        total_product = 1
        for num in nums:
            total_product *= num
        return total_product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_indexes = [i for i, num in enumerate(nums) if num == 0]
        zero_occurences = len(zero_indexes)
        total_items = len(nums)
        if zero_occurences > 1:
            return [0] * total_items
        
        if zero_occurences == 1:
            zero_index = zero_indexes[0]
            nums.pop(zero_index)
            total_product = self.get_product(nums)
            products_arr = [0] * total_items
            products_arr[zero_index] = total_product
            return products_arr
        
        total_product = self.get_product(nums)
        products_arr = []
        for num in nums:
            products_arr.append(total_product // num)
        return products_arr
        
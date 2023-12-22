class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        pre = 1
        post = 1

        for i in range(n):
            # Multiplying prefix that we have so far
            answer[i] *= pre
            pre *= nums[i]

            # Multiplying postfix that we have so far
            answer[n - i - 1] *= post
            post *= nums[n - i - 1]

        return answer


print(Solution().productExceptSelf([1, 2, 3, 4]))

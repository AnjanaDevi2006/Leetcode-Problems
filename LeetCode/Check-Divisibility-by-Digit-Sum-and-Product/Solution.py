class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        digit_sum = 0
        digit_pro = 1

        while n:
            digit = n % 10
            digit_sum += digit
            digit_pro *= digit
            n //= 10

        total = digit_sum + digit_pro

        return original % total == 0
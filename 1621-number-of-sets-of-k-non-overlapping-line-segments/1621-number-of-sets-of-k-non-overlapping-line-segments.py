
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 1_000_000_007

        total = n + k - 1
        choose = 2 * k

        fact = [1] * (total + 1)
        inv_fact = [1] * (total + 1)

        for i in range(1, total + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[total] = pow(fact[total], MOD - 2, MOD)

        for i in range(total, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        return (
            fact[total]
            * inv_fact[choose] % MOD
            * inv_fact[total - choose] % MOD
        )
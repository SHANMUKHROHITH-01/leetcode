class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def backtrack(remain, combo, start):
            if remain == 0:
                # Found a valid combination
                results.append(list(combo))
                return
            elif remain < 0:
                # Exceeded the target, stop this branch
                return

            for i in range(start, len(candidates)):
                # Add the number to the current combination
                combo.append(candidates[i])
                # Give the current number another chance (start remains i)
                backtrack(remain - candidates[i], combo, i)
                # Backtrack: remove the number before the next iteration
                combo.pop()

        backtrack(target, [], 0)
        return results
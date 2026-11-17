class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        # Convert each inner list to a set (dedupes + enables O(1) lookup).
        # Then unpack with * so set.intersection receives N separate arguments
        # instead of one list: set.intersection(set1, set2, set3, ...)
        common = set.intersection(*[set(arr) for arr in nums])

        # Sort only once, at the end — intersecting throws away order,
        # so sorting mid-way would be wasted work.
        return sorted(common)


if __name__ == "__main__":
    s = Solution()
    print(s.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))  # [3, 4]
    print(s.intersection([[1, 2, 3], [4, 5, 6]]))                        # []
    print(s.intersection([[1]]))                                         # [1]
class Solution:
    def search_matrix(self, matrix, target):

        # Edge case
        if not matrix:
            return False

        r, c = len(matrix), len(matrix[0])

        left, right = 0, r - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] < target:
                left = mid + 1

            else:
                right = mid - 1

        if right < 0:
            return False

        row = matrix[right]
        left, right = 0, c - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
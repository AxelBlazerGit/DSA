class Solution:
	def isWordExist(self, mat, word):
		#Code here
		def dfs(x, y, idx):
            if idx == len(word):
                return True
            if not (0 <= x < n and 0 <= y < m) or (x, y) in hash or mat[x][y] != word[idx]:
                return False

            hash.add((x, y))
            for dx, dy in move:
                if dfs(x + dx, y + dy, idx + 1):
                    return True
            hash.remove((x, y))

            return False

        n, m = len(mat), len(mat[0])
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for x in range(n):
            for y in range(m):
                if mat[x][y] == word[0]:
                    hash = set()
                    if dfs(x, y, 0):
                        return True

        return False

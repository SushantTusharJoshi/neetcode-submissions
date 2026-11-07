class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:                          # build the letter tree
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        ROWS, COLS = len(board), len(board[0])
        path, res = set(), []

        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                    (r, c) in path or board[r][c] not in node.children):
                return
            nxt = node.children[board[r][c]]     # step down the tree
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None                  # add each word once
            path.add((r, c))                     # choose
            dfs(r + 1, c, nxt)                   # go deeper
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)
            path.remove((r, c))                  # undo

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return res
def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if len(board) <= 0:
        return
    
    def printBoard():
        for row in board:
            print(row)
    
    n_rows = len(board)
    n_cols = len(board[0])
    
    def search(r, c):
        # mark cell as visited
        board[r][c] = 'V'
        # up
        if r > 0:
            if board[r - 1][c] == 'O':
                search(r - 1, c)
        # down
        if r < n_rows - 1:
            if board[r + 1][c] == 'O':
                search(r + 1, c)
        # right
        if c < n_cols - 1:
            if board[r][c + 1] == 'O':
                search(r, c + 1)
        # left
        if c > 0:
            if board[r][c - 1] == 'O':
                search(r, c - 1)
        # if you can't go anywhere else, just return
        return
    
    # start searching from any 'O's on the outside
    for c in range(n_cols):
        # first row: r = 0
        if board[0][c] == 'O':
            search(0, c)
            printBoard()
        if board[n_rows - 1][c] == 'O':
            search(n_rows - 1, c)
            printBoard()
    for r in range(1, n_rows - 1):
        # first column: c = 0
        if board[r][0] == 'O':
            search(r, 0)
        # last column: c = n_cols - 1
        if board[r][n_cols - 1] == 'O':
            search(r, n_cols - 1)
    
    # now that all of the edge islands are marked, we can transform
    # any internal remaining 'O's to 'X's and any changed 'V's
    # back to 'O's
    for r in range(n_rows):
        for c in range(n_cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'V':
                board[r][c] = 'O'
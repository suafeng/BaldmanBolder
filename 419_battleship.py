# X..X
# ...X
# ...X

# count the number of battleship!
# The idea is to count the number of X that having no X above or left, this is
# the beginning of the battleship, just count this.

def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i - 1 < 0 or board[i-1][j] != 'X':
                        if j - 1 < 0 or board[i][j-1] != 'X':
                            count += 1
        return count

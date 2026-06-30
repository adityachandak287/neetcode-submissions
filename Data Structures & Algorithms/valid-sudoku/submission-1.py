class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_len = len(board)
        import math
        grid_size = int(math.sqrt(board_len))
        grids = [0] * board_len
        rows = [0] * board_len
        cols = [0] * board_len

        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                grid_idx = (row_idx//grid_size) * grid_size + (col_idx//grid_size)

                cell_val = (int(cell) - 1) if cell != "." else -1
                if cell_val == -1:
                    continue

                if not (grids[grid_idx] & (1<<cell_val)):
                    grids[grid_idx] |= 1<<cell_val
                else:
                    return False
                if not (rows[row_idx] & (1<<cell_val)):
                    rows[row_idx] |= 1<<cell_val
                else:
                    return False
                if not (cols[col_idx] & (1<<cell_val)):
                    cols[col_idx] |= 1<<cell_val
                else:
                    return False

        return True

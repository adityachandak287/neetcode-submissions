class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_len = len(board)
        import math
        grid_size = int(math.sqrt(board_len))
        grids = [[0] * board_len for _ in range(board_len)]
        rows = [[0] * board_len for _ in range(board_len)]
        cols = [[0] * board_len for _ in range(board_len)]

        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                grid_idx = (row_idx//grid_size) * grid_size + (col_idx//grid_size)

                cell_val = (int(cell) - 1) if cell != "." else -1
                if cell_val == -1:
                    continue

                grids[grid_idx][cell_val] += 1
                if grids[grid_idx][cell_val] > 1:
                    return False

                rows[row_idx][cell_val] += 1
                if rows[row_idx][cell_val] > 1:
                    return False

                cols[col_idx][cell_val] += 1
                if cols[col_idx][cell_val] > 1:
                    return False

        return True

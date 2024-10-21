import sudoku as s
import numpy as np

class SudokuHumain(s.Sudoku):

    def __init__(self, taille: int = 9) -> None:
        super().__init__(taille)
        solutionsParCase = np.zeros((self.taille, self.taille))

    def resoudreSudoku(self) -> bool:
        pass
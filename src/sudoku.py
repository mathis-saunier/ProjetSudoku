from abc import ABC, abstractmethod
import numpy as np

class Sudoku:
    taille = 9
    grille = np.zeros((taille, taille), dtype=int)

    def __init__(self) -> None:
        pass

    def caseEstVide(self, l: int, c: int) -> bool:
        pass
    
    def fixerChiffre(self, chiffre: int, l: int, c: int):
        pass

    def effacerChiffre(self, l: int, c: int):
        pass

    def obtenirChiffre(self, l: int, c: int) -> int:
        pass

    def estChiffreValable(self, chiffre: int, l: int, c: int) -> bool:
        pass

    def obtenirChiffresValables(self, l: int, c: int) -> list[int]:
        pass

    def obtenirLigne(self, l: int) -> list[int]:
        pass

    def obtenirColonne(self, c: int) -> list[int]:
        pass

    def obtenirCarre(self, l: int, c: int) -> list[int]:
        pass

    def verifierLigne(self, l: int) -> bool:
        pass

    def verifierColonne(self, c: int) -> bool:
        pass

    def verifierCarre(self, l: int, c: int) -> bool:
        pass

    def verifierSudoku(self) -> bool:
        pass

    def afficherSudoku(self):
        pass
    
    @abstractmethod
    def resoudreSudoku(self) -> bool:
        pass
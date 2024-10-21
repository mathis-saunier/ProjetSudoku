from abc import ABC, abstractmethod
import numpy as np
import sys

class Sudoku:

    def __init__(self, taille: int = 9) -> None:
        taille = taille
        grille = np.zeros((taille, taille), dtype=int)
        pass

    def remplirSudokuDepuisTxt(self, fichier: str) -> None:
        pass

    def caseEstVide(self, l: int, c: int) -> bool:
        pass
    
    def fixerChiffre(self, chiffre: int, l: int, c: int) -> None:
        pass

    def effacerChiffre(self, l: int, c: int) -> None:
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

    def afficherSudoku(self) -> None:
        pass
    
    @abstractmethod
    def resoudreSudoku(self) -> bool:
        # sys.argv pour obtenir le -v quand on fait "python3 main.py -v"
        pass
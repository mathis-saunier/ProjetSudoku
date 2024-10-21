from abc import ABC, abstractmethod
import numpy as np
import sys

class Sudoku:

    def __init__(self) -> None:
        self.taille = 9
        self.grille = np.zeros((9, 9), dtype=int)

    def remplirSudokuDepuisTxt(self, fichier: str) -> None:
        pass

    def caseEstVide(self, l: int, c: int) -> bool:
        return self.obtenirChiffre(l, c) == 0
    
    def fixerChiffre(self, chiffre: int, l: int, c: int) -> None:
        assert 1 <= chiffre <= self.taille, "La valeur doit être entre 1 et 9."
        self.grille[l, c] = chiffre

    def effacerChiffre(self, l: int, c: int) -> None:
        self.grille[l, c] = 0

    def obtenirChiffre(self, l: int, c: int) -> int:
        return self.grille[l, c]

    def obtenirLigne(self, l: int) -> list[int]:
        return np.copy(self.grille[l, :])

    def obtenirColonne(self, c: int) -> list[int]:
        return np.copy(self.grille[:, c])

    def obtenirCarre(self, l: int, c: int) -> list[int]:
        return np.copy(self.grille[l//3*3:l//3*3+3, c//3*3:c//3*3+3]).flatten()

    def verifierAbsenceChiffresEnDouble(self, liste: list[int]) -> bool:
        chiffres, occurences = np.unique(liste, return_counts=True)
        chiffresEnDouble = chiffres[occurences > 1]
        return (len(chiffresEnDouble) == 0) or (len(chiffresEnDouble) == 1 and chiffresEnDouble[0] == 0)

    def verifierLigne(self, l: int) -> bool:
        ligne = self.obtenirLigne(l)
        return self.verifierAbsenceChiffresEnDouble(ligne)

    def verifierColonne(self, c: int) -> bool:
        colonne = self.obtenirColonne(c)
        return self.verifierAbsenceChiffresEnDouble(colonne)

    def verifierCarre(self, l: int, c: int) -> bool:
        carre = self.obtenirCarre(l, c)
        return self.verifierAbsenceChiffresEnDouble(carre)

    def estChiffreValable(self, chiffre: int, l: int, c: int) -> bool:
        chiffresPresents = self.obtenirLigne(l) + self.obtenirColonne(c) + self.obtenirCarre(l, c)
        return chiffre not in chiffresPresents

    def obtenirChiffresValables(self, l: int, c: int) -> list[int]:
        chiffresPossibles = [1,2,3,4,5,6,7,8,9]
        chiffresPresents = self.obtenirLigne(l) + self.obtenirColonne(c) + self.obtenirCarre(l, c)
        return [c for c in chiffresPossibles if c not in chiffresPresents]

    def verifierSudoku(self) -> bool:
        sudokuCorrect = True
        for i in range(self.taille):
            sudokuCorrect = sudokuCorrect and self.verifierLigne(i) and self.verifierColonne(i)
        if not sudokuCorrect:
            return False
        else:
            for i in range(0, self.taille, 3):
                for j in range(0, self.taille, 3):
                    sudokuCorrect = sudokuCorrect and self.verifierCarre(i, j)
            return sudokuCorrect

    def afficherSudoku(self) -> None:
        pass
    
    @abstractmethod
    def resoudreSudoku(self) -> bool:
        # sys.argv pour obtenir le -v quand on fait "python3 main.py -v"
        pass
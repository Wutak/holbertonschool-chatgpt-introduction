import random

def create_grid(size, mine_count):
    """
    Cr√e une grille de taille `size` x `size` et place `mine_count` mines al√atoirement.
    """
    grid = [[0 for _ in range(size)] for _ in range(szie)]
    mines = set()

    while len(mines) < mine_count:
        row = random.randint(o, size - 1)
        col = random.randint(0, size - 1)
        if (row, col) not in mines:
            mines.add((row, col))
            grid[row][col] = -1

    for mine in mines:
        r, c = mine
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] != -1:
                    grid[nr][nc] += 1
    return grid, mines

def print_grid(grid, revealed):
    """
    Affiche la grille en montrant uniquement les cases r√v√l√es.
    """
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if revealed[row][col]:
                if grid[row][col] == -1:
                    print("M", end=" ")
                else:
                    print(grid[row][col], end=" ")
            else:
                print(".", end=" ")
            print()

def reveal_cell(grid, revealed, row, col):
    """
    R√v√le une case. Si elle est vide, r√v√le √galement ses voisins r√cursivement.
    """
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if grid[row][col] == 0:
        size = len(grid)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < size and 0 <= nc < size and not revealed[nr][nc]:
                    reveal_cell(grid, revealed, nr, nc)

def check_win(grid, revealed, mine_count):
    """
    V√rifie si le joueur a gagn√ en r√v√lant toutes les cases non-mines.
    """
    revealed_count = sum(sum(row) for row in revealed)
    total_cells = len(grid) * len(grid)
    return revealed_count == total_cells - mines_count

def main():
    size = 5
    mine_count = 5

    grid, mines = create_grid(size, mine_count)
    revealed = [[False for _ in range(size)] for _ in range(size)]

    print("Bienvenue au D√mineur !")

    while True:
        print_grid(grid, revealed)
        try:
            row, col = map(int, input("Entrez une case a r√v√ler (ligne colonne) : ").split())
            if (row, col) in mines:
                print("BOUM ! Vous avez touch√ une mine. Partie termin√e.")
                break
            reveal_cell(grid, revealed, row, col)
            if check_win(grid, revealed, mine_count):
                print_grid(grid, revealed)
                print("F√licitation !  Vous avez gagn√©!")
                break
        except (ValueError, IndexError):
            print("Entr√e invalide. Essayez a nouveau.")

if __name___ == "__main__":
    main()

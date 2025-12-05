#Выполняеться 4789=2+1+1+1=5
import chess
import os
def print_custom_board(board):
    print("\n   A B C D E F G H\n")
    rows = str(board).split("\n")
    for i, row in enumerate(rows):
        print(f" {8 - i} {row} {8 - i}")
    print("\n   A B C D E F G H\n")
def main():
    board = chess.Board()
    while not board.is_game_over():
        os.system('cls')
        print_custom_board(board)
        turn = "Белых" if board.turn == chess.WHITE else "Черных"
        print("Пример хода: d2d4 | Команда отката: undo, undo 3, undo full")
        move_str = input(f"Ход {turn}: ").strip()
        # ---------- ОБРАБОТКА КОМАНДЫ ОТКАТА ----------
        if move_str.startswith("undo"):
            parts = move_str.split()
            # Полный откат
            if len(parts) == 2 and parts[1] == "full":
                while board.move_stack:
                    board.pop()
                continue
            # Откат N ходов
            if len(parts) == 2 and parts[1].isdigit():
                n = int(parts[1])
                for _ in range(min(n, len(board.move_stack))):
                    board.pop()
                continue
            # Откат 1 хода
            if len(parts) == 1:
                if board.move_stack:
                    board.pop()
                continue
            print("Некорректная команда отката.")
            input("Нажмите Enter...")
            continue
        # ------------------------------------------------
        try:
            move = board.parse_san(move_str)
            if move in board.legal_moves:
                board.push(move)
            else:
                print("Этот ход невозможен!")
                input("Enter...")
        except ValueError:
            print("Неверный формат хода! Пример: e2e4, Nf3")
            input("Enter...")
    # --- Игра окончена ---
    os.system('cls')
    print_custom_board(board)
    print("\nИгра окончена!")
    result = board.result()
    print("Белые победили!" if result == "1-0" else
          "Черные победили!" if result == "0-1" else
          "Ничья!")
if __name__ == "__main__":
    main()
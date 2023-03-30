# функция для рисования поля
def draw_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

# функция для проверки если победитель
def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            return True
    if board[0] == board[4] == board[8] and board[0] != "-":
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        return True
    return False

# функция для игры
def game():
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    player = "X"
    while True:
        draw_board(board)
        print(f"Ход: {player}")
        position = int(input("Выберите позицию на поле (1-9): "))
        if position < 1 or position > 9:
            print("Недопустимая позиция. Пожалуйста, выберите от 1 до 9")
            continue
        if board[position-1] != "-":
            print("Эта позиция уже занята. Пожалуйста, выберите другую")
            continue
        board[position-1] = player
        if check_winner(board):
            draw_board(board)
            print(f"Победитель: {player}!")
            break
        if all([pos != "-" for pos in board]):
            draw_board(board)
            print("Ничья!")
            break
        player = "X" if player == "O" else "O"

game()
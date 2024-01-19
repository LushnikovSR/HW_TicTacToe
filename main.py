import random


class TicTacToe:
    def __init__(self, size: int, player_sign: chr, robot_sign: chr):
        self.board = [[" _ " for col in range(size)] for row in range(size)]
        self.player = str(" " + player_sign + " ")
        self.robot = str(" " + robot_sign + " ")
        self.first = self.first_step()
        self.step_count = 0

    def first_step(self) -> bool:
        rand = random.randint(0, 1)
        return bool(rand)

    def move(self):
        if self.first:
            print("Player:")
            self.player_step()
            if not self.check_winner() and self.step_count < (len(self.board) ** 2 // 2):
                print("Robot:")
                self.robot_step()
        else:
            print("Robot:")
            self.robot_step()
            if not self.check_winner() and self.step_count < (len(self.board) ** 2 // 2):
                print("Player:")
                self.player_step()

    def player_step(self):
        row = int(input("Выбрать строку: "))
        col = int(input("Выбрать столбец: "))
        if self.board[row][col] != " _ ":
            self.player_step()
        else:
            self.board[row][col] = self.player
            for i in range(len(game.board)):
                print(game.board[i])
        #     добавить задержку времени

    def robot_step(self):
        rand_row = random.randrange(0, 3)
        rand_col = random.randrange(0, 3)
        if self.board[rand_row][rand_col] != " _ ":
            self.robot_step()
        else:
            self.board[rand_row][rand_col] = self.robot
            for i in range(len(game.board)):
                print(game.board[i])

    def check_winner(self) -> bool:
        return self.check_player() or self.check_robot()

    def check_player(self) -> bool:
        return self.check_rows(self.player) or self.check_columns(self.player) or self.check_diagonals(self.player)

    def check_robot(self) -> bool:
        return self.check_rows(self.robot) or self.check_columns(self.robot) or self.check_diagonals(self.robot)

    def check_rows(self, side) -> bool:
        row_res = set()
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                row_res.add(self.board[i][j])
            if len(row_res) == 1 and side in row_res:
                return True
            row_res = set()
        return False

    def check_columns(self, side) -> bool:
        col_res = set()
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                col_res.add(self.board[j][i])
            if len(col_res) == 1 and side in col_res:
                return True
            col_res = set()
        return False

    def check_diagonals(self, side) -> bool:
        res_1 = set()
        for el in range(len(self.board)):
            res_1.add(self.board[el][el])
        if len(res_1) == 1 and side in res_1:
            return True

        res_2 = set()
        for j in range(len(self.board)):
            res_2.add(self.board[j][len(self.board) - 1 - j])
        if len(res_2) == 1 and side in res_2:
            return True

        return False

    def final_message(self):
        if self.check_player():
            return "Player Wins!!!"
        elif self.check_robot():
            return "Game Over -> :`/"
        else:
            return "DRAW"


if __name__ == '__main__':
    game = TicTacToe(3, "X", "0")
    game.first_step()
    STEP_AMOUNT = (len(game.board) ** 2 // 2) + 1
    for i in range(STEP_AMOUNT):
        game.move()
        game.step_count += 1
        if game.check_winner():
            break
    print(game.final_message())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

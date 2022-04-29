import time
import random


def print_timer(text):
    print(text)
    time.sleep(1)


class Player_chose:

    choices = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.human_move = self.choices
        self.computer_move = random.choice(self.choices)

    def validate_input(self):
        while True:
            self.user_choice = input("rock, paper, scissors? >")
            if self.user_choice in self.human_move:
                return self.user_choice
            else:
                print_timer("That is wrong  input")

    def learn(self, human_move, computer_move):
        self.human_move = human_move
        self.computer_move = computer_move


class human_Player(Player_chose):

    def choose(self):
        return self.validate_input()

    def learn(self, human_move, computer_move):
        pass


class computer_player(Player_chose):

    def choose(self):
        return self.computer_move

    def learn(self, human_move, computer_move):
        self.computer_move = computer_move


class Cycle_computerInput(Player_chose):

    def choose(self):
        if self.human_move == self.choices[0]:
            return self.choices[1]
        elif self.human_move == self.choices[1]:
            return self.choices[2]
        else:
            return self.choices[0]

    def learn(self, human_move, computer_move):
        self.human_move = human_move


class Reflect_computerInput(Player_chose):

    def choose(self):
        if self.computer_move is None:
            return random.choice(self.choices)
        else:
            self.human_move = self.computer_move
        return self.computer_move

    def learn(self, human_move, computer_move):
        self.computer_move = computer_move


class Run():

    print_timer("Welcome to the Amazing  Game!")

    def __init__(self, user, computer_input):
        self.user = user
        self.computer_input = computer_input
        self.count1 = 0
        self.count2 = 0

    def compare_choices(self, user_c, computer_c):
        if ((user_c == 'rock' and computer_c == 'scissors') or
           (user_c == 'scissors' and computer_c == 'paper') or
           (user_c == 'paper' and computer_c == 'rock')):
            return user_c
        elif user_c == computer_c:
            return "Tied"
        else:
            return computer_c

    def round_number(self):
        while True:
            try:
                self.rounds = int(input("How many rounds do  "
                                        "you want play? > "))
            except ValueError:
                print_timer("Not an integer! Try again.")
                continue
            else:
                return self.rounds
                break

    def more_play(self):
        while True:
            morerounds = input("Do you want more rounds?\n"
                               "yes or no \n").lower()
            if "yes" in morerounds:
                self.Game()
            else:
                print_timer("Game Over \n")

    def play(self):
        user_c = self.user.choose()
        computer_c = self.computer_input.choose()
        self.user.learn(user_c, computer_c)
        self.computer_input.learn(computer_c, user_c,)
        self.winner = self.compare_choices(user_c, computer_c)
        if self.winner == user_c:
            self.count1 += 1
        elif self.winner == "Tied":
            self.count1 = self.count1
            self.count2 = self.count2
        else:
            self.count2 += 1
        print_timer(f" You played : {user_c}\n"
                    f" Opponent played:{computer_c}\n"
                    f" Your  scores is: {self.count1}\n"
                    f" Computer  scores is: {self.count2}\n")

    def Game(self):
        self.round_number()
        round = 1
        while round <= self.rounds:
            print_timer(f" you have play {round}"
                        f" out of {self.rounds}\n")
            round += 1
            self.play()
        if self.count1 > self.count2:
            print_timer(f"You won!\n")
        elif self.count1 < self.count2:
            print_timer(f" computer won \n")
        else:
            print_timer(f"You tied!\n")
        print_timer(f"Your scores {self.count1} and"
                    f"computer {self.count2}\n")
        self.more_play()


if __name__ == '__main__':
    user = human_Player()
    Stragies = [
                Cycle_computerInput(),
                Reflect_computerInput(),
                computer_player()
               ]
    computer_input = random.choice(Stragies)
    game = Run(user, computer_input)
    game.Game()

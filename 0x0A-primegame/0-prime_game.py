#!/usr/bin/python3
"""
Module simulates a game betwenen Maria and Ben
"""


def isWinner(x, nums):
    """
    Args:
        x = number of rounds
        nums = array of n
        len(nums) == x

    Return: Name of Winner
    """

    if x < 1:
        return None
    
    winners = []

    def is_prime(number):
        """helper function to identify prime numbers"""
        if number <= 1:
            return False
        if number > 1 < 4:
            return True
        for x in range(4, number - 1):
            if number % x == 0:
                return False
        return True

    def play_game(n):
        """simulate game play"""
        num_list = list(range(1, n + 1))
        maria_turn = True
        game_over = False

        while len(num_list) > 1 or game_over is False:
            first_prime = None
            for x in num_list:
                if is_prime(x):
                    first_prime = x
                    break

            if first_prime is None:
                game_over = True
                break

            num_list = [y for y in num_list if y % first_prime != 0]
            maria_turn = not maria_turn

        if maria_turn:
            return "Ben"
        else:
            return "Maria"

    for n in nums:
        winner = play_game(n)
        winners.append(winner)

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

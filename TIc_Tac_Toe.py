#!/bin/python3

import math
import os
import random
import re
import sys

def nextMove(player, board):
    opponent = 'O' if player == 'X' else 'X'

    # Function to check if a player can win with the next move
    def can_win(b, p):
        for i in range(3):
            # Check rows and columns
            if b[i][0] == b[i][1] == p and b[i][2] == '_':
                return (i, 2)
            if b[i][0] == b[i][2] == p and b[i][1] == '_':
                return (i, 1)
            if b[i][1] == b[i][2] == p and b[i][0] == '_':
                return (i, 0)
            if b[0][i] == b[1][i] == p and b[2][i] == '_':
                return (2, i)
            if b[0][i] == b[2][i] == p and b[1][i] == '_':
                return (1, i)
            if b[1][i] == b[2][i] == p and b[0][i] == '_':
                return (0, i)

        # Check diagonals
        if b[0][0] == b[1][1] == p and b[2][2] == '_':
            return (2, 2)
        if b[0][0] == b[2][2] == p and b[1][1] == '_':
            return (1, 1)
        if b[1][1] == b[2][2] == p and b[0][0] == '_':
            return (0, 0)
        if b[0][2] == b[1][1] == p and b[2][0] == '_':
            return (2, 0)
        if b[0][2] == b[2][0] == p and b[1][1] == '_':
            return (1, 1)
        if b[1][1] == b[2][0] == p and b[0][2] == '_':
            return (0, 2)

        return None

    # Check if player can win
    move = can_win(board, player)
    if move:
        print(f"{move[0]} {move[1]}")
        return

    # Check if opponent can win and block them
    move = can_win(board, opponent)
    if move:
        print(f"{move[0]} {move[1]}")
        return

    # Otherwise, choose the first empty cell (fallback move)
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                print(f"{r} {c}")
                return

if __name__ == '__main__':
    player = input().strip()
    board = []
    for _ in range(3):
        board.append(input().strip())

    nextMove(player, board)

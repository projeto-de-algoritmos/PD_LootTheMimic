import random
import math
import logging

import pygame

class Knapsack:
    def __init__(self, window):
        self.window = window
        self.items = []

    def solve_dynamic_programming(self, items, max_w):
        # Solve the knapsack problem using dynamic programming
        # Returns the maximum value that can be put in a knapsack of capacity max_w
        # and prints the items that make up this solution
        n = len(items)
        table = [[0 for x in range(max_w + 1)] for x in range(n + 1)]

        for i in range(n + 1):
            for w in range(max_w + 1):
                if i == 0 or w == 0:
                    table[i][w] = 0
                elif items[i - 1]['weight'] <= w:
                    table[i][w] = max(
                        items[i - 1]['value'] + table[i - 1][w - items[i - 1]['weight']],
                        table[i - 1][w],
                    )
                else:
                    table[i][w] = table[i - 1][w]

        return table[n][max_w], self.get_items(table, items, max_w)
    
    def get_items(self, table, items, max_w):
        # Get the items that make up the solution to the knapsack problem
        solution = []
        n = len(items)
        w = max_w
        for i in range(n, 0, -1):
            if table[i][w] != table[i - 1][w]:
                solution.append(items[i - 1])
                w -= items[i - 1]['weight']
        return solution
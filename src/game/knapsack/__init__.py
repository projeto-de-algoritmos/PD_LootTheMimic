import random
import math
import logging

import pygame

class Knapsack:
    def __init__(self, window, difficulty):
        self.window = window
        self.difficulty = difficulty
        self.items = []

    def knapsack(items, max_weight):
        n = len(items)
        dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            weight, value = items[i - 1]['weight'], items[i - 1]['value']
            for w in range(1, max_weight + 1):
                if weight > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

        max_value = dp[n][max_weight]
        current_weight = max_weight
        combination = []
        for i in range(n, 0, -1):
            if max_value <= 0:
                break
            if max_value != dp[i - 1][current_weight]:
                item = items[i - 1]
                combination.append(item)
                max_value -= item['value']
                current_weight -= item['weight']

        return max_value, combination
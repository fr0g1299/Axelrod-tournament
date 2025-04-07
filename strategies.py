"""
Strategies for the Axelrod tournament.

Each strategy is a function that takes two parameters: the list of moves made by the player
and the list of moves made by the opponent. The function should return the player's move.
"""

import random
ROUNDS = 200

def always_cooperate(_self_history, _opponent_history):
    """Always cooperate"""
    return 'C'

def always_betray(_self_history, _opponent_history):
    """Always betray"""
    return 'B'

def random_choice(_self_history, _opponent_history):
    """Make a random choice"""
    return random.choice(['C', 'B'])

def tit_for_tat(_self_history, opponent_history):
    """Tit for Tat: cooperate on the first move, then mirror the opponent's move"""
    return 'C' if not opponent_history else opponent_history[-1]

def tit_for_tat_last_betray(self_history, opponent_history, rounds=ROUNDS):
    """Tit for Tat, but betray on the last move"""
    if len(self_history) == rounds - 1:
        return 'B'
    return 'C' if not opponent_history else opponent_history[-1]

def reverse_tit_for_tat(_self_history, opponent_history):
    """Reverse Tit for Tat: betray on the first move, then mirror the opponent's move"""
    return 'B' if not opponent_history else opponent_history[-1]

def tit_for_tat_modified(self_history, opponent_history, rounds=ROUNDS):
    """Modified Tit for Tat: betray on the last three moves and if the opponent has defected 5 times"""
    if len(self_history) in {ROUNDS - 1, ROUNDS - 2, ROUNDS - 3}:
        return 'B'
    opponent_defections = opponent_history.count('B')
    if opponent_defections >= 5:
        return 'B'
    return 'C' if not opponent_history else opponent_history[-1]

def tit_for_two_tats(_self_history, opponent_history):
    """Tit for Two Tats: betray if the opponent has defected twice in a row"""
    if len(opponent_history) < 2:
        return 'C'
    if opponent_history[-1] == 'B' and opponent_history[-2] == 'B':
        return 'B'
    return 'C'

def tit_for_two_tats_modified(self_history, opponent_history, rounds=ROUNDS):
    """Tit for Two Tats: betray if the opponent has defected twice in a row and on the last 3 rounds"""
    if len(self_history) in {ROUNDS - 1, ROUNDS - 2, ROUNDS - 3}:
        return 'B'
    if len(opponent_history) < 2:
        return 'C'
    if opponent_history[-1] == 'B' and opponent_history[-2] == 'B':
        return 'B'
    return 'C'

def periodic_ddc(self_history, _opponent_history):
    """Periodic DDC: defect on the first and second move, then cooperate"""
    pattern = ['B', 'B', 'C']
    return pattern[len(self_history) % len(pattern)]

def periodic_ccd(self_history, _opponent_history):
    """Periodic CCD: cooperate on the first and second move, then defect"""
    pattern = ['C', 'C', 'B']
    return pattern[len(self_history) % len(pattern)]

def grudger(_self_history, opponent_history):
    """Grudger: cooperate until betrayed, then always defect"""
    return 'B' if 'B' in opponent_history else 'C'

def grudger_forgiving(_self_history, opponent_history):
    """Grudger Forgiving: cooperate until betrayed 2 times, then always defect"""
    if opponent_history.count('B') > 1:
        return 'B'
    return 'C'

def grudger_more_forgiving(_self_history, opponent_history):
    """Grudger More Forgiving: cooperate until betrayed 4 times, then always defect"""
    if opponent_history.count('B') > 3:
        return 'B'
    return 'C'

def forgiving_tit_for_tat(_self_history, opponent_history):
    """Forgiving Tit for Tat: similar to Tit for Tat, but forgives after 3 rounds"""
    if not opponent_history:
        return 'C'
    if opponent_history[-1] == 'B':
        return 'B' if opponent_history[-3:] != ['C', 'C', 'C'] else 'C'
    return 'C'

def naive_prober(self_history, opponent_history):
    """Naive Prober: Tit for Tat but randomly defects with small probability"""
    if not opponent_history:
        return 'C'
    if random.random() < 0.1:
        return 'B'
    return opponent_history[-1]


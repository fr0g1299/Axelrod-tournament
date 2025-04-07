from strategies import *
import argparse

# Payoff matrix: (Player1_move, Player2_move) -> (P1 reward, P2 reward)
payoff_matrix = {
    ('C', 'C'): (3, 3),
    ('B', 'B'): (1, 1),
    ('B', 'C'): (5, 0),
    ('C', 'B'): (0, 5)
}

# Strategy dictionary mapping strategy names to their corresponding functions
strategies = {
    'Always Cooperate': always_cooperate,
    'Always Betray': always_betray,
    'Random': random_choice,
    'Tit for Tat': tit_for_tat,
    'Tit for Tat Modified': tit_for_tat_modified,
    'Tit for Tat Last Betray': tit_for_tat_last_betray,
    'Reverse Tit for Tat': reverse_tit_for_tat,
    'Tit for Two Tats': tit_for_two_tats,
    'Periodic DDC': periodic_ddc,
    'Periodic CCD': periodic_ccd,
    'Grudger': grudger,
    'Grudger Forgiving': grudger_forgiving,
    'Grudger More Forgiving': grudger_more_forgiving,
    'Forgiving Tit for Tat': forgiving_tit_for_tat,
    'Naive Prober': naive_prober,
    'Tit for Two Tats Modified': tit_for_two_tats_modified
}

def play_match(strategy1, strategy2, rounds):
    """
    Simulate a match between two strategies over a specified number of rounds.

    Args:
        strategy1 (function): The first strategy function.
        strategy2 (function): The second strategy function.
        rounds (int): The number of rounds to simulate.

    Returns:
        tuple: The scores for each strategy after all rounds.
    """
    history1 = []
    history2 = []
    score1 = 0
    score2 = 0

    # Simulate each round of the match
    for _ in range(rounds):
        move1 = strategy1(history1, history2)
        move2 = strategy2(history2, history1)
        history1.append(move1)
        history2.append(move2)
        reward1, reward2 = payoff_matrix[(move1, move2)]
        score1 += reward1
        score2 += reward2

    return score1, score2

def run_tournament(rounds, iterations):
    """
    Run the Axelrod tournament for a specified number of rounds and iterations.

    Args:
        rounds (int): Number of rounds per match.
        iterations (int): Number of tournament iterations.

    Prints the results of each match and the final standings.
    """
    strategy_names = list(strategies.keys())
    # Initialize results dictionary
    results = {
        name: {
            'score': 0,
            'wins': 0,
            'matches': 0
        } for name in strategy_names
    }

    # Print tournament header
    print("=" * 70)
    print(f"{'Axelrod Tournament':^70}")
    print("=" * 70)
    print(f"Total Rounds per Match: {rounds}\n")

    print(f"{'Match':<40} {'Result':<15} {'Winner':<15}")
    print("-" * 70)

    # Iterate over each pair of strategies
    for k in range(iterations):
        for i in range(len(strategy_names)):
            for j in range(i, len(strategy_names)):
                name1 = strategy_names[i]
                name2 = strategy_names[j]
                score1, score2 = play_match(strategies[name1], strategies[name2], rounds)

                results[name1]['score'] += score1
                results[name2]['score'] += score2
                results[name1]['matches'] += 1
                results[name2]['matches'] += 1

                # Determine the winner of the match
                if score1 > score2:
                    winner = "Win"
                    results[name1]['wins'] += 1
                elif score2 > score1:
                    winner = "Loss"
                    results[name2]['wins'] += 1
                else:
                    winner = "Draw"

                if k == iterations - 1:
                    print(f"{name1} vs {name2:<28} {score1}-{score2:<10} {winner}")
            if k == iterations - 1:
                print()

    # Print final standings
    print("=" * 70)
    print(f"{'Final Standings (after ' + str(rounds) + ' rounds per match)':^70}")
    print("=" * 70)
    print(f"{'Strategy':<30} {'Wins':<10} {'Score':<12} {'Avg Score':<12}")
    print("-" * 70)

    for name, data in sorted(results.items(), key=lambda x: x[1]['score'], reverse=True):
        avg_score = data['score'] / data['matches'] if data['matches'] else 0
        print(f"{name:<30} {data['wins']:<10} {data['score']:<12} {avg_score:<12.0f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Axelrod Tournament.")
    parser.add_argument("--rounds", "-r", type=int, default=200, help="Number of rounds per match (default: 200)")
    parser.add_argument("--iterations", "-i", type=int, default=1, help="Number of tournament iterations (default: 1)")
    args = parser.parse_args()

    run_tournament(rounds=args.rounds, iterations=args.iterations)

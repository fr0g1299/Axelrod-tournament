import axelrod as axl


class GrudgerMoreForgiving(axl.Player):
    """
    A strategy that cooperates until the opponent defects more than 3 times,
    after which it defects forever.
    """

    name = "Grudger More Forgiving"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }
    defections = 0

    def strategy(self, opponent):
        # Count opponent defections
        if opponent.history:
            if opponent.history[-1] == axl.Action.D:
                self.defections += 1

        # Betray on the last move
        if len(self.history) == self.match_attributes["length"] - 1:
            return axl.Action.D

        # Cooperate until the opponent defects more than 3 times
        if self.defections > 3:
            return axl.Action.D

        # Cooperate otherwise
        return axl.Action.C

class TitForTatModified(axl.Player):
    """
    A strategy that behaves like Tit for Tat but:
    1. Betrays on the last three moves.
    2. Switches to always defect if the opponent defects 5 times.
    """

    name = "Tit For Tat Modified"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    defections = 0

    def strategy(self, opponent):
        # Count opponent defections
        if opponent.history:
            if opponent.history[-1] == axl.Action.D:
                self.defections += 1

        # Betray on the last three moves
        if len(self.history) in range(self.match_attributes["length"] - 3, self.match_attributes["length"]):
            return axl.Action.D

        # Switch to always defect if opponent defects 5 times
        if self.defections >= 5:
            return axl.Action.D

        # Standard Tit for Tat behavior otherwise
        if opponent.history:
            return opponent.history[-1]
        return axl.Action.C

class TitForTwoTatsModified(axl.Player):
    """
    A strategy that behaves like Tit for Tat but:
    1. Betrays on the last three moves.
    """

    name = "Tit For Two Tats Modified"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent):
        # Betray on the last three moves
        if len(self.history) in range(self.match_attributes["length"] - 3, self.match_attributes["length"]):
            return axl.Action.D

        # Tit for Two Tats behavior otherwise
        if len(opponent.history) >= 2 and opponent.history[-1] == axl.Action.D and opponent.history[-2] == axl.Action.D:
            return axl.Action.D
        return axl.Action.C

class TitForTatLastBetray(axl.Player):
    """
    A strategy that behaves like Tit for Tat but:
    1. Betrays on the last move.
    """

    name = "Tit For Tat Last Betray"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent):
        # Betray on the last move
        if len(self.history) == self.match_attributes["length"] - 1:
            return axl.Action.D

        # Standard Tit for Tat behavior otherwise
        if opponent.history:
            return opponent.history[-1]
        return axl.Action.C
    
class PeriodicDDC(axl.Player):
    """
    A strategy that follows a periodic pattern: Defect, Defect, Cooperate.
    """

    name = "Periodic DDC"
    classifier = {
        "memory_depth": 3,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent):
        # Periodic pattern: Defect, Defect, Cooperate
        pattern = [axl.Action.D, axl.Action.D, axl.Action.C]
        return pattern[len(self.history) % len(pattern)]


class PeriodicCCD(axl.Player):
    """
    A strategy that follows a periodic pattern: Cooperate, Cooperate, Defect.
    """

    name = "Periodic CCD"
    classifier = {
        "memory_depth": 3,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent):
        # Periodic pattern: Cooperate, Cooperate, Defect
        pattern = [axl.Action.C, axl.Action.C, axl.Action.D]
        return pattern[len(self.history) % len(pattern)]


class GrudgerForgiving(axl.Player):
    """
    A strategy that cooperates until betrayed 3 times, then always defects.
    """

    name = "Grudger Forgiving"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    defections = 0

    def strategy(self, opponent):
        # Count opponent defections
        if opponent.history:
            if opponent.history[-1] == axl.Action.D:
                self.defections += 1

        if self.defections > 3:
            return axl.Action.D
        return axl.Action.C


players = [
    axl.Cooperator(),
    axl.Defector(),
    axl.Random(),
    axl.TitForTat(),
    TitForTatModified(),
    TitForTatLastBetray(),
    axl.ContriteTitForTat(),
    axl.TitFor2Tats(),
    TitForTwoTatsModified(),
    PeriodicDDC(),
    PeriodicCCD(),
    axl.Grudger(),
    GrudgerForgiving(),
    GrudgerMoreForgiving(),
    axl.ForgivingTitForTat(),
    axl.NaiveProber()
]

tournament = axl.Tournament(players)
results = tournament.play()
print("Scores:")
for player, score in zip(players, results.scores):
    avg_score = sum(score) / len(score)
    print(f"{player.name}: {avg_score:.2f}")

average_scores = [sum(score)/len(score) for score in results.scores]
best_index = average_scores.index(max(average_scores))
print(f"\nBest strategy: {players[best_index].name} with average score {average_scores[best_index]:.2f}")

# Axelrod-tournament

This project simulates the **Iterated Prisoner's Dilemma** through an Axelrod-style tournament, where a variety of strategies compete to maximize their payoff over repeated interactions. The tournament is customizable in terms of match length and the number of iterations.

## Project Structure

- `strategies.py`: Contains the implementations of various strategies used in the tournament.
- `main.py`: Runs the tournament, prints match results, and computes final standings.
- `library.py`: A script that uses the [Axelrod Python library](https://github.com/Axelrod-Python/Axelrod) to simulate a tournament with custom strategies implemented as subclasses of `axelrod.Player`. It includes additional strategies such as `Grudger Forgiving`, `Tit for Tat Modified`, and periodic strategies.

## Strategies

Implemented in `strategies.py`, the following strategies are available:

- **Always Cooperate**: Always plays `C`.
- **Always Betray**: Always plays `B`.
- **Random**: Randomly chooses `C` or `B`.
- **Tit for Tat**: Starts with `C`, then mirrors the opponent’s last move.
- **Tit for Tat Last Betray**: Behaves like Tit for Tat but always betrays in the final round.
- **Tit for Tat Modified**: Betrays on the last three moves and if the opponent has defected at least 5 times.
- **Reverse Tit for Tat**: Starts with `B`, then mirrors opponent’s last move.
- **Tit for Two Tats**: Defects only if the opponent defected twice in a row.
- **Tit for Two Tats Modified**: Betrays if the opponent has defected twice in a row or during the last 3 rounds of the game.
- **Periodic DDC**: Cycles through `D`, `D`, `C` pattern.
- **Periodic CCD**: Cycles through `C`, `C`, `D` pattern.
- **Grudger**: Cooperates until betrayed, then always defects.
- **Grudger Forgiving**: Same as Grudger but forgives up to 2 defections.
- **Grudger More Forgiving**: Same as above but forgives up to 4 defections.
- **Forgiving Tit for Tat**: Like Tit for Tat, but forgives if the last 3 moves were cooperations.
- **Naive Prober**: Tit for Tat with a small chance of probing (random betrayal).

## How to Run

1. Clone the repository to your local machine.

2. **Run the tournament**:
    ```sh
    python main.py -r 200 -i 1
    ```

   - You can customize the number of rounds per match and tournament iterations using the flags:
     - `--rounds`, `-r`: Number of rounds per match (default: 200)
     - `--iterations`, `-i`: Number of tournament repetitions (default: 1)

## Example Output

Here’s a sample output from a run with `-r 200`:

```
    ======================================================================
                            Axelrod Tournament
    ======================================================================
    Total Rounds per Match: 200

    Match                                    Result          Winner
    ----------------------------------------------------------------------
    Always Cooperate vs Always Cooperate             600-600        Draw
    Always Cooperate vs Always Betray                0-1000       Loss
    Always Cooperate vs Random                       345-770        Loss
    Always Cooperate vs Tit for Tat                  600-600        Draw
    Always Cooperate vs Tit for Tat Modified         597-602        Loss
    Always Cooperate vs Tit for Tat Last Betray      597-602        Loss
    Always Cooperate vs Reverse Tit for Tat          597-602        Loss
    Always Cooperate vs Tit for Two Tats             600-600        Draw
    Always Cooperate vs Periodic DDC                 198-868        Loss
    Always Cooperate vs Periodic CCD                 402-732        Loss
    Always Cooperate vs Grudger                      600-600        Draw
    Always Cooperate vs Grudger Forgiving            600-600        Draw
    Always Cooperate vs Grudger More Forgiving       600-600        Draw
    Always Cooperate vs Forgiving Tit for Tat        600-600        Draw
    Always Cooperate vs Naive Prober                 540-640        Loss
    Always Cooperate vs Tit for Two Tats Modified    591-606        Loss

    Always Betray vs Always Betray                200-200        Draw
    Always Betray vs Random                       552-112        Win
    Always Betray vs Tit for Tat                  204-199        Win
    Always Betray vs Tit for Tat Modified         204-199        Win
    Always Betray vs Tit for Tat Last Betray      204-199        Win
    Always Betray vs Reverse Tit for Tat          200-200        Draw
    Always Betray vs Tit for Two Tats             208-198        Win
    Always Betray vs Periodic DDC                 464-134        Win
    Always Betray vs Periodic CCD                 736-66         Win
    Always Betray vs Grudger                      204-199        Win
    Always Betray vs Grudger Forgiving            208-198        Win
    Always Betray vs Grudger More Forgiving       216-196        Win
    Always Betray vs Forgiving Tit for Tat        204-199        Win
    Always Betray vs Naive Prober                 204-199        Win
    Always Betray vs Tit for Two Tats Modified    208-198        Win

    Random vs Random                       443-443        Draw
    Random vs Tit for Tat                  435-435        Draw
    Random vs Tit for Tat Modified         119-619        Loss
    Random vs Tit for Tat Last Betray      456-456        Draw
    Random vs Reverse Tit for Tat          447-447        Draw
    Random vs Tit for Two Tats             640-375        Win
    Random vs Periodic DDC                 325-520        Loss
    Random vs Periodic CCD                 565-410        Win
    Random vs Grudger                      103-603        Loss
    Random vs Grudger Forgiving            120-600        Loss
    Random vs Grudger More Forgiving       121-586        Loss
    Random vs Forgiving Tit for Tat        452-452        Draw
    Random vs Naive Prober                 416-456        Loss
    Random vs Tit for Two Tats Modified    638-373        Win

    Tit for Tat vs Tit for Tat                  600-600        Draw
    Tit for Tat vs Tit for Tat Modified         597-602        Loss
    Tit for Tat vs Tit for Tat Last Betray      597-602        Loss
    Tit for Tat vs Reverse Tit for Tat          500-500        Draw
    Tit for Tat vs Tit for Two Tats             600-600        Draw
    Tit for Tat vs Periodic DDC                 397-402        Loss
    Tit for Tat vs Periodic CCD                 534-534        Draw
    Tit for Tat vs Grudger                      600-600        Draw
    Tit for Tat vs Grudger Forgiving            600-600        Draw
    Tit for Tat vs Grudger More Forgiving       600-600        Draw
    Tit for Tat vs Forgiving Tit for Tat        600-600        Draw
    Tit for Tat vs Naive Prober                 247-252        Loss
    Tit for Tat vs Tit for Two Tats Modified    593-598        Loss

    Tit for Tat Modified vs Tit for Tat Modified         598-598        Draw
    Tit for Tat Modified vs Tit for Tat Last Betray      598-598        Draw
    Tit for Tat Modified vs Reverse Tit for Tat          215-215        Draw
    Tit for Tat Modified vs Tit for Two Tats             602-597        Win
    Tit for Tat Modified vs Periodic DDC                 461-146        Win
    Tit for Tat Modified vs Periodic CCD                 719-104        Win
    Tit for Tat Modified vs Grudger                      602-597        Win
    Tit for Tat Modified vs Grudger Forgiving            602-597        Win
    Tit for Tat Modified vs Grudger More Forgiving       602-597        Win
    Tit for Tat Modified vs Forgiving Tit for Tat        602-597        Win
    Tit for Tat Modified vs Naive Prober                 225-225        Draw
    Tit for Tat Modified vs Tit for Two Tats Modified    593-598        Loss

    Tit for Tat Last Betray vs Tit for Tat Last Betray      598-598        Draw
    Tit for Tat Last Betray vs Reverse Tit for Tat          500-500        Draw
    Tit for Tat Last Betray vs Tit for Two Tats             602-597        Win
    Tit for Tat Last Betray vs Periodic DDC                 397-402        Loss
    Tit for Tat Last Betray vs Periodic CCD                 536-531        Win
    Tit for Tat Last Betray vs Grudger                      602-597        Win
    Tit for Tat Last Betray vs Grudger Forgiving            602-597        Win
    Tit for Tat Last Betray vs Grudger More Forgiving       602-597        Win
    Tit for Tat Last Betray vs Forgiving Tit for Tat        602-597        Win
    Tit for Tat Last Betray vs Naive Prober                 226-231        Loss
    Tit for Tat Last Betray vs Tit for Two Tats Modified    593-598        Loss

    Reverse Tit for Tat vs Reverse Tit for Tat          200-200        Draw
    Reverse Tit for Tat vs Tit for Two Tats             602-597        Win
    Reverse Tit for Tat vs Periodic DDC                 398-398        Draw
    Reverse Tit for Tat vs Periodic CCD                 536-531        Win
    Reverse Tit for Tat vs Grudger                      203-203        Draw
    Reverse Tit for Tat vs Grudger Forgiving            602-597        Win
    Reverse Tit for Tat vs Grudger More Forgiving       602-597        Win
    Reverse Tit for Tat vs Forgiving Tit for Tat        500-500        Draw
    Reverse Tit for Tat vs Naive Prober                 221-221        Draw
    Reverse Tit for Tat vs Tit for Two Tats Modified    595-595        Draw

    Tit for Two Tats vs Tit for Two Tats             600-600        Draw
    Tit for Two Tats vs Periodic DDC                 330-670        Loss
    Tit for Two Tats vs Periodic CCD                 402-732        Loss
    Tit for Two Tats vs Grudger                      600-600        Draw
    Tit for Two Tats vs Grudger Forgiving            600-600        Draw
    Tit for Two Tats vs Grudger More Forgiving       600-600        Draw
    Tit for Two Tats vs Forgiving Tit for Tat        600-600        Draw
    Tit for Two Tats vs Naive Prober                 275-300        Loss
    Tit for Two Tats vs Tit for Two Tats Modified    592-602        Loss

    Periodic DDC vs Periodic DDC                 332-332        Draw
    Periodic DDC vs Periodic CCD                 670-330        Win
    Periodic DDC vs Grudger                      138-463        Loss
    Periodic DDC vs Grudger Forgiving            142-462        Loss
    Periodic DDC vs Grudger More Forgiving       153-458        Loss
    Periodic DDC vs Forgiving Tit for Tat        402-397        Win
    Periodic DDC vs Naive Prober                 370-405        Loss
    Periodic DDC vs Tit for Two Tats Modified    662-332        Win

    Periodic CCD vs Periodic CCD                 468-468        Draw
    Periodic CCD vs Grudger                      76-731        Loss
    Periodic CCD vs Grudger Forgiving            86-726        Loss
    Periodic CCD vs Grudger More Forgiving       106-716        Loss
    Periodic CCD vs Forgiving Tit for Tat        534-534        Draw
    Periodic CCD vs Naive Prober                 494-549        Loss
    Periodic CCD vs Tit for Two Tats Modified    722-407        Win

    Grudger vs Grudger                      600-600        Draw
    Grudger vs Grudger Forgiving            600-600        Draw
    Grudger vs Grudger More Forgiving       600-600        Draw
    Grudger vs Forgiving Tit for Tat        600-600        Draw
    Grudger vs Naive Prober                 229-229        Draw
    Grudger vs Tit for Two Tats Modified    593-598        Loss

    Grudger Forgiving vs Grudger Forgiving            600-600        Draw
    Grudger Forgiving vs Grudger More Forgiving       600-600        Draw
    Grudger Forgiving vs Forgiving Tit for Tat        600-600        Draw
    Grudger Forgiving vs Naive Prober                 260-265        Loss
    Grudger Forgiving vs Tit for Two Tats Modified    592-602        Loss

    Grudger More Forgiving vs Grudger More Forgiving       600-600        Draw
    Grudger More Forgiving vs Forgiving Tit for Tat        600-600        Draw
    Grudger More Forgiving vs Naive Prober                 290-305        Loss
    Grudger More Forgiving vs Tit for Two Tats Modified    591-606        Loss

    Forgiving Tit for Tat vs Forgiving Tit for Tat        600-600        Draw
    Forgiving Tit for Tat vs Naive Prober                 277-282        Loss
    Forgiving Tit for Tat vs Tit for Two Tats Modified    593-598        Loss

    Naive Prober vs Naive Prober                 224-229        Loss
    Naive Prober vs Tit for Two Tats Modified    626-541        Win

    Tit for Two Tats Modified vs Tit for Two Tats Modified    594-594        Draw

    ======================================================================
                Final Standings (after 200 rounds per match)
    ======================================================================
    Strategy                       Wins       Score        Avg Score
    ----------------------------------------------------------------------
    Grudger Forgiving              3          9429         555
    Grudger More Forgiving         3          9428         555
    Tit for Two Tats Modified      9          9040         532
    Tit for Tat Modified           10         9039         532
    Grudger                        3          9015         530
    Forgiving Tit for Tat          0          8946         526
    Tit for Tat Last Betray        8          8915         524
    Tit for Tat                    0          8899         523
    Tit for Two Tats               0          8763         515
    Always Cooperate               0          8667         510
    Reverse Tit for Tat            5          7123         419
    Periodic CCD                   3          6924         407
    Periodic DDC                   8          6741         397
    Random                         4          6605         389
    Naive Prober                   12         5638         332
    Always Betray                  14         5416         319
```

## Insights

Based on the tournament output, we can draw several interesting conclusions:

1. **Grudger-based strategies dominate**  
   - **Grudger More Forgiving**, **Grudger Forgiving**, and **Grudger** all performed exceptionally well, occupying 3 of the top 5 positions.
   - These strategies strike a balance between cooperation and retribution, punishing defection but forgiving occasional missteps.

2. **Modified Tit-for-Tat variants outperform standard Tit-for-Tat**  
    - **Tit for Tat Modified** and **Tit for Two Tats Modified** demonstrated superior performance compared to regular **Tit for Tat**.  
    - Both strategies ranked higher in total score and average score, with **Tit for Two Tats Modified** achieving 9 wins and **Tit for Tat Modified** achieving 10 wins.  
    - This suggests that adaptive strategies, particularly those that account for opponent behavior or end-game scenarios, are more effective in maximizing payoffs.

3. **Always Betray and Naive Prober were aggressive, but not dominant**  
   - While **Always Betray** had the most wins (14), it ranked near the bottom in total score and average score.
   - **Naive Prober** also had a high number of wins (12), but poor average performance suggests it exploited some weaker strategies but performed inconsistently overall.

4. **Periodic and random strategies underperformed**  
   - Strategies like **Periodic DDC**, **Periodic CCD**, and **Random** generally had low scores and average placements. Their lack of adaptability likely made them predictable or exploitable.

5. **Always Cooperate is easily exploited**  
   - Despite some high-scoring draws, **Always Cooperate** consistently lost to most other strategies, demonstrating that unconditional cooperation is not sustainable in adversarial environments.

6. **Forgiving strategies are solid but not top-tier**  
   - **Forgiving Tit for Tat** had moderate performance with high draw rates, showing that forgiveness helps avoid conflict but may not capitalize on strategic advantage.

### Summary Table (Top Performers)

| Strategy                  | Wins | Total Score | Avg. Score |
|---------------------------|------|-------------|------------|
| Grudger Forgiving         | 3    | 9429        | 555        |
| Grudger More Forgiving    | 3    | 9428        | 555        |
| Tit for Two Tats Modified | 9    | 9040        | 532        |
| Tit for Tat Modified      | 10   | 9039        | 532        |
| Grudger                   | 3    | 9015        | 530        |


## License

This project is licensed under the **MIT License**.

## Acknowledgments

- Inspired by Robert Axelrod's original research on cooperation and strategy in repeated games.
- Thanks to the open-source community and game theory pioneers.

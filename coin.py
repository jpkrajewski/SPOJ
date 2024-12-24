def maximize_fun(budget, parties):
    """
    Function to maximize fun within a given budget using dynamic programming.
    Args:
    - budget (int): Total available budget.
    - parties (list of tuples): List of (price, fun) for each party.

    Returns:
    - tuple: (minimum budget spent, maximum fun achieved)
    """
    parties_count = len(parties)

    # Initialize DP table with 0
    DP = [[0] * (budget + 1) for _ in range(parties_count + 1)]
    print("Initial DP table:")
    for row in DP:
        print(row)
    print("\n")

    # Fill the DP table
    for i in range(1, parties_count + 1):
        price, fun = parties[i - 1]
        for b in range(budget + 1):
            if b >= price:
                # Maximize fun: Include or exclude the current party
                DP[i][b] = max(DP[i - 1][b], DP[i - 1][b - price] + fun)
            else:
                # Exclude the current party
                DP[i][b] = DP[i - 1][b]

        # Debugging: Print the DP table row for the current party
        print(f"After considering party {i} (price={price}, fun={fun}): {DP[i]}")
    print("\n")

    # Extract maximum fun and minimum budget spent
    max_fun = DP[parties_count][budget]
    min_budget = 0

    # Find the minimum budget that achieves max fun
    for i in range(budget + 1):
        if DP[parties_count][i] == max_fun:
            min_budget = i
            break

    return min_budget, max_fun


# Test cases for the function
if __name__ == "__main__":
    # Sample test case
    budget = 50
    parties = [
        (12, 3),
        (15, 8),
        (16, 9),
        (16, 6),
        (10, 2),
        (21, 9),
        (18, 4),
        (12, 4),
        (17, 8),
        (18, 9),
    ]

    min_budget, max_fun = maximize_fun(budget, parties)
    print(f"Result: Minimum Budget = {min_budget}, Maximum Fun = {max_fun}")


while True:
    try:
        budget, parties_count = map(int, input().split())
        if budget == 0 and parties_count == 0:
            break
            
        prices = []
        fun_values = []
        for _ in range(parties_count):
            price, fun = map(int, input().split())
            prices.append(price)
            fun_values.append(fun)
            
        # Initialize DP table starting from index 1
        dp = [[0 for _ in range(budget + 1)] for _ in range(parties_count + 1)]
        
        # Fill DP table
        for i in range(1, parties_count + 1):
            for j in range(1, budget + 1):
                if prices[i-1] <= j:
                    dp[i][j] = max(fun_values[i-1] + dp[i-1][j-prices[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        # Find minimum budget needed for max fun
        max_fun = dp[-1][-1]
        j = budget
        while dp[parties_count][j] == max_fun:
            j -= 1
        print(j+1, max_fun)
    except Exception:
        break
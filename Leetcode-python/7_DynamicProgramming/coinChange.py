def coinChange(coins, amount):
    # if need to make 0, no need anything return
    if(amount <= 0):
        return 0

    INT_MAX = 1<<32

    dp = [INT_MAX] * (amount + 1)
    dp[0] = 0

    for amount in range(1, amount+1): # iterating over amount
        for coin in coins:
            # coin that we are taking is less than or equal than amount
            if(coin <= amount):
                # update the dp array
                dp[amount] = min(dp[amount-coin]+1, dp[amount])
    return dp[amount] if dp[amount] != INT_MAX else -1


coins = [1,2,5]
amount = 11
ans = coinChange(coins, amount)
print(ans)


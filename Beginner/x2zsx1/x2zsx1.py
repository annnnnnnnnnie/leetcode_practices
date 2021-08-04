class Solution:
    @staticmethod
    def max_profit(prices):
        if len(prices) <= 1:
            return 0

        prices += [0]

        all_transactions = []

        low_index = 0
        current_price = prices[low_index]

        for high_index in range(len(prices)):
            if prices[high_index] >= current_price:
                current_price = prices[high_index]
            else:
                all_transactions += [(low_index, high_index, current_price - prices[low_index])]
                low_index = high_index
                current_price = prices[low_index]
        all_profits = [profit for (_, _, profit) in all_transactions]
        return sum(all_profits)

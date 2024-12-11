###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always an egg_weigh of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg_weigh weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    7
    Returns: int, smallest number of eggs needed to make target weight
    """

    local_result_dict = {}

    if target_weight in memo:
        return memo[target_weight]
    else:
        for egg_weight in egg_weights:
            if not target_weight:
                local_result_dict[egg_weight] = 0
            elif egg_weight > target_weight:
                continue
            else:
                local_result_dict[egg_weight] = dp_make_weight(egg_weights, target_weight - egg_weight, memo) + 1

    result = min(local_result_dict.values())
    memo[target_weight] = result
    return result


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    # egg_weights = (1, 5, 10)
    # n = 10
    egg_weights = (1, 5, 10, 25)
    n = 99
    # print("Egg weights = (1, 5, 10, 25)")
    # print("n = 99")
    # print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
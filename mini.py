import math

def minimax(values, is_max):
    # Base case
    if len(values) == 1:
        return values[0]

    mid = len(values) // 2
    left = values[:mid]
    right = values[mid:]

    if is_max:
        return max(minimax(left, False), minimax(right, False))
    else:
        return min(minimax(left, True), minimax(right, True))


# USER INPUT
values = list(map(int, input("Enter numbers (space-separated): ").split()))

if len(values) == 0:
    print("Please enter at least one number.")
else:
    result = minimax(values, True)
    print("The optimal value is:", result)

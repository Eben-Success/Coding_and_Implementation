
def can_ship(candidate, weights, days):
    days_taken = 1
    cur_weight = 0

    for weight in weights:
        cur_weight += weight

        if cur_weight > candidate:
            cur_weight = weight
            days_taken += 1

    return days_taken <= days

def ship(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2

        if can_ship(mid, weights, days):
            right = mid
        else:
            left = mid + 1

    return right

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(ship(weights, days))


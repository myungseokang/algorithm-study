
def solution(food_times, k):
    answer = 0
    food_count = len(food_times)
    last_eating = 0
    t = 0

    if sum(food_times) <= k:
        return -1

    while t < k:
        eating_idx = t % food_count
        print(t, eating_idx)
        if food_times[eating_idx] != 0:
            food_times[eating_idx] -= 1
            last_eating = eating_idx
            t += 1

    print(food_times)

    while True:
        last_eating += 1
        last_eating %= food_count
        if food_times[last_eating] != 0:
            answer = last_eating
            break
        print(last_eating)

    return answer + 1


print(solution([3, 1, 2], 5))

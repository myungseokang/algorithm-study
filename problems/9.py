def solution(s):
    answer = len(s)
    
    length = len(s)

    total = []
    
    for i in range(1, length // 2 + 1):
        prev = s[:i]
        prev_count = 1
        compressed = ""

        for j in range(i, length, i):
            if prev == s[j:j + i]:
                prev_count += 1
            else:
                compressed += str(prev_count) + prev if prev_count >= 2 else prev
                prev = s[j:j + i]
                prev_count = 1
        
        compressed += str(prev_count) + prev if prev_count >= 2 else prev
        answer = min(answer, len(compressed))
    
    return answer


print(solution('aabbaccc'))

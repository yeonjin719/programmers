def solution(k, score):
    answer = []
    rank = []
    for i in range(len(score)):
        if i < k:
            rank.append(score[i])
        else:
            if rank[-1] < score[i]:
                rank[-1] = score[i]
        rank.sort(reverse=True)
        answer.append(rank[-1])
    return answer

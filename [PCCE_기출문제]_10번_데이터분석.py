def solution(data, ext, val_ext, sort_by):
    answer = []
    info = {"code":0,"date":1,"maximum":2,"remain":3}
    for i in range(len(data)):
        if data[i][info[ext]] < val_ext:
            answer.append(data[i])
    index = info[sort_by]
    answer.sort(key = lambda x : x[index])
    return answer




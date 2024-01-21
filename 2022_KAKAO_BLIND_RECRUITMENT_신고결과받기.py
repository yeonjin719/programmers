def solution(id_list, report, k):
    cnt = {}
    stop={}
    answer = []
    for i in range(len(id_list)):
        answer.append(0)
    for i in range(len(report)):
        a,b = report[i].split(" ")
        if a in cnt.keys():
            if b in cnt[a]:
                pass
            else:
                cnt[a].append(b)
        else:
            cnt[a] = [b]
    cnt_keys = list(cnt.keys())       
    for i in range(len(cnt)):
        for j in cnt[cnt_keys[i]]:
            if j in stop.keys():
                stop[j] += 1
            else:
                stop[j] = 1
    li = list(stop.keys())
    for i in range(len(stop)):
        if stop[li[i]] >= k:
            for j in range(len(id_list)):
                if id_list[j] in cnt.keys():
                    if li[i] in cnt[id_list[j]]:
                        answer[j] += 1
        else:
            pass
    return answer

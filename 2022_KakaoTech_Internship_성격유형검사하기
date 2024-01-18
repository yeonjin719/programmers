def solution(survey, choices):
    score = [3,2,1,0,1,2,3]
    result = {'R':0, 'T':0, 'F':0,'C':0,'M':0,'J':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        A = list(survey[i])
        if choices[i] <= 3:
            result[A[0]] += score[choices[i]-1]
        else:                
            result[A[1]] += score[choices[i]-1]
    answer = ''
    if result['R'] >= result['T']:
        answer += 'R'
    else:
        answer += 'T'
    if result['C'] >= result['F']:
        answer += 'C'
    else:
        answer += 'F'
    if result['J'] >= result['M']:
        answer += 'J'
    else:
        answer += 'M'
    if result['A'] >= result['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer

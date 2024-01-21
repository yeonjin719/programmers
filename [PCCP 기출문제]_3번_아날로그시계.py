def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    startTime = h1*3600 + m1*60 + s1
    endTime = h2*3600 + m2*60 + s2
    if startTime == 0 * 3600 or startTime == 12 * 3600:
        answer += 1
    while startTime < endTime:
        hCur = startTime / 120 % 360
        mCur = startTime / 10 % 360
        sCur = startTime * 6 % 360
        hNext = 360 if (startTime + 1) / 120 % 360 == 0  else (startTime + 1)/120%360
        mNext = 360 if (startTime + 1) / 10 % 360 == 0 else (startTime + 1) / 10 % 360
        sNext = 360 if (startTime + 1) * 6 % 360 == 0 else (startTime + 1) * 6 % 360

        if sCur < hCur and sNext >= hNext:
            answer += 1
        if sCur < mCur and sNext >= mNext:
            answer += 1
        if sNext == hNext and hNext == mNext:
            answer -= 1
        startTime += 1
    return answer

def solution(today, terms, privacies):
    Tyear, Tmonth, Tday = map(int, today.split("."))
    
    answer = []
    info = {}
    for i in range(len(terms)):
        kind, term = terms[i].split(" ")
        info[kind] = int(term)

    for i in range(len(privacies)):
        date, Pkind = privacies[i].split(" ")
        year, month, day = date.split(".")
        month = int(month)
        month += info[Pkind]
        day = int(day) 
        day -= 1
        year = int(year)
        if month > 12:
            if (month%12) == 0:
                year += (month//12) -1
            else:
                year += (month//12) 
            month %= 12
            if month == 0:
                month = 12
        if day <= 0:
            day = 28
            month -= 1
            if month < 1:
                month = 12
                year -= 1
        if Tyear > year:
            answer.append(i+1)
        elif Tyear == year and Tmonth > month:
            answer.append(i+1)
        elif Tyear == year and Tmonth == month and Tday > day:
            answer.append(i+1)
        else:
            pass
    return answer

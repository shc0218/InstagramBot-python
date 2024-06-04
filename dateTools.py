def chage_korean_dayofweek(day):
    day_of_week = {
        "Mon": "월",
        "Tue": "화",
        "Wed": "수",
        "Thu": "목",
        "Fri": "금",
        "Sat": "토",
        "Sun": "일"
    }
    for week in day_of_week.keys():
        if week in day:
            return day.replace(week, day_of_week[week])
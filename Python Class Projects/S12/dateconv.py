import datetime
from persiantools.jdatetime import JalaliDate


birthtime = "شروع 20 آذر 1388 - جمعه 13:00 تا 19:00"


def convert_birthtime(birthtime):

    parts = birthtime.split("-")

    date_part = parts[0].strip()
    time_part = parts[1].strip()

    date_words = date_part.split()

    day = int(date_words[1])
    month_name = date_words[2]
    year = int(date_words[3])

    months = {
        "فروردین": 1,
        "اردیبهشت": 2,
        "خرداد": 3,
        "تیر": 4,
        "مرداد": 5,
        "شهریور": 6,
        "مهر": 7,
        "آبان": 8,
        "آذر": 9,
        "دی": 10,
        "بهمن": 11,
        "اسفند": 12
    }

    month = months[month_name]

    jalali_date = JalaliDate(year, month, day)
    gregorian_date = jalali_date.to_gregorian()

    time_words = time_part.split()

    start_time = datetime.datetime.strptime(
        time_words[1],
        "%H:%M"
    ).time()

    end_time = datetime.datetime.strptime(
        time_words[3],
        "%H:%M"
    ).time()

    result = {
        "start_date": {
            "value": gregorian_date,
            "type": "date"
        },

        "start_time": {
            "value": start_time,
            "type": "time"
        },

        "end_time": {
            "value": end_time,
            "type": "time"
        }
    }

    return result


result = convert_birthtime(birthtime)

print(result)
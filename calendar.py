import math

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

jie_qi = ["小寒", "大寒", "立春", "雨水", "惊蛰", "春分",
          "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
          "小暑", "大暑", "立秋", "处暑", "白露", "秋分", 
          "寒露", "霜降", "立冬", "小雪", "大雪", "冬至"]

jie_qi_to_month = {
    "大寒": "腊月", "雨水": "正月", "春分": "二月", "谷雨": "三月",
    "小满": "四月", "夏至": "五月", "大暑": "六月", "处暑": "七月",
    "秋分": "八月", "霜降": "九月", "小雪": "十月", "冬至": "冬月",
}

chinese_day = ['', "初一", "初二", "初三", "初四", "初五", "初六", "初七",
                   "初八", "初九", "初十", "十一", "十二", "十三", "十四",
                   "十五", "十六", "十七", "十八", "十九", "二十", "廿一",
                   "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八",
                   "廿九", "三十"]

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def get_days_in_month(year, month):
    if is_leap_year(year) and month == 1:
        return days_in_month[month] + 1
    else:
        return days_in_month[month]

def function1(y, x):
    return 365.242 * (y - 1900) + 6.2 + 15.22 * x - 1.9 * math.sin(0.262 * x)

def function2(m):
    return 1.6 + 29.5306 * m + 0.4 * math.sin(1 - 0.45058 * m)

def days_to_gregorian_date(n):
    # @param n: num days from 1900-01-00
    y = 1900
    m = 0
    while n > get_days_in_month(y, m):
        n = n - get_days_in_month(y, m)
        m = (m + 1) % 12
        if m == 0:
            y = y + 1
    year = y
    month = m + 1
    day = n
    return year, month, day

def gregorian_date_to_days(year, month, day):
    '''
    Count the total number of days from 1900-01-00 to the
    current gregorian date
    '''
    days = 0
    for y in range(1900, year):
        if is_leap_year(y):
            days = days + 366
        else:
            days = days + 365
    
    for m in range(0, month-1):
        days = days + get_days_in_month(year, m)

    days = days + day
    return days

# print(gregorian_date_to_days(2001, 1, 1))

def get_nearest_shuo_day(day):
    L= 0
    while day >= int(function2(L)):
        L = L + 1
    return L-1, function2(L-1)

days = gregorian_date_to_days(2019, 4, 10)
# print(days)
a, shuo_day = get_nearest_shuo_day(days)
# print(shuo_day)
shuo_day = int(shuo_day)
y, m, d = days_to_gregorian_date(shuo_day)
# print("{}-{}-{}".format(y, m, d))
print(chinese_day[days - shuo_day + 1])

# m, d = days_to_gregorian_date(10)
# print("{}-{}".format(m, d))

def create_jie_qi_list(year):
    dong_zhi_day = function1(year - 1, jie_qi.index("冬至"))
    result = [{
        "day": int(dong_zhi_day),
        "month": jie_qi_to_month["冬至"],
        "jieqi": "冬至"
    }]
    for i in range(1, len(jie_qi), 2):
        jieqi_name = jie_qi[i]
        day = function1(year, i)
        result.append({
            "day": int(day),
            "month": jie_qi_to_month[jieqi_name],
            "jieqi": jieqi_name
        })
    return result

jie_qi_list = create_jie_qi_list(2019)
for item in jie_qi_list:
    print(item)


def create_month_list(year):
    days = int(function1(year-1, jie_qi.index("冬至")))
    m, shuo_day = get_nearest_shuo_day(days)
    result = []
    for i in range(m, m + 13):
        result.append({
            "month": None,
            "first_day": int(function2(i)),
            "last_day": int (function2(i+1) - 1)
        })
    return result

month_list = create_month_list(2019)
for item in month_list:
    print(item)

for i in range(0, 4):
    days = int(function1(2015, i))
    y, m, d = days_to_gregorian_date(days)
    print("{}-{}-{}".format(y, m, d))

    days = int(function2(i))
    y, m, d = days_to_gregorian_date(days)
    print("{}-{}-{}".format(y, m, d))


'''
print(is_leap_year(1900))
print(is_leap_year(1904))
print(is_leap_year(1905))
print(is_leap_year(2000))
'''


'''
print(function(1900, 0))
print(function(1900, 1))
print(function(1900, 2))
print(function(1900, 3))
'''


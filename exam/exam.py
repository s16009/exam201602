# 'hello, {name}!'と出力してください 。
def hello(name):
   print('hello, {0}!'.format(name))

# sentence の文字数を出力してください
def length(sentence):
    print(len("sentence"))


# sentence の2文字目から5文字目まで(5文字目は含まない)を出力してください
def slicing2to5(sentence):
    print("sentence"[1:4])


# number の符号を出力してください。ただし、0は'0'と出力してください
def number_sign(number):
    if number > 0:
        print("+")
    elif number == 0:
        print("0")
    else:
        print("-")


# number が素数なら'ok',そうでないなら'ng'と出力してください
def prime_number(number):
    count = 0
    for n in range(1, number+1):
        if number % n == 0:
            count += 1
    if count == 2:
        print("ok")
    else:
        print("ng")



# 1からnumberまでの合計を出力してください
def sum_from_1_to(number):
    count = 0
    for n in range(1, number):
        count += n
        print(count)


# numberの階乗(factorial)を出力してください
def factorial(number):
    import math
    print(math.factorial(number))


# リストdataの各要素(整数)を3乗した結果をリスト型として返してください
def cubic_list(date):
    pass

# 底辺x,高さyの直角三角形(right angled triangle)の残り1つの辺の長さを返してください
def calc_hypotenuse(x, y):
    import math
    return math.sqrt(x ** 2 + y ** 2)



# 底辺x,斜辺vの直角三角形の残り1つの辺の長さを返してください
def calc_subtense(x, v):
    import math
    return math.sqrt(abs(x ** 2 - v ** 2))


# 三辺の長さがそれぞれx,y,zの三角形の面積を返してください
def calc_area_triangle(x, y, z):
    import math
    return (z * (math.sqrt(x ** 2 - ((x ** 2 - y ** 2 ** 2) / (2 * z)) ** 2))) / 2



# 引数a,b,cを小数点以下2桁表示で空白切りで表示してください
def point_two_digits(a, b, c):
    print('{0} {1} {2}'.format(format(a, '.2f'), format(b, '.2f'), format(c, '.2f')))


# リストdataの内容を小さい順でソートした結果を返してください
def list_sort(data):
    return sorted(data)


# 文字列の並びを逆にしたものを返してください
def reverse_string(sentence):
    return sentence[::-1]

# dateから2016年4月1日までの日数を返してください
def days_from_date(date):
    import datetime
    a = datetime.date(2016, 4, 1)
    b = datetime.date(date)
    c = a - b
    return c.days

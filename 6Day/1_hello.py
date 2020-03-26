
# --------------------------------------------
# 해당 문자열 찾기

#   결과값
#   True
# --------------------------------------------

a = 'spartacodingclub@gmail.com'

# 1
def check_email1(text):
    return '@' in text

print(check_email1(a))

# 2
def check_email2(text):
    if text.find('@') -1:
        return True
    else:
        return False

print(check_email2(a))

# --------------------------------------------
# 메일 주소 찾기

#   결과값
#   gmail
# --------------------------------------------

def get_mail(text):
    return text.split('@')[1].split('.')[0]

print(get_mail(a))

# --------------------------------------------
# 리스트 안의 개수 세기

#   결과값
#   {'사과': 1, '감': 3, '배': 1, '포도': 3, '딸기': 2, '수박': 1}
# --------------------------------------------

b = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

def count_list(a_list):
    result = {}

    for fruit in a_list:
        if fruit in result:
            result[fruit] += 1
        else:
            result[fruit] = 1

    return result

# 결과값
print(count_list(b))

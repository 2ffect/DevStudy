############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user_data):
    user_id = str(user_data.get('id', '')) # get을 사용해서 아이디가 없는 경우 키 에러 방지, str로 받아서 정수로만 이루어진 경우 에러 방지
    check_list = "0123456789"
    if len(user_id) == 0: # 빈 문자열 인 경우 
        return False

    return user_id[-1] in check_list

# def is_id_valid(user_data):


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True


user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################

user_data3 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data3)) # False

user_data4 = {
    'id': 1515351,
    'password': '1q2w3e4r', 
} 
print(is_id_valid(user_data4)) # True


user_data5 = {
    'd': 'No id dict',
    'password': '1q2w3e4r', 
}
print(is_id_valid(user_data5)) # False
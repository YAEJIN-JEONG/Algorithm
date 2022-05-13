def solution(phone_book):
    # 전화번호 정렬
    phone_book.sort()

    # 현재와 바로 이전 전화번호만 서로 확인하면 됨
    for i in range(1, len(phone_book)):
        len_prev = len(phone_book[i - 1])

        if phone_book[i][:len_prev] == phone_book[i - 1]:
            return False

    return True

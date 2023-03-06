"""
호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.


"""


def solution(book_time):
    answer = 0
    start_res = []
    end_res = []
    for tm in book_time:
        start_res.append(int(tm[0].split(":")[0]) * 60 + int(tm[0].split(":")[1]))
        end_res.append(int(tm[1].split(":")[0]) * 60 + int(tm[1].split(":")[1]) + 9)

    start_res.sort()
    end_res.sort()

    cnt = 0
    while True:
        if not start_res or not end_res:
            break
        if start_res[0] <= end_res[0]:
            cnt += 1
            del start_res[0]
        else:
            cnt -= 1
            del end_res[0]
        if answer < cnt:
            answer = cnt

    return answer

if __name__ == '__main__':
    book_time = [[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]], [["09:10", "10:10"], ["10:20", "12:20"]], [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]]
    for book in book_time:
        solution(book)


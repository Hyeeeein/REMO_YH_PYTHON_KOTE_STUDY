from datetime import datetime

# 대여기간을 분으로 변환하는 함수
def convert_to_minutes(loan_period):
    # DDD/hh:mm 형식을 분으로 변환
    days, time = loan_period.split('/')
    hours, minutes = map(int, time.split(':'))
    return int(days) * 24 * 60 + hours * 60 + minutes

# 대여 시작 시간과 반납 시간으로 벌금을 계산하는 함수
def calculate_fine(start_time, end_time, loan_period_minutes, fine_per_minute):
    # 날짜/시간 형식에 맞춰 시간 차이를 계산
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
    
    # 대여 기간 초과한 시간 계산
    total_minutes = int((end - start).total_seconds() / 60)
    
    if total_minutes > loan_period_minutes:
        # 대여 기간을 초과한 시간에 대해 벌금 계산
        overdue_minutes = total_minutes - loan_period_minutes
        return overdue_minutes * fine_per_minute
    return 0

def main():
    N, loan_period, fine_per_minute = input().split()
    N = int(N)
    fine_per_minute = int(fine_per_minute)

    # 대여 기간을 분으로 변환
    loan_period_minutes = convert_to_minutes(loan_period)
    
    # 대여 기록을 관리할 딕셔너리
    rental_records = {}
    fines = {}

    for _ in range(N):
        data = input().split()
        date_time = data[0] + " " + data[1]  # "yyyy-MM-dd hh:mm"
        item = data[2]
        name = data[3]

        if name in rental_records and item in rental_records[name]:
            # 반납 시각은 입력 시각과 같음
            return_time = date_time
            start_time = rental_records[name][item]
            fine = calculate_fine(start_time, return_time, loan_period_minutes, fine_per_minute)
            if fine > 0:
                if name not in fines:
                    fines[name] = 0
                fines[name] += fine
            del rental_records[name][item]  # 반납 처리
        
        else:
            # 대여 기록 추가 (반납 시 추가되므로 대여 기록을 추가)
            if name not in rental_records:
                rental_records[name] = {}
            rental_records[name][item] = date_time

    # 벌금을 내야하는 사람이 없으면 -1 출력
    if not fines:
        print(-1)
    else:
        # 사전순으로 정렬하여 출력
        for name in sorted(fines):
            print(name, fines[name])

if __name__ == "__main__":
    main()



# import sys, heapq
# from datetime import datetime, timedelta

# N, L, F = list(input().split())

# def get_total_minutes(date_time_str):
#     # 문자열을 날짜와 시간으로 분리
#     date_part, time_part = date_time_str.split('/')  # "014"과 "10:10" 분리
#     day_of_year = int(date_part)  # "014" -> 14번째 날
#     hour, minute = map(int, time_part.split(':'))  # "10:10" -> 10시, 10분
    
#     # 현재 연도의 1월 1일을 기준으로 14번째 날짜 계산
#     start_date = datetime(datetime.now().year, 1, 1)  # 1월 1일
#     target_date = start_date + timedelta(days=day_of_year - 1, hours=hour, minutes=minute)
    
#     # 1월 1일부터 target_date까지의 총 분 수 계산
#     total_minutes = (target_date - start_date).total_seconds() / 60
    
#     return total_minutes

# total_minutes = get_total_minutes(L)
# print(total_minutes)

# name_heap = []
# dict = {}

# for _ in range(int(N)):
#     date, time, item, name = sys.stdin.readline().split()
#     heapq.heappush(name_heap, (name, item, date, time))


# while name_heap:
#     name, item, startDate, startTime = heapq.heappop(name_heap)
#     name, item, endDate, endTime= heapq.heappop(name_heap)
#     fmt = "%Y-%m-%d %H:%M"
#     date1 = datetime.strptime(startDate + ' ' + startTime, fmt)
#     date2 = datetime.strptime(endDate + ' '+ endTime, fmt)
#     time_diff = abs(date2 - date1)
#     minutes = time_diff.total_seconds() / 60 # 실 대여기간
#     money = (minutes - total_minutes) * int(F)
#     if money > 0:
#         dict[name] = dict.get(name, 0) + money



# print(dict)
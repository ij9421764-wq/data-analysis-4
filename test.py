import csv
import os  # 파일 경로를 다루는 파이썬 기본 모듈


def dp(name):
    here = os.path.dirname(os.path.abspath(__file__))

    for c in (
        os.path.join("data", name),
        os.path.join(here, "data", name),
        os.path.join(here, "..", "data", name),
    ):
        if os.path.exists(c):
            return c
    return os.path.join("data", name)


LOT = dp("17_열처리.csv")  # 오늘의 주 데이터
PROC = dp("17_열처리_공정.csv")  # 빈칸이  섞인 파일
WIDE = dp("20_cmapss_fd001_sample.csv")  # 열 수만 셉니다.


print("=" * 60)
print("[0] 파이썬 표현 미리보기")

x = 859.5318  # 뒤에서 실제로 나오는 온도 평균
print(
    f"1) {x:.2f} <- .2f = 소수 둘째 자리까지 출력 | {x:10.1f} <- 10칸 폭, 첫째 자리 | {44:>5d} <- 정수 5칸 오른쪽 | {0.00455:.1%} <-0.00455를 퍼센트로 "
)
with open(LOT, encoding="utf-8-sig") as f:
    r = csv.reader(f)
    header = next(r)  # 첫 줄은 열 이름이라 따로 꺼냄
    rows = list(r)  # 나머지 줄이 데이터

# [['09:00', '로트A', '861.9', '42.9', '0.451', '정상'],  ...
# 2차원임
print(rows)

# [861.9, 858.4, 858.7, 860.7, ...
# 1차원임
temps = [float(row[2]) for row in rows]
print(temps)

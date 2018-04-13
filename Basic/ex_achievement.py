
#성명, 국어, 영어, 수학점수를 입력 받아 서
#총점, 평균, 학점을 출력하는 프로그램 작성.
print("-"*25, "성적출력프로그램", "-"*25)
student = input("성명입력>>>")
kor = int(input("국어점수>>>") )
eng = int(input("영어점수>>>") )
mat = int(input("수학점수>>>") )

total = kor + eng + mat
avg = float(total) / 3.0
grade = 'F'

# if ~ elif문으로 조건을 비교 해서 출력한다.
if avg>=90:
    grade = 'A'
elif avg>=80:
    grade = 'B'
elif avg>=70:
    grade = 'C'
elif avg>=60:
    grade = 'D'
else:
    grade = 'F'

print("성명:", student)
print("국어점수:", kor)
print("영어점수:", eng)
print("수학점수:", mat);
print("총점:", total)
print("평균:", avg)
print("학점:", grade)
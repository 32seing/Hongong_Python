#inch 단위를 cm단위로 변경하기
#숫자 입력받기
raw_input = input("inch 단위의 숫자를 입력해주세요: ")

#입력받은 데이터를 숫자 자료형으로 변경하고 cm단위로 변경
inch = int(raw_input)
cm = inch * 2.54

#출력
print(inch, "inch는 cm단위로 ", cm, "cm 입니다.")
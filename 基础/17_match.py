# match只支持python3.10以上
score = int(input("请输入成绩："))
match score:
    case 90:
        print("优秀")
    case 80:
        print("良好")
    case 70:
        print("中等")
    case 60:
        print("及格")
    case _:
        print("不及格")
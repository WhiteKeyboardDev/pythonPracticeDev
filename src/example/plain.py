def hi():
    asia = {"한국", "중국", "일본"}
    asia.add("베트남")
    asia.add("중국")
    asia.remove("일본")
    asia.update(["홍콩", "한국", "태국"])
    print(asia)

if(__name__ == "__main__"):
    hi()
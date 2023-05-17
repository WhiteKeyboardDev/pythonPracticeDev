import easyocr


def init():
    # OCR 모델을 초기화합니다.
    reader = easyocr.Reader(['en'])

    # 이미지 파일 경로
    image_path = 'C:/Users/1234/Desktop/000-testData/png/1.png'

    # 이미지에서 텍스트를 추출합니다.
    result = reader.readtext(image_path)

    # 추출된 텍스트 출력
    for detection in result:
        text = detection[1]
        print(text)


if __name__ == "__main__":
    init()

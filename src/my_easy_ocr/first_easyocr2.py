import os
import easyocr
from PIL import Image, ImageDraw, ImageFont

def init():
    image_fold_path = "C:/Users/1234/Desktop/000-testData/ForEasyOCR/png/001-not_trained"
    ko_font_path = 'C:/Users/1234/Desktop/000-testData/ForEasyOCR/나눔 글꼴/나눔고딕/NanumFontSetup_TTF_GOTHIC/NanumGothic.ttf'

    reader = easyocr.Reader(['en', 'ko'], gpu=False)

    font_size = 35
    font = ImageFont.truetype(ko_font_path, font_size, encoding="UTF-8")

    for image in os.listdir(image_fold_path):
        image_path = os.path.join(image_path, image)
        if os.path.isfile(image_path):
            result = reader.readtext(image_path)
            img = Image.open(image_path)
            for r in result:
                x, y = min(list(_[0] for _ in r[0])), min(list(_[1] for _ in r[0]))
                text_data = r[1]
                d = ImageDraw.Draw(img)
                d.text((x - 15, y - 15), text_data, font=font, fill=(255, 0, 0))
            img.save(image_path + "-result.png")

if __name__ == "__main__":
    init()
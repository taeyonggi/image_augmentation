from PIL import Image


for i in range(1, 1633):
    # 이미지 불러오기
    img = Image.open("train (" + str(i) + ").jpg")

    # 회전된 이미지 회전하기
    image_90 = img.transpose(Image.ROTATE_90)
    image_180 = img.transpose(Image.ROTATE_180)
    image_270 = img.transpose(Image.ROTATE_270)
    FlipLRImage = img.transpose(Image.FLIP_LEFT_RIGHT)
    FlipTBImage = img.transpose(Image.FLIP_TOP_BOTTOM)

    # 회전된 이미지 저장하기
    image_90.save("train (" + str(i) + ")_90.jpg")
    image_180.save("train (" + str(i) + ")_180.jpg") 
    image_270.save("train (" + str(i) + ")_270.jpg")
    FlipLRImage.save("train (" + str(i) + ")_LR.jpg")
    FlipTBImage.save("train (" + str(i) + ")_TB.jpg")
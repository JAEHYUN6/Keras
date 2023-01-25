from PIL import Image
import glob

def resize_images(img_path):
    images = glob.glob(img_path + '*.jpg')
    print(len(images), ' images to be resized')
    # 파일마다 모두 28x28 사이즈로 바꾸어 저장
    target_size = (28, 28)
    for img in images:
        old_img = Image.open(img)
        new_img = old_img.resize(target_size, Image.ANTIALIAS)
        new_img.save(img, 'JPEG')
    print(len(images), ' images resized.')

image_dir_path = "./train/scissor/"
resize_images(image_dir_path)

image_dir_path = "./train/rock/"
resize_images(image_dir_path)

image_dir_path = "./train/paper/"
resize_images(image_dir_path)
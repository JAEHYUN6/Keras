from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# scissor image
image_dir_path = "./train/scissor/"
image_pil = Image.open(image_dir_path + '0.jpg')
image = np.array(image_pil)

plt.imshow(image)
plt.show()

# rock image
image_dir_path = "./train/rock/"
image_pil = Image.open(image_dir_path + '0.jpg')
image = np.array(image_pil)

plt.imshow(image)
plt.show()

# paper image
image_dir_path = "./train/paper/"
image_pil = Image.open(image_dir_path + '0.jpg')
image = np.array(image_pil)

plt.imshow(image)
plt.show()


print(image_pil.size)


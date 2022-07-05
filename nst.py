import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import PIL.Image
from datetime import datetime
import tensorflow_hub as hub

def change_image(first_file_name, second_file_name):
    mpl.rcParams["figure.figsize"] = (12, 12)
    mpl.rcParams["axes.grid"] = False

    def tensor_to_image(tensor):
        tensor = tensor * 255
        tensor = np.array(tensor, dtype=np.uint8)
        if np.ndim(tensor) > 3:
            assert tensor.shape[0] == 1
            tensor = tensor[0]
        return PIL.Image.fromarray(tensor)


    def load_img(path_to_img):
        max_dim = 512
        img = tf.io.read_file(path_to_img)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.convert_image_dtype(img, tf.float32)

        shape = tf.cast(tf.shape(img)[:-1], tf.float32)
        long_dim = max(shape)
        scale = max_dim / long_dim

        new_shape = tf.cast(shape * scale, tf.int32)

        img = tf.image.resize(img, new_shape)
        img = img[tf.newaxis, :]
        return img

    # 직접 작성되어야하는 부분
    # content_path = "./golden_gate.jpg"
    # style_path = "./starry_night.jpg"

    # 인풋 사진들어가는 경로
    content_path = 'media/'+first_file_name
    style_path = 'media/'+second_file_name

    content_image = load_img(content_path)
    style_image = load_img(style_path)


    hub_module = hub.load(
        "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1"
    )
    stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]
    tensor_to_image(stylized_image)
    result_img = tensor_to_image(stylized_image)

    user_time = datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S")
    result_img.save(user_time + ".jpg", "JPEG")
    
    print("result end")
    #출력된 파일 이름
    file_name = user_time + ".jpg"

    return file_name
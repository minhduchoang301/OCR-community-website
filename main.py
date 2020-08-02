import tensorflow as tf
from Preproccess import Preprocess
import cv2


def main(input_dir: str, model_path: str):  # , output_dir: str
    preprocess = Preprocess()
    model = tf.keras.models.load_model(model_path)
    # Lines segmenting
    lines = preprocess.crop_line_from_img(input_dir)

    # Export character images
    # line_num = 0
    paragraph = ""
    for line in lines:
        line_str = ""
        # Words segmenting
        words = preprocess.crop_word_from_line(line)
        for word in words:
            word_str = ""
            # Characters segmenting
            chars = preprocess.crop_char_from_word(word)
            for char in chars:
                char_str = model.predict(cv2.resize(char, (28, 28), interpolation=cv2.INTER_AREA))
                word_str += char_str
            line_str = line_str + " " + word_str
        paragraph = paragraph + "\n" + line_str
    return paragraph


if __name__ == '__main__':
    input_dir = input("Image path: ")
    # output_dir = input("Output path: ")
    model_path = input("Model path: ")
    main(input_dir, model_path)

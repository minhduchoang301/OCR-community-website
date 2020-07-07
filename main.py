import tensorflow as tf
from Prepoccess import Preprocess

def main(input_dir: str, output_dir: str, model_path: str):
    preprocess = Preprocess()
    model = tf.keras.models.load_model(model_path)
    # Lines segmenting
    lines = preprocess.segment_all(input_dir)
    # Words segmenting
    words = preprocess.crop_word_from_line(lines)
    # Characters segmenting 
    chars = preprocess.crop_char_from_word(words)

    # Export character images
    #line_num = 0
    paragraph = ""
    for line in chars:
        line_str =""
        for word in line:
            word_str = "" 
            for char in word:
                char_str = model.predict(cv2.resize(char, (28,28), interpolation = cv2.INTER_AREA))
                word_str += char_str
            line_str = line_str + " " + word_str
        paragraph = paragraph + "\n" + line_str
    print(paragraph)


if __name__ == '__main__':
    input_dir = input("Image path: ")
    output_dir = input("Output path: ")
    model_path = input("Model path: ")
	main(input_dir, output_dir)
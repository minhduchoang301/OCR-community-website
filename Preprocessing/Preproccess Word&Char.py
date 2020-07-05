import craft
import cv2


class Preprocess():
    """To segment words from line and or chars from word
    ====================================================
    """

    def crop_word_from_line(self, input_dir: str, line_image_name: str, output_dir: str):
        path = input_dir + "/" + line_image_name
        img = cv2.imread(path)
        bboxes, polys, heatmap = craft.detect_text(img)
        i = 0
        for i in range(len(bboxes)):
            x1 = bboxes[i][0][0]
            y1 = bboxes[i][0][1]
            x2 = bboxes[i][1][0]
            y2 = bboxes[i][1][1]
            x3 = bboxes[i][2][0]
            y3 = bboxes[i][2][1]
            x4 = bboxes[i][3][0]
            y4 = bboxes[i][3][1]

            top_left_x = int(min([x1, x2, x3, x4]))
            top_left_y = int(min([y1, y2, y3, y4]))
            bot_right_x = int(max([x1, x2, x3, x4]))
            bot_right_y = int(max([y1, y2, y3, y4]))

            letter = img[top_left_y:bot_right_y, top_left_x:bot_right_x]
            print(letter.shape)
            cv2.imwrite(output_dir +"/" + line_image_name + str(i) + ".jpg", letter)

    def crop_char_from_word(self, input_dir: str, word_image_name: str, output_dir: str):
        path = input_dir + "/" + word_image_name
        img = cv2.imread(path)
        bboxes, polys, heatmap = craft.detect_text(img)
        i = 0
        for i in range(len(bboxes)):
            x1 = bboxes[i][0][0]
            y1 = bboxes[i][0][1]
            x2 = bboxes[i][1][0]
            y2 = bboxes[i][1][1]
            x3 = bboxes[i][2][0]
            y3 = bboxes[i][2][1]
            x4 = bboxes[i][3][0]
            y4 = bboxes[i][3][1]

            top_left_x = int(min([x1, x2, x3, x4]))
            top_left_y = int(min([y1, y2, y3, y4]))
            bot_right_x = int(max([x1, x2, x3, x4]))
            bot_right_y = int(max([y1, y2, y3, y4]))

            letter = img[top_left_y:bot_right_y, top_left_x:bot_right_x]
            print(letter.shape)
            cv2.imwrite(output_dir +"/" + word_image_name + str(i) + ".jpg", letter)

import os
import cv2


def main(image_list, save_list, image_dir="/home/projects/competition_orange/data/phase1"):
    """
    改变bbox矩形框的格式
    """
    with open(image_list, 'r') as fr, open(save_list, 'w') as fw:
        lines = fr.readlines()
        for i,item in enumerate(lines):
            print("{} / {}".format(str(i), str(len(lines))))
            parts = item.strip().split(" ")
            if not len(parts) % 5 == 1:
                print("item length error: {}".format(item))
            
            # 确定bbox的数目
            bbox_num = int((len(parts) - 1) // 5)

            # 读取图片
            image_path = os.path.join(image_dir, parts[0])
            img = cv2.imread(image_path)
            h, w = img.shape[:2]

            # 画出每一个框
            for i in range(bbox_num):
                label = parts[1+i*5]
                bbox = parts[2+i*5: 6+i*5]
                bbox = [float(x) for x in bbox]
                
                # 把相对坐标换成绝对的
                # 原始坐标是：中间x，中间y，宽度，高度
                mid_x = int(w * bbox[0])
                mid_y = int(h * bbox[1])
                x1 = mid_x - int(w * bbox[2] / 2)
                y1 = mid_y - int(h * bbox[3] / 2)
                x2 = mid_x + int(w * bbox[2] / 2)
                y2 = mid_y + int(h * bbox[3] / 2)

                new_bbox = [x1, y1, x2, y2]
                new_bbox = [str(x) for x in new_bbox]
                fw.writelines(parts[0].split("/")[-1] + " " + label + " " + " ".join(new_bbox) + "\n")
    return




if __name__ == "__main__":

    image_list = "/home/projects/competition_orange/data/list/test_list.txt"
    save_list = "/home/projects/competition_orange/data/list/annos_test.txt"
    main(image_list, save_list)

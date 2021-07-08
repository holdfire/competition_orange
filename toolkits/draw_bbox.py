import os
import cv2


def draw(item, save_path, image_dir="/home/projects/orange/data/phase1"):
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

        # print(image_path, x1, y1, x2, y2)
        # print(h, w)
        # exit(0)

        # 确定矩形框的两个点
        pt1 = (x1, y1)
        pt2 = (x2, y2)

        # 根据标签画出不同颜色的框
        if label == "0":
            img = cv2.rectangle(img, pt1, pt2, (255,0,0), 2)
        elif label == "1":
            img = cv2.rectangle(img, pt1, pt2, (0,255,0), 2)
        elif label == "2":
            img = cv2.rectangle(img, pt1, pt2, (0,0,255), 2)
        else:
            print("image label error!")

    # 保存图片
    cv2.imwrite(save_path, img)
    return


def batch_draw(image_list, save_dir, sup=100):
    """
    批量画出上面的框
    """
    with open(image_list, 'r') as fr:
        lines = fr.readlines()
        for i in range(sup):
            item = lines[i]
            image_name = item.split(" ")[0].split("/")[-1]
            save_path = os.path.join(save_dir, image_name)
            draw(item, save_path)  
            print(i, "  "+save_path) 
    return




if __name__ == "__main__":

    image_list = "/home/projects/orange/data/list/train_list.txt"
    save_dir = "/home/projects/orange/data/image_bbox"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    batch_draw(image_list, save_dir)

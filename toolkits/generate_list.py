import os
import glob


def generate_path_label(image_dir, label_dir, dst_file):

    # 第一步生成所有的图片的路径
    image_paths = glob.glob(image_dir + "/*[jpg,JPG]")
    print(len(image_paths))

    # 记录每个图有多少个框
    counts = {}

    # 第二步找到对应的label文件
    with open(dst_file, 'w') as fw:
        for i, image_path in enumerate(image_paths):
            label_name = image_path.split("/")[-1].split(".")[0] + ".txt"
            label_path = os.path.join(label_dir, label_name)

            # 只写图片路径名
            # fw.writelines(image_path.split("phase1/")[1] + "\n")

           
            # 写图片路径和label
            with open(label_path, 'r') as fr:
                lines = fr.readlines()
                label = " ".join([line.strip() for line in lines])
                fw.writelines(image_path.split("phase1/")[1] +  " " + label + "\n")

                # 统计每个图片有多少个框
                if str(len(lines)) not in counts:
                    counts[str(len(lines))] = 1
                else:
                    counts[str(len(lines))] += 1
    x = []
    y = []
    for key in sorted([int(x) for x in counts.keys()]):
        x.append(key)
        y.append(counts[str(key)])
    print(x)
    print(y)

    return



if __name__ == "__main__":

    image_dir = "/home/projects/orange/data/phase1/train/images/"
    label_dir = "/home/projects/orange/data/phase1/train/labels/"
    dst_file = "/home/projects/orange/data/list/train_list.txt"
    if not os.path.exists(os.path.dirname(dst_file)):
        os.makedirs(os.path.dirname(dst_file))
    generate_path_label(image_dir, label_dir, dst_file)

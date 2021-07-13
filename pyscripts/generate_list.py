import os
import glob


def generate_path_label(image_dir, label_dir, dst_file):

    # 第一步生成所有的图片的路径
    image_paths = glob.glob(image_dir + "/*[jpg,JPG]")
    # print(len(image_paths))

    # 记录每个图有多少个框
    counts = {}
    catgory = {"0":0, "1":0, "2":0}
    # 记录长宽比
    ratio_dict = {}
    # 记录宽度
    width_dict = {}

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

                # 在原始标注文件的每一行
                for line in lines:
                    # 统计每个类别的样本数目
                    catgory[line.split(" ")[0]] += 1

                    # 统计长宽比
                    ratio = float(line.split(" ")[3]) / float(line.split(" ")[4])
                    if ratio >= 2:
                        ratio = int(ratio)
                    else:
                        ratio = int(ratio * 10) / 10
                        ratio = round(ratio, 1)
                    # 保存
                    if ratio in ratio_dict:
                        ratio_dict[ratio] += 1
                    else:
                        ratio_dict[ratio] = 1

                    # 统计宽度
                    width = float(line.split(" ")[3])
                    width = round(width, 1)
                    if width in width_dict:
                        width_dict[width] += 1
                    else:
                        width_dict[width] = 1


    # 展示框的数目：图片数
    x = []
    y = []
    for key in sorted([int(x) for x in counts.keys()]):
        x.append(key)
        y.append(counts[str(key)])
    print(x)
    print(y)
    print(catgory)

    # 展示长宽比
    x = []
    y = []
    for key in sorted([x for x in ratio_dict.keys()]):

        x.append(key)
        y.append(ratio_dict[key])
    print(x)
    print(y)
    print(ratio_dict)

    # 展示宽度
    x = []
    y = []
    for key in sorted([x for x in width_dict.keys()]):
        x.append(key)
        y.append(width_dict[key])
    print(x)
    print(y)
    print(width_dict)

    return



def generate_test(src_dir, dst_file):
    image_paths = glob.glob(src_dir + "/*[jpg,JPG]")
    with open(dst_file, 'w') as fw:
        for i, image_path in enumerate(image_paths):
            fw.writelines(image_path.split("phase1/")[1] + " 0 0.5 0.5 0.2 0.2\n")
    return






if __name__ == "__main__":

    # image_dir = "/home/projects/competition_orange/data/phase1/train/images/"
    # label_dir = "/home/projects/competition_orange/data/phase1/train/labels/"
    # dst_file = "/home/projects/competition_orange/data/list/train_list.txt"
    # if not os.path.exists(os.path.dirname(dst_file)):
    #     os.makedirs(os.path.dirname(dst_file))
    # generate_path_label(image_dir, label_dir, dst_file)


    src_dir = "/home/projects/competition_orange/data/phase1/test/images/"
    dst_file = "/home/projects/competition_orange/data/list/test_list.txt"
    generate_test(src_dir, dst_file)
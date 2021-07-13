import pickle

src_file = "./result/val_result/out.pkl"

content = pickle.load(open(src_file, 'rb'))
print(type(content))
print(content[1])
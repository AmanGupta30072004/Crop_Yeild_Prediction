import pickle
file_path="D:\idse\projects\Crop Yield Prediction\model.pkl"
with open (file_path,"rb") as reader:
    data=pickle.load(reader)
    print(data)
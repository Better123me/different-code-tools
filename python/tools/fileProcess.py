# 获得所有待处理的文件路径列表， 可以指定后缀
def getImgPathList(dirPath:str)->list:
    tif_files = []
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            if file.endswith('.tif'):
                full_path = os.path.join(root, file)
                tif_files.append(full_path)
    return tif_files



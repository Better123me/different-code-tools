# 对列表按规则排序
maskPaths = sorted(maskPaths, key=lambda x: int(x.split('.')[0].split("\\")[-1]))
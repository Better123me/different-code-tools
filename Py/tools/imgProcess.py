# tif格式文件######################################################################################
import skimage.io as io

# 根据路径读取图片文件， 在调用前保证路径文件存在
def readFromPath(path):
    return io.imread(path).astype(float)

# 保存文件
def save(self):
    newfileName = r"E:\Project_CSC\dataSet\DenoisedImg\\" + self.category.value() + self.order + ".tif"
    tifffile.imwrite(newfileName, self.img)



##############################################################################################
# 图像处理
    
# 高斯算法去噪
def denoise_Guass(self, kernelSize):
    self.img = cv2.GaussianBlur(self.img, (kernelSize, kernelSize), 0)


from scipy.ndimage import median_filter
# 中值滤波去噪
def denoise_Median(self, kernelSize):
    self.img = median_filter(self.img, kernelSize)


# 获得图像最亮点的坐标
def getMaxBrightnessCord(self, img):
    max_index = np.unravel_index(np.argmax(img), img.shape)
    return [max_index[0], max_index[1]]


# 获得图像重心x, y坐标
def getImgGravity(self, img):
    max_pixel_value = np.max(img)
    normalized_img = img.astype(float) / max_pixel_value

    rows, cols = img.shape
    row_indices, col_indices = np.indices((rows, cols))
    weighted_row_indices = row_indices * normalized_img
    weighted_col_indices = col_indices * normalized_img

    total_sum = np.sum(normalized_img)
    center_of_mass_row = int(np.sum(weighted_row_indices) / total_sum)
    center_of_mass_col = int(np.sum(weighted_col_indices) / total_sum)
    return [center_of_mass_row, center_of_mass_col]

# 获得图片全局平均亮度
def getAverageBrightness(self, img):
    global_brightness = np.mean(img)
    return global_brightness

# 对图片进行阈值化处理_hard      高于阈值取像素最大值，低于阈值取0
def hard_thresholding(self, threshold):
    p_max = np.max(self.img)
    self.thresholdImg = np.where(self.img > threshold, p_max, 0)

# soft阈值化处理          高于阈值的部分不变，低于的部分变成0
def soft_thresholding(self, threshold):
    self.thresholdImg = np.where(self.img > threshold, self.img, 0)

# softadjust 高于的部分减去阈值，低于的部分变成0
def softAdjust_thresholding(self, threshold):
    self.thresholdImg = np.where(self.img > threshold, self.img - threshold, 0)


# 对图像进行掩膜运算
mask = self.readImg(maskPath)
maskedImg = np.copy(self.img)
maskedImg[mask != 255] = 0

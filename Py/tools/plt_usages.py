# 1.plt 显示图片并加上颜色棒

def show(self, title:str=""):
    if title:
        plt.title(title)
    plt.imshow(self.img.T, origin='lower', aspect='auto', vmin=np.median(self.img),vmax=np.percentile(self.img,99.9))  # 使用'viridis'颜色映射，并自动调整纵横比
    plt.colorbar()  
    plt.show()
#######################################################################################
# 绘制折线图，并一表多线

def showAnalysis(self, x_label = "", y_label="", title=""):
    # 获取x, y1, y2, y3
    y_minBr = np.min(self.img, axis=0)
    y_avgBr = np.mean(self.img, axis=0)
    y_maxBr = np.max(self.img, axis=0)
    x = np.arange(len(y_minBr))
    # 保证所有的特征值都已计算
    self.getAllFeatures()

    # 设置坐标轴样式
    x_label = "image_x" if x_label == "" else x_label
    y_label = "image_AV/min/max_Br of x direction" if y_label == "" else y_label
    title = "here is your title"

    plt.figure(figsize=(8, 6))  # 设置图像大小
    plt.plot(x, y_minBr, label='min_Br', color='blue')  # 绘制亮度总和曲线
    plt.plot(x, y_avgBr, label='mean_Br', color='red')  # 绘制平均亮度曲线
    plt.plot(x, y_maxBr, label='max_Br', color='green')  # 绘制最大亮度曲线
    plt.xlabel(x_label)  # 设置 x 轴标题
    plt.ylabel(y_label)  # 设置 y 轴标题
    plt.title(title)  # 设置图表标题
    plt.legend(loc='upper right')  # 显示曲线和颜色对应值
    plt.grid(False)  # 添加网格线
    plt.show()
#######################################################################################
    # 绘制图片，并在图上标注点
def show(self, title: str = ""):
    if title:
        plt.title(title)

    # imshow使用的是行列解析，而矩阵是列行模式
    plt.imshow(self.img.T, origin='lower', aspect='auto', vmin=np.median(self.img),
                vmax=np.percentile(self.img, 99.9))

    plt.colorbar()
    # 在图像上添加两个点
    plt.scatter(x=self.features["cord_maxBrightness"][0], y=self.features["cord_maxBrightness"][1],color='red', edgecolor='red', marker='o', facecolors='none')
    plt.text(self.features["cord_maxBrightness"][0], self.features["cord_maxBrightness"][1], 'maxBrightness', color='red',
                fontsize=8, ha='left', va='top')

    plt.scatter(x=self.features["cord_gravity"][0], y=self.features["cord_gravity"][1],color='yellow', edgecolor='yellow', marker='o', facecolors='none')
    plt.text(self.features["cord_gravity"][0], self.features["cord_gravity"][1], 'COG', color='yellow',
                fontsize=8, ha='left', va='top')

    plt.show()

#######################################################################################
def plotLineChart(self, x_data, y_data, title=None, x_label=None, y_label=None, savePath=None):
    plt.plot(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    if savePath:
        plt.savefig(savePath)

# 一张图上画多个子表
def plot_multiple_charts(self, save_path=None):
        x = self.utils.data['img_id']
        x_label = "Image Index/shot number"
        featureList = ["AV_Br", "max_x", "max_y", "COG_x", "COG_y", "A_O_B"]
        yListName = ["avgBrightness", "cord_maxBright_x", "cord_maxBright_y",
                     "cord_gravity_x", "cord_gravity_y", "ratio_bright"]
        y_data = []
        for name in yListName:
            y_data.append(self.utils.data[name])

        fig, axs = plt.subplots(2, 3, figsize=(14, 8))
        for i in range(2):
            for j in range(3):
                y = y_data[i * 3 + j]
                x_label = x_label
                y_label = self.category + " " + featureList[i * 3 + j]
                ax = axs[i, j]
                ax.plot(x, y)
                ax.set_xlabel(x_label)
                ax.set_ylabel(y_label)
                ax.set_title(y_label + "VS shot number")
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)

        plt.show()


# 保存表格图像
plt.savefig(name)
plt.close()

# 根据保存的图像合并成大图-多图合并
def merge_plots(self, filenames, size, titles):
    rows, cols = size
    fig, axs = plt.subplots(rows, cols, figsize=(cols * 5, rows * 5))
    for ax, filename, title in zip(axs.flatten(), filenames, titles):
        image = plt.imread(filename)
        ax.imshow(image)
        ax.axis('off')  # 关闭坐标轴
        ax.set_title(title)

    plt.tight_layout()  # 调整子图布局，以防重叠
    plt.show()
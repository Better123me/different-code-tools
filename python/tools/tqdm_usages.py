from tqdm import tqdm
import time

x = range(10)
for i in tqdm(x, desc='this is a desc in line'):
    time.sleep(0.5)
    # 如果需要提前更新进度条，我们使用tqdm.update()
    # tqdm.update()

# 手动更新方法
with tqdm(total=len(x)) as pbar:
    for item in x:
        # 在这里执行任务
        time.sleep(1)  # 模拟任务执行时间
        pbar.update(1)  # 更新进度条的完成量
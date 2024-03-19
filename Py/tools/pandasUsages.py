
# 去除指定特征列名的列
columns_to_drop = [col for col in concatenated_df.columns if 'id' in col.lower() and col.lower() != 'all_id']
concatenated_df.drop(columns=columns_to_drop, inplace=True)

# 重命名列名
column_names = filtered_df.columns
new_column_names = [tname + "_" + col_name for col_name in column_names]
filtered_df.columns = new_column_names


# 筛选出符合特征组要求的列
# select xx with a > b and c < d这种
filtered_df = df[(df['thresholdSrc'] == thresholdSrc) & (df['thresholdMethod'] == method)]

# 清空整个df
def clear_dataframe(df):
    cleared_df = df.drop(df.index, axis=0).drop(df.columns, axis=1)
    return cleared_df


# 计算两张表之间数据的相关性
from scipy.stats import pearsonr
def calculate_correlation(df1, df2, k):
    correlated_columns = []
    for col1 in df1.columns:
        for col2 in df2.columns:
            correlation, _ = pearsonr(df1[col1], df2[col2])
            if abs(correlation) > k:
                correlated_columns.append((col1, col2, correlation))
    return correlated_columns


# 获得一张表中特定两列所有按行匹配的数据，并根据某一列的元素的值重新排列
def getCoupleDate(self, col1Name, col2Name):
    col1 = self.data[col1Name]
    col2 = self.data[col2Name]
    unique_pairs = set(zip(col1, col2))
    sorted_pairs = sorted(unique_pairs, key=lambda pair: pair[0])
    x_list, y_list = zip(*sorted_pairs)
    return x_list, y_list
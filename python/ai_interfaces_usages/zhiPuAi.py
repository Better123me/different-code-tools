from zhipuai import ZhipuAI


def Ask(text):
    """
    使用智谱AI的chatAPI来回答一个问题。
    参数:
        - question: 字符串，用户的提问。
    返回:
        - response_text: 字符串，智谱AI的回答。
    """
    # 替换为您的API密钥
    api_key = ""
    # 创建ZhipuAI客户端实例
    client = ZhipuAI(api_key=api_key)
    # 设置模型的名称
    model = "glm-4"
    if text:
        messages = [
            {"role": "user", "content": text}
        ]
        # 发起API请求
        response = client.chat.completions.create(model=model, messages=messages)
        # 从响应中获取回答内容
        response_text = response.choices[0].message.content
        return response_text
    return -1


if __name__ == "__main__":
    s=input("请输入问题：")
    answer = Ask(s)
    print(answer)

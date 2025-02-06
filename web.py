import gradio as gr
import requests

#claude API配置
API_KEY = "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"
URL = "https://api.anthropic.com/v1/messages"
HEADERS = {
    "x-api-key":API_KEY,
    "anthropic-version":"2023-06-01",
    "Content-Type":"application/json"
}

#聊天函数
def chat_with_claude(message):
    data = {
        "model": "claude-3-haiku-20240307",
        "messages": [{"role": "user", "content": message}],
        "max_tokens": 500
    }
    response = requests.post(URL, headers=HEADERS, json=data)

    if response.status_code == 200:
        return response.json()["content"]

        #提取“text”部分
        text_response = result["choices"][0]["text"]
        print(text_response)
    else:
        return f"❌ 请求失败: {response.status_code}, {response.json()}"



#存储对话历史
def chat_with_claude(message):
    global chat_history
    chat_history.append({"role":"user","content":message}) #记录用户输入

    data = {
        "model": "claude-3-haiku-20240307",
        "messages": chat_history,  #让Claude看到所有对话历史
        "max_tokens": 500
    }
    response = requests.post(URL, headers=HEADERS, json=data)

    if response.status_code == 200:
        response_text = response.json()["content"]
        chat_history.append({"role":"user","content":response_text})  #记录Claude回复
        return response_text
    else:
        return f"❌ 请求失败: {response.status_code}, {response.json()}"


# 创建 Gradio Web 界面
chat_ui = gr.Interface(
    fn=chat_with_claude,
    inputs="text",
    outputs="text",
    title="菲菲菲菲常聪明的Chatbot",
    description="与小菲侠进行对话"
)

chat_ui.launch()

#运行Web界面
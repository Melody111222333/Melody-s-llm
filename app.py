from fastapi import FastAPI
import requests
from pydantic import BaseModel

# Claude API 配置
API_KEY = "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"
URL = "https://api.anthropic.com/v1/messages"
HEADERS = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "Content-Type": "application/json"
}

# 创建 FastAPI 实例
app = FastAPI()

# 定义请求数据格式
class ChatRequest(BaseModel):
    message: str

# API 端点：处理聊天请求
@app.post("/chat")
async def chat(request: ChatRequest):
    data = {
        "model": "claude-3-haiku-20240307",  # 你可以改为更强的模型
        "messages": [{"role": "user", "content": request.message}],
        "max_tokens": 500
    }
    response = requests.post(URL, headers=HEADERS, json=data)

    if response.status_code == 200:
        return {"response": response.json()["content"]}
    else:
        return {"error": response.json()}

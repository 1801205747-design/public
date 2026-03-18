# deepseek_chatbot_official.py
import os
import requests
import json
from typing import Optional

class DeepSeekChatbot:
    def __init__(self, api_key: str, base_url: str = "https://api.deepseek.com"):
        """
        初始化DeepSeek聊天机器人
        
        参数:
            api_key: DeepSeek API密钥
            base_url: API基础URL，默认为官方API地址
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def chat(self, message: str, model: str = "deepseek-chat") -> str:
        """
        发送消息给DeepSeek模型并获取回复
        
        参数:
            message: 用户输入的问题
            model: 使用的模型，默认为deepseek-chat
            
        返回:
            model_response: 模型的回复文本
        """
        # 构建请求数据
        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": message}
            ],
            "stream": False,
            "max_tokens": 2048
        }
        
        try:
            # 发送POST请求到聊天接口
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=data,
                timeout=30
            )
            
            # 检查响应状态
            response.raise_for_status()
            
            # 解析响应
            result = response.json()
            
            # 提取回复内容
            if "choices" in result and len(result["choices"]) > 0:
                model_response = result["choices"][0]["message"]["content"]
                return model_response
            else:
                return "错误：未收到有效回复"
                
        except requests.exceptions.RequestException as e:
            return f"网络请求错误: {str(e)}"
        except json.JSONDecodeError as e:
            return f"JSON解析错误: {str(e)}"
        except Exception as e:
            return f"未知错误: {str(e)}"
    
    def interactive_chat(self):
        """交互式聊天模式"""
        print("=" * 50)
        print("DeepSeek Chatbot 已启动！")
        print("输入 'quit' 或 'exit' 退出程序")
        print("=" * 50)
        
        while True:
            try:
                # 获取用户输入
                user_input = input("\n你: ").strip()
                
                # 检查退出条件
                if user_input.lower() in ['quit', 'exit', '退出']:
                    print("\n再见！")
                    break
                
                if not user_input:
                    print("提示：请输入有效的问题")
                    continue
                
                # 显示思考中提示
                print("AI思考中...", end="", flush=True)
                
                # 调用模型
                response = self.chat(user_input)
                
                # 清空"思考中"提示
                print("\r" + " " * 20 + "\r", end="")
                
                # 打印回复
                print(f"DeepSeek: {response}")
                
            except KeyboardInterrupt:
                print("\n\n程序被用户中断")
                break
            except Exception as e:
                print(f"\n发生错误: {str(e)}")

# 主程序
def main():
    # 从环境变量获取API密钥
    api_key = os.getenv("DEEPSEEK_API_KEY")
    
    if not api_key:
        # 如果环境变量不存在，提示用户输入
        print("=" * 50)
        print("DeepSeek API密钥配置")
        print("=" * 50)
        print("您可以在 https://platform.deepseek.com/api_keys 获取API密钥")
        api_key = input("请输入您的DeepSeek API密钥: ").strip()
        
        if not api_key:
            print("错误：API密钥不能为空")
            return
    
    # 创建聊天机器人实例
    chatbot = DeepSeekChatbot(api_key)
    
    # 运行交互式聊天
    chatbot.interactive_chat()

if __name__ == "__main__":
    main()
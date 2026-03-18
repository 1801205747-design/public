# simple_example.py
import os
from deepseek_chatbot_official import DeepSeekChatbot

def simple_example():
    # 方法1：通过环境变量设置API密钥
    # 在终端执行: export DEEPSEEK_API_KEY="your-api-key"
    api_key = os.getenv("DEEPSEEK_API_KEY")
    
    # 方法2：直接设置（仅用于测试，生产环境请使用环境变量）
    if not api_key:
        api_key = "sk-your-api-key-here"  # 替换为您的API密钥
    
    # 创建聊天机器人
    chatbot = DeepSeekChatbot(api_key)
    
    # 测试问题
    test_questions = [
        "你好，请简单介绍一下自己",
        "Python是什么？",
        "如何学习编程？"
    ]
    
    print("DeepSeek Chatbot 测试开始：")
    print("-" * 40)
    
    for question in test_questions:
        print(f"\n问题: {question}")
        response = chatbot.chat(question)
        print(f"回答: {response}")
        print("-" * 40)

if __name__ == "__main__":
    simple_example()
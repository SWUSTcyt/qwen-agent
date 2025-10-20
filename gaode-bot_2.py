import os
from qwen_agent.agents import Assistant
from qwen_agent.gui import WebUI
from dotenv import load_dotenv
load_dotenv()

# LLM 配置
llm_cfg = {
    "model": "qwen-plus-latest",
    "model_server": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx"
    "api_key": os.getenv("DASHSCOPE_API_KEY"),
}

# 系统消息
system = "你是会天气查询、地图查询、网页部署的助手"

# 工具列表
tools = [
    {
        "mcpServers": {
            "amap-maps": {
                "type": "sse",
                "url": os.getenv("AMAP_MAPS_MCP_URL"),
            },
            "edgeone-pages-mcp": {
                "type": "sse",
                "url": os.getenv("EDGEONE_PAGES_MCP_URL"),
            },
        }
    }
]

# 创建助手实例
bot = Assistant(
    llm=llm_cfg,
    name="助手",
    description="高德地图、天气查询、公网链接部署",
    system_message=system,
    function_list=tools,
)

def app_gui():
    """Web图形界面模式
    
    提供 Web 图形界面，特点：
    - 友好的用户界面
    - 预设查询建议
    - 支持地图查询、天气查询、网页部署等功能
    """
    try:
        print("正在启动 Web 界面...")
        # 配置聊天界面
        chatbot_config = {
            'prompt.suggestions': [
                '帮我查询北京今天的天气',
                '查找上海东方明珠的位置',
                '规划从北京到上海的路线',
                '部署一个简单的网页到公网',
                '搜索附近的停车场',
                '推荐陆家嘴附近的高档餐厅'
            ]
        }
        
        print("Web 界面准备就绪，正在启动服务...")
        # 启动 Web 界面
        WebUI(
            bot,
            chatbot_config=chatbot_config
        ).run()
    except Exception as e:
        print(f"启动 Web 界面失败: {str(e)}")
        print("请检查网络连接和 API Key 配置")

def app_tui():
    """终端交互模式（原有的命令行交互）"""
    messages = []
    
    while True:
        query = input("\nuser question: ")
        if not query.strip():
            print("user question cannot be empty！")
            continue
        messages.append({"role": "user", "content": query})
        bot_response = ""
        is_tool_call = False
        tool_call_info = {}
        for response_chunk in bot.run(messages):
            new_response = response_chunk[-1]
            if "function_call" in new_response:
                is_tool_call = True
                tool_call_info = new_response["function_call"]
            elif "function_call" not in new_response and is_tool_call:
                is_tool_call = False
                print("\n" + "=" * 20)
                print("工具调用信息：", tool_call_info)
                print("工具调用结果：", new_response)
                print("=" * 20)
            elif new_response.get("role") == "assistant" and "content" in new_response:
                incremental_content = new_response["content"][len(bot_response):]
                print(incremental_content, end="", flush=True)
                bot_response += incremental_content
        messages.extend(response_chunk)

if __name__ == '__main__':
    print("=" * 50)
    print("欢迎使用高德地图智能助手！")
    print("=" * 50)
    print("请选择运行模式：")
    print("1. Web界面模式（推荐）- 现代化的图形界面")
    print("2. 命令行模式 - 传统的终端交互")
    print("=" * 50)
    
    while True:
        choice = input("请输入选择 (1/2): ").strip()
        
        if choice == "1":
            print("正在启动Web界面模式...")
            app_gui()
            break
        elif choice == "2":
            print("正在启动命令行模式...")
            app_tui()
            break
        else:
            print("无效选择，请输入 1 或 2")
            continue
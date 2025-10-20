# 高德地图智能助手

基于 Qwen Agent 框架开发的多功能智能助手，集成了高德地图API、天气查询和网页部署功能。

## ✨ 功能特性

- 🗺️ **地图查询**: 地点搜索、路线规划、POI查询
- 🌤️ **天气查询**: 实时天气信息获取
- 🌐 **网页部署**: 一键部署网页到公网
- 💬 **多种交互**: 支持Web界面和命令行两种模式
- 🔄 **流式输出**: 实时响应，提升用户体验
- 🛠️ **工具集成**: 基于MCP协议的模块化工具系统

## 🚀 快速开始

### 环境要求

- Python 3.8+
- 阿里云DashScope API Key
- 高德地图MCP服务URL
- EdgeOne页面部署MCP服务URL

### 安装步骤

1. **克隆项目**
```bash
git clone <your-repo-url>
cd mcp-a2a
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **配置环境变量**
```bash
# 复制环境变量模板
cp .example.env .env

# 编辑 .env 文件，填入您的API密钥
# DASHSCOPE_API_KEY=your_api_key
# AMAP_MAPS_MCP_URL=your_amap_url
# EDGEONE_PAGES_MCP_URL=your_edgeone_url
```

4. **运行程序**
```bash
python gaode-bot_2.py
```

## 📖 使用说明

### 运行模式

程序启动后，您可以选择两种交互模式：

#### 1. Web界面模式（推荐）
- 现代化的图形界面
- 预设查询建议
- 支持连续对话
- 实时响应显示

#### 2. 命令行模式
- 传统的终端交互
- 流式输出效果
- 工具调用可视化
- 适合开发者使用

### 预设查询建议

Web界面提供以下预设查询模板：

- 🌤️ "帮我查询北京今天的天气"
- 🏢 "查找上海东方明珠的位置"
- 🗺️ "规划从北京到上海的路线"
- 🌐 "部署一个简单的网页到公网"
- 🅿️ "搜索附近的停车场"
- 🍽️ "推荐陆家嘴附近的高档餐厅"

## 🔧 配置说明

### 环境变量

| 变量名 | 说明 | 获取地址 |
|--------|------|----------|
| `DASHSCOPE_API_KEY` | 阿里云DashScope API密钥 | [DashScope控制台](https://dashscope.console.aliyun.com/) |
| `AMAP_MAPS_MCP_URL` | 高德地图MCP服务URL | [ModelScope MCP](https://mcp.api-inference.modelscope.net/) |
| `EDGEONE_PAGES_MCP_URL` | EdgeOne页面部署MCP服务URL | [ModelScope MCP](https://mcp.api-inference.modelscope.net/) |

### 工具配置

项目使用MCP (Model Context Protocol) 协议集成外部工具：

- **amap-maps**: 高德地图核心服务
- **edgeone-pages-mcp**: 网页部署服务

## 📁 项目结构

```
mcp-a2a/
├── gaode-bot_2.py          # 主程序文件
├── assistant_bot.py         # 完整功能版本
├── gaode-bot.py            # 原始简单版本
├── requirements.txt        # 依赖文件
├── .example.env           # 环境变量模板
├── .gitignore            # Git忽略文件
└── README.md             # 项目文档
```

## 🛠️ 开发说明

### 代码结构

- **模块化设计**: 功能分离，易于维护
- **错误处理**: 完善的异常处理机制
- **类型提示**: 使用Python类型注解
- **文档完善**: 详细的函数和模块说明

### 扩展功能

您可以轻松扩展新的功能：

1. 在 `tools` 配置中添加新的MCP服务
2. 在 `chatbot_config` 中添加新的预设建议
3. 创建新的交互模式函数

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- [Qwen Agent](https://github.com/QwenLM/Qwen-Agent) - 核心框架
- [阿里云DashScope](https://dashscope.console.aliyun.com/) - LLM服务
- [高德地图](https://lbs.amap.com/) - 地图服务
- [ModelScope](https://mcp.api-inference.modelscope.net/) - MCP服务

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 [Issue](https://github.com/your-username/mcp-a2a/issues)
- 发送邮件至 your-email@example.com

---

⭐ 如果这个项目对您有帮助，请给它一个星标！

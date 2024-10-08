# AI 教育应用

这个项目是一个 AI 教育应用的基础框架。目前已经实现了用户注册和登录功能，以及首页的简单静态设计。

## 当前完成的工作

1. 用户注册功能

   - 允许用户创建新账户
   - 用户信息（用户名、邮箱、密码）存储在 users.txt 文件中
   - 注册时会检查用户名是否已存在

2. 用户登录功能

   - 支持使用用户名或邮箱登录
   - 登录成功后会将用户信息存储在本地存储中
   - 登录状态会影响页面显示（如显示用户名、登出按钮等）

3. 页面设计

   - 创建了基本的静态页面布局
   - 包含导航栏、hero 区域和其他内容区块
   - 所有页面使用统一的背景图片
   - 首页添加了 AI 教育场景轮播图展示

4. 后端服务器

   - 使用 Flask 框架搭建
   - 实现了注册和登录的 API 端点
   - 添加了 CORS 支持，允许前端页面访问 API

5. 前端交互

   - 使用原生 JavaScript 实现前后端交互
   - 表单提交和数据验证
   - 登录状态管理
   - 实现了 AI 教育场景轮播图功能

## 待完成工作

1. 实现具体的 AI 教育功能
2. 改进用户认证系统，增加安全性
3. 优化用户界面和用户体验
4. 添加更多的教育相关内容和功能

## 技术栈

- 后端：Python (Flask)
- 前端：HTML, CSS, JavaScript
- 数据存储：暂时使用文本文件 (users.txt)
- 轮播图：Swiper.js

## 如何运行

1. 确保已安装 Python 和 Flask
2. 运行 `python server.py` 启动后端服务器
3. 在浏览器中打开 index.html 文件

注意：这个项目目前还处于开发阶段，仅用于学习和测试目的。在实际部署时，需要考虑更多的安全性和性能优化措施。

## 最近更新

- 更新了所有页面的背景图片，使用了统一的图片资源
- 在首页添加了 AI 教育场景轮播图，展示智能批改作业、自动推荐学习路径和情绪识别辅助教学等功能

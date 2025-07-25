# 贪吃蛇游戏 PWA

一个功能完整的渐进式网页应用（PWA）贪吃蛇游戏，支持离线运行和主屏幕安装。

## 🎮 特性

- **全屏游戏体验** - 充分利用屏幕空间
- **5档速度调节** - 从最慢到最快，满足不同玩家需求
- **多种食物类型** - 苹果、鸡蛋、老鼠、虫子，随机出现
- **可爱的蛇头设计** - 黄色蛇头，始终正向显示
- **微信浏览器优化** - 完美适配微信内置浏览器
- **PWA功能** - 支持离线运行、主屏幕安装、推送通知
- **响应式设计** - 适配各种移动设备

## 📁 文件结构

```
PWA/
├── snake_mobile_wechat_fullscreen_pwa.html  # 主游戏文件
├── manifest.json                            # PWA配置文件
├── sw.js                                   # Service Worker
├── create_pwa_icons.py                     # 图标生成脚本
├── icons/                                  # 应用图标目录
│   ├── icon-16x16.png
│   ├── icon-32x32.png
│   ├── icon-48x48.png
│   ├── icon-72x72.png
│   ├── icon-96x96.png
│   ├── icon-128x128.png
│   ├── icon-144x144.png
│   ├── icon-152x152.png
│   ├── icon-167x167.png
│   ├── icon-180x180.png
│   ├── icon-192x192.png
│   ├── icon-256x256.png
│   ├── icon-384x384.png
│   └── icon-512x512.png
├── PWA使用说明.txt                         # 详细使用说明
└── README.md                               # 项目说明
```

## 🚀 快速开始

### 1. 本地测试

```bash
# 使用Python启动本地服务器
python -m http.server 8000

# 访问 http://localhost:8000/snake_mobile_wechat_fullscreen_pwa.html
```

### 2. 部署到GitHub Pages

1. 创建GitHub仓库
2. 上传所有PWA文件
3. 启用GitHub Pages服务
4. 访问 `https://用户名.github.io/仓库名/snake_mobile_wechat_fullscreen_pwa.html`

### 3. 安装到主屏幕

#### iOS (Safari)
1. 用Safari打开游戏网址
2. 点击底部分享按钮
3. 选择"添加到主屏幕"
4. 确认安装

#### Android (Chrome)
1. 用Chrome打开游戏网址
2. 点击右上角菜单
3. 选择"添加到主屏幕"
4. 确认安装

## 🎯 游戏特性

### 游戏机制
- 蛇可以在全屏范围内移动
- 食物只在可见区域内生成（避免被方向键遮挡）
- 5档速度选择：最慢、慢、正常、快、最快
- 多种食物类型随机出现

### 视觉设计
- 绿色游戏背景
- 黄色蛇头和蛇身
- 彩色食物（红色苹果、白色鸡蛋、白色老鼠、蓝色虫子）
- 圆润的按钮设计
- 现代化的UI界面

### 技术优化
- 微信浏览器特殊优化
- 防止页面滚动和缩放
- 触摸事件优化
- 全屏显示适配
- 响应式设计

## 🔧 技术栈

- **HTML5** - 页面结构
- **CSS3** - 样式和动画
- **JavaScript** - 游戏逻辑
- **Canvas API** - 游戏渲染
- **Service Worker** - 离线缓存
- **Web App Manifest** - PWA配置

## 📱 兼容性

| 浏览器 | 支持状态 |
|--------|----------|
| Chrome (Android/iOS) | ✅ 完全支持 |
| Safari (iOS) | ✅ 完全支持 |
| Firefox (Android) | ✅ 完全支持 |
| Edge (Windows) | ✅ 完全支持 |
| 微信内置浏览器 | ✅ 完全支持 |
| QQ浏览器 | ✅ 完全支持 |

## 🛠️ 开发

### 生成图标

```bash
# 安装依赖
pip install Pillow

# 生成图标
python create_pwa_icons.py
```

### 自定义配置

修改 `manifest.json` 文件来自定义PWA配置：
- 应用名称和描述
- 图标路径
- 主题颜色
- 显示模式

### Service Worker

`sw.js` 文件负责：
- 资源缓存策略
- 离线功能
- 推送通知
- 后台同步

## 📊 性能优化

- **资源预缓存** - 关键资源预先缓存
- **图片优化** - 使用WebP格式和响应式图片
- **代码压缩** - 减少文件大小
- **懒加载** - 按需加载资源
- **离线优先** - 优先使用缓存资源

## 🔔 推送通知

PWA支持推送通知功能：
- 游戏提醒
- 新版本通知
- 活动通知

## 📈 使用统计

可以通过以下方式统计使用情况：
- Google Analytics
- 自定义统计
- Service Worker日志

## 🔄 更新机制

- 自动检测新版本
- 后台更新
- 用户提示更新

## 🐛 故障排除

### 常见问题

1. **PWA无法安装**
   - 确保使用HTTPS连接
   - 检查manifest.json配置
   - 验证Service Worker注册

2. **游戏无法运行**
   - 检查浏览器兼容性
   - 清除浏览器缓存
   - 重新加载页面

3. **图标不显示**
   - 检查图标文件路径
   - 验证图标格式
   - 重新生成图标

### 调试工具

- Chrome DevTools
- Lighthouse PWA审计
- Service Worker调试

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📞 支持

如有问题，请：
1. 查看故障排除部分
2. 提交Issue
3. 联系开发者

---

🎉 **享受游戏！** 现在您拥有了一个功能完整的PWA贪吃蛇游戏！ 
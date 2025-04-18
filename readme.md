# 📄 PDF Cleaner — PDF 空白页与指定页删除工具

这是一个部署在 **macOS** 上的局域网 PDF 工具，用户可通过浏览器上传 PDF 文件，自动删除空白页或手动选择指定页码删除，并下载清理后的新文件。

---

## ✨ 功能介绍

- ✅ 自动清理 PDF 空白页（保留含图片的页面）
- ✅ 手动选择页码进行删除
- ✅ 隐藏访问路径防止他人访问
- ✅ 上传文件自动定时清理（默认 5 分钟）

---

## 💻 环境要求

- 系统：macOS
- Python：3.9 或以上版本
- （推荐）使用 conda 创建虚拟环境

## 🚀 安装与运行步骤

### 1. 克隆项目或进入代码目录

```bash
git clone https://your.repo/pdf-cleaner.git
cd pdf-cleaner
```

### 2. （可选）使用 Conda 创建并激活虚拟环境
```bash
conda create -n pdfcleaner python=3.9
conda activate pdfcleaner
```

### 3. 安装依赖库
```bash
pip install -r requirements.txt
```
### 4. 启动服务
```bash
python app.py
```
### 5. 访问页面
打开浏览器，访问以下隐藏路径（默认配置）：
```bash
http://<本机IP>:8912/cleaner-a8F7g9Qd23kL
```
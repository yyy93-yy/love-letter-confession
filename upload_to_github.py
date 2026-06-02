import requests
import base64
import json

# GitHub API 配置
GITHUB_TOKEN = ""  # 用户需要在 GitHub 设置中创建个人访问令牌
USERNAME = ""      # 用户的 GitHub 用户名
REPO_NAME = "love-letter-confession"
BRANCH = "main"

# 读取 HTML 文件内容
with open("love-letter.html", "r", encoding="utf-8") as f:
    content = f.read()

# Base64 编码内容
encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")

# 1. 创建仓库
print("🚀 正在创建 GitHub 仓库...")
create_repo_url = "https://api.github.com/user/repos"
repo_data = {
    "name": REPO_NAME,
    "description": "浪漫星空表白网页",
    "private": False,
    "auto_init": False
}

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.post(create_repo_url, headers=headers, data=json.dumps(repo_data))
if response.status_code == 201:
    print(f"✅ 仓库创建成功: {response.json()['html_url']}")
else:
    print(f"❌ 仓库创建失败: {response.text}")
    exit()

# 2. 创建文件
print("📤 正在上传文件...")
create_file_url = f"https://api.github.com/repos/{USERNAME}/{REPO_NAME}/contents/index.html"
file_data = {
    "message": "Add love letter HTML file",
    "content": encoded_content,
    "branch": BRANCH
}

response = requests.put(create_file_url, headers=headers, data=json.dumps(file_data))
if response.status_code == 201:
    print(f"✅ 文件上传成功!")
    
    # 生成预览链接
    raw_url = f"https://raw.githubusercontent.com/{USERNAME}/{REPO_NAME}/{BRANCH}/index.html"
    preview_url = f"https://htmlpreview.github.io/?{raw_url}"
    
    print("\n" + "="*60)
    print("🎉 部署完成!")
    print(f"📁 GitHub 仓库: https://github.com/{USERNAME}/{REPO_NAME}")
    print(f"🔗 预览链接: {preview_url}")
    print("💡 复制预览链接到微信发送给好友即可!")
    print("="*60)
else:
    print(f"❌ 文件上传失败: {response.text}")

# 使用说明
print("\n📖 使用方法:")
print("1. 访问 https://github.com/settings/tokens 创建个人访问令牌")
print("2. 勾选 repo 权限")
print("3. 将令牌填入 GITHUB_TOKEN 变量")
print("4. 填入你的 GitHub 用户名")
print("5. 重新运行此脚本")

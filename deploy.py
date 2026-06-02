import requests
import base64
import json

# ==================== 请填写你的 GitHub 信息 ====================
GITHUB_TOKEN = input("请输入你的 GitHub 个人访问令牌: ").strip()
USERNAME = input("请输入你的 GitHub 用户名: ").strip()
REPO_NAME = "love-letter-confession"
BRANCH = "main"
# ===============================================================

# 读取 HTML 文件内容
with open("love-letter.html", "r", encoding="utf-8") as f:
    content = f.read()

# Base64 编码内容
encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# 1. 创建仓库
print("\n🚀 正在创建 GitHub 仓库...")
create_repo_url = "https://api.github.com/user/repos"
repo_data = {
    "name": REPO_NAME,
    "description": "浪漫星空表白网页",
    "private": False,
    "auto_init": False
}

response = requests.post(create_repo_url, headers=headers, data=json.dumps(repo_data))
if response.status_code == 201:
    print(f"✅ 仓库创建成功")
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
    print("✅ 文件上传成功!")
    
    # 生成链接
    repo_url = f"https://github.com/{USERNAME}/{REPO_NAME}"
    raw_url = f"https://raw.githubusercontent.com/{USERNAME}/{REPO_NAME}/{BRANCH}/index.html"
    preview_url = f"https://htmlpreview.github.io/?{raw_url}"
    
    print("\n" + "="*60)
    print("🎉 部署完成!")
    print(f"📁 GitHub 仓库: {repo_url}")
    print(f"🔗 预览链接: {preview_url}")
    print("\n💡 使用方法:")
    print("1. 复制预览链接")
    print("2. 在微信中发送给好友")
    print("3. 好友点击即可访问表白网页")
    print("="*60)
else:
    print(f"❌ 文件上传失败: {response.text}")

# ====== 如何获取 GitHub 令牌 ======
print("\n📖 如果还没有令牌，请按以下步骤获取:")
print("1. 访问 https://github.com/settings/tokens")
print("2. 点击 \"Generate new token\"")
print("3. 填写 Note (如: Love Letter Token)")
print("4. 勾选 repo 权限")
print("5. 点击 \"Generate token\"")
print("6. 复制生成的令牌并粘贴到上方")

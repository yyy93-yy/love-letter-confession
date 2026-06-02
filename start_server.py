from pyngrok import ngrok
import time

# 设置 ngrok authtoken（如果有）
# ngrok.set_auth_token("YOUR_AUTH_TOKEN")

# 创建 HTTP 隧道，转发到本地 8000 端口
public_url = ngrok.connect(8000)

print("=" * 50)
print("🎉 网站已成功暴露到公网！")
print(f"🌐 公网访问地址: {public_url}")
print("📱 可以直接复制这个链接发送给微信好友")
print("=" * 50)

# 保持运行
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    ngrok.kill()
    print("✅ 服务已停止")

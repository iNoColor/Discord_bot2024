import requests
import json

def send_message():
    """
    ฟังก์ชันสำหรับส่งข้อความไปทาง webhook ของ Discord
    """
    # กำหนด URL ของ webhook ที่จะส่งข้อความไป
    webhook_url = "https://discord.com/api/webhooks/1260264408425173002/PX1HJpORKy-AdgzUIKFTtuCefbnOqlN8yT5GfuJBJDbbOcuj06ImRe6v28p_yYvwEiuh"
    
    # รับข้อความจากผู้ใช้
    message_content = input("กรุณาใส่ข้อความที่ต้องการส่ง: ")

    # สร้าง payload สำหรับส่งข้อมูล
    payload = {
        "content": message_content
    }

    # กำหนด headers สำหรับการส่งข้อมูลในรูปแบบ JSON
    headers = {
        "Content-Type": "application/json"
    }

    # ส่งคำขอ POST ไปยัง webhook URL
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    # ตรวจสอบสถานะการส่งคำขอ
    if response.status_code == 204:
        print("ส่งข้อความสำเร็จ")
    else:
        print("ส่งข้อความไม่สำเร็จ")

# เรียกใช้งานฟังก์ชันส่งข้อความ
send_message()

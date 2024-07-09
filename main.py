import requests
import json

def send_message():
    """
    ฟังก์ชันสำหรับส่งข้อความไปทาง webhook ของ Discord
    """
    # กำหนด URL ของ webhook ที่จะส่งข้อความไป
    webhook_url = "https://discord.com/api/webhooks/1154399027383775252/nqnFVnsQus90hTtkyfpt92QZnXQYdOE-2ixpcDT1cULC0ytmjnayz-l_LkePUQ9_feib"
    
    while True:
        # รับข้อความจากผู้ใช้
        message_content = input("กรุณาใส่ข้อความที่ต้องการส่ง (หรือพิมพ์ 'exit' เพื่อออก): ")
        
        # ถ้าผู้ใช้พิมพ์ 'exit' ให้หยุดการทำงานของลูป
        if message_content.lower() == 'exit':
            print("หยุดการทำงาน...")
            break

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

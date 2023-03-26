# 引入 MIMEText 物件
from email.mime.text import MIMEText
# 如果想要在電子郵件中加入圖片，則須在 Python 專案中引用 MIMEImage 類別，並且引用 pathlib 函式庫來讀取圖片
from email.mime.image import MIMEImage
from pathlib import Path
# 引入 MIMEMultipart 物件
from email.mime.multipart import MIMEMultipart
# Python 專案中的電子郵件內容完成後，接下來就要設定 Gmail 的 SMTP 伺服器來寄送
import smtplib
# 建立 MIMEText 物件
text = MIMEText("I'm using python")
# 建立 MIMEImage 物件
image = MIMEImage(Path("C:/Users/Lucas/Documents/Python_2023Spring/class1/logo_tree.png").read_bytes())
# 建立 MIMEMultipart 物件
content = MIMEMultipart()
# 郵件標題
content["subject"] = "2023 Python App 創新程式春季班【Demo】"
# 寄件者
content["from"] = "lucaschang1112@gmail.com"
# 收件者
content["to"] = "sallyyengchi@gmail.com"
# 郵件內容
content.attach(text)
# 郵件圖片內容
content.attach(image)

# 利用 with 來自動釋放資源
with open("C:/Users/Lucas/Documents/Python_2023Spring/class5/password.txt", "r") as f:
    mailToken = f.read()
# 建立 smtplib 物件
smtp = smtplib.SMTP(host = "smtp.gmail.com", port = "587")
# 利用 with 來自動釋放資源
with smtp:
    try:
        # 驗證SMTP伺服器
        smtp.ehlo()
        # 建立加密傳輸
        smtp.starttls()
        smtp.login("IAmSoGood1112@gmail.com", mailToken)
        # 寄送郵件
        smtp.send_message(content)
        print("Email is sended compeletely!")
        smtp.quit()
    except Exception as e:
        print("Error message: ", e)
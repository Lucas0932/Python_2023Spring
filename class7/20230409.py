# 傳簡訊
"""
from twilio.rest import Client

account_sid = 'AC6750b87daddd4a84526e6a67a7544270'
auth_token = '16f195c194f5dec08ec3f8d9d3d601a6'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGf3f9d66c5289a78928d0bf8022618a46',
    body='SMS Testing',
    to='+886912515971'
)

print(message.sid)
"""
#照出路徑
"""
# 大多數常用操作，只需要用到 Path 這個類別
from pathlib import Path
# # 引數傳入你要指向的位置
# p = Path('.\Desktop')
# 若沒有傳入引數，預設指向開啟 Python 的位置
p = Path("class7\20230409.py")
# resolve() 找出絕對路徑
p.resolve()
# 輸出絕對路徑
print(p.resolve())
"""
#讀表(google sheets)
"""
import pygsheets
gc = pygsheets.authorize(service_file = "C:/Users/Lucas/Documents/Python_2023Spring/class7/double-zenith-383613-e7b227ae03b3.json")
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1LZPZ0QDtbQR8_r5Un3BGbn5jwSclXUIA11D_arPsrv4/edit#gid=0")
# 利用Index 選取工作表
ws = sht[0]
# # 利用名子選取工作表
# ws = sht.worksheet_by_title("工作表1")
ws.update_value("A1", "yay")
# 讀取表中內容
# value = ws.get_value("A1")
# print("A1's value: " + value)
A1 = ws.cell("A1")
print(A1)
# 清除 sheet 內所有值
ws.clear()
"""
#利用 python 編輯 google sheets
""""""
import pygsheets
gc = pygsheets.authorize(service_file = "C:/Users/Lucas/Documents/Python_2023Spring/class7/double-zenith-383613-e7b227ae03b3.json")
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1LZPZ0QDtbQR8_r5Un3BGbn5jwSclXUIA11D_arPsrv4/edit#gid=0")
# 利用名子選取工作表
ws = sht.worksheet_by_title("classwork")
ws.update_value("A1", "Name")
ws.update_value("A2", "Amy")
ws.update_value("A3", "Peter")
ws.update_value("B1", "Age")
ws.update_value("B2", "19")
ws.update_value("B3", "15")
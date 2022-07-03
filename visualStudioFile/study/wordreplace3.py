from win32com.client import Dispatch
import win32com.client# 导入脚本模块
app = Dispatch('Word.Application')

doc = app.Documents.Open( "C:\\Users\\29545\\Desktop\\测试2.docx")
# 运行下句代码后，s获得新建文档的光标焦点，也就是图中的回车符前
s = app.Selection
# 用“Hello, World!“替换s代表的范围的文本
s.Text =  'Hello, world!'

w = win32com.client.Dispatch('Word.Application')
# 新建word文档
doc = app.Documents.Add()

# 后台运行，不显示，不警告
w.Visible = 0

w.DisplayAlerts = 0

doc = w.Documents.Open("C:\\Users\\29545\\Desktop\\测试2.docx")
# 运行下句代码后，s获得新建文档的光标焦点，也就是图中的回车符前
s = app.Selection
# 用“Hello, World!“替换s代表的范围的文本
s.Text =  'Hello, world!'
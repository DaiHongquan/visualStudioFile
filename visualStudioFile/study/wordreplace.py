import win32com.client# 导入脚本模块

WordApp = win32com.client.Dispatch("Word.Application")# 载入WORD模块

WordApp.Visible = True# 显示Word应用程序

w = win32com.client.Dispatch('Word.Application')

# 后台运行，不显示，不警告
w.Visible = 0

w.DisplayAlerts = 0

doc = w.Documents.Open("C:\\Users\\29545\\Desktop\\测试2.docx")

OldStr= 'MACROBUTTON  AcceptAllChangesInDoc ${extra.partyA_partyName_1}'

NewStr= 'MACROBUTTON  AcceptAllChangesInDoc ${extra.partyA_partyName_2}'

w.Selection.Find.Execute(OldStr, False, False, False, False, False, True, 1, True, NewStr, 2)

# worddoc = w.Documents.Add() # 创建新的文档

# ‘1111’为查找目标，‘abcd’为替换为的字符

doc.Content.Find.Execute(FindText=u'招商', ReplaceWith=u'不', Replace=2, Wrap=1)

# 保存，如果只有一种替换，这不是必须的，有两种替换要先保存第一种

doc.Save()

# 关闭word

doc.Close()
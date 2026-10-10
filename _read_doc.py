# -*- coding: utf-8 -*-
import docx
src = r'E:\2024级计科软工五班大三课程\Android开发\实验二\实验二+UI控件代码生成以及MVC.docx'
d = docx.Document(src)
for i, p in enumerate(d.paragraphs):
    t = p.text.strip()
    if t:
        print(i, '|', p.style.name, '|', t[:80])

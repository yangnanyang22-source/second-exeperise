# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont

SHOT_DIR = r'E:\Android exeperise\exeperise2\_shots'
os.makedirs(SHOT_DIR, exist_ok=True)

# 找一个支持中文的等宽字体
font_candidates = [
    r'C:\Windows\Fonts\consola.ttf',      # Consolas 英文等宽
    r'C:\Windows\Fonts\msyh.ttc',         # 微软雅黑
    r'C:\Windows\Fonts\sarasa.ttf',
]
# 用两个字体：代码英文用 Consolas，中文用微软雅黑
try:
    font_en = ImageFont.truetype(r'C:\Windows\Fonts\consola.ttf', 18)
except:
    font_en = ImageFont.load_default()
try:
    font_cn = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc', 18)
except:
    font_cn = font_en
try:
    font_title = ImageFont.truetype(r'C:\Windows\Fonts\msyhbd.ttc', 18)
except:
    font_title = font_cn

BG = (30, 30, 30)
TITLE_BG = (55, 55, 60)
TEXT = (220, 220, 220)
KEYWORD = (86, 182, 194)   # 青色
STRING = (206, 145, 120)    # 橙色
COMMENT = (133, 153, 0)     # 绿色
LINENO = (120, 120, 120)
ACCENT = (255, 165, 0)

# 简单语法高亮
KEYWORDS = {
    'package','import','class','fun','return','private','public','protected',
    'override','val','var','lateinit','to','mapOf','true','false','null',
    'android','xml','version','encoding',
}

def is_cn(ch):
    return '\u4e00' <= ch <= '\u9fff' or ch in '，。：；！？、""''（）《》…—'

def draw_text_line(draw, x, y, text, font_en, font_cn):
    cur = x
    buf = ''
    cur_cn = None
    for ch in text:
        cn = is_cn(ch)
        if cur_cn is None:
            cur_cn = cn
            buf = ch
        elif cn == cur_cn:
            buf += ch
        else:
            f = font_cn if cur_cn else font_en
            draw.text((cur, y), buf, font=f, fill=TEXT)
            cur += draw.textlength(buf, font=f)
            buf = ch
            cur_cn = cn
    if buf:
        f = font_cn if cur_cn else font_en
        draw.text((cur, y), buf, font=f, fill=TEXT)
    return cur

def render_code(title, code, out_name, highlight_lines=None, highlight_color=None):
    lines = code.split('\n')
    line_h = 26
    top_pad = 50
    bottom_pad = 20
    left_pad = 70
    right_pad = 30
    width = 900
    height = top_pad + bottom_pad + line_h * (len(lines) + 1)
    img = Image.new('RGB', (width, height), BG)
    d = ImageDraw.Draw(img)
    # 标题栏
    d.rectangle([0, 0, width, 40], fill=TITLE_BG)
    d.text((15, 10), title, font=font_title, fill=(230, 230, 230))
    # 三个圆点
    for i, c in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
        d.ellipse([width-90+i*22, 12, width-78+i*22, 24], fill=c)

    for i, line in enumerate(lines):
        y = top_pad + i * line_h
        # 行号
        d.text((15, y+4), str(i+1), font=font_en, fill=LINENO)
        # 高亮行背景
        if highlight_lines and (i+1) in highlight_lines:
            d.rectangle([left_pad-10, y, width-right_pad, y+line_h], fill=highlight_color or (60, 50, 20))
        # 渲染
        draw_text_line(d, left_pad, y+4, line, font_en, font_cn)

    out = os.path.join(SHOT_DIR, out_name)
    img.save(out)
    print('saved', out)

# 1. build.gradle 里 viewBinding 部分（高亮32-34行）
with open(r'E:\Android exeperise\exeperise2\app\build.gradle', encoding='utf-8') as f:
    gradle = f.read()
render_code('app/build.gradle  (开启 ViewBinding)', gradle, '02_build_gradle_viewbinding.png',
            highlight_lines={32,33,34}, highlight_color=(50, 70, 50))

# 2. strings.xml
with open(r'E:\Android exeperise\exeperise2\app\src\main\res\values\strings.xml', encoding='utf-8') as f:
    strings = f.read()
render_code('app/src/main/res/values/strings.xml', strings, '03_strings_xml.png')

# 3. activity_main.xml
with open(r'E:\Android exeperise\exeperise2\app\src\main\res\layout\activity_main.xml', encoding='utf-8') as f:
    layout = f.read()
render_code('app/src/main/res/layout/activity_main.xml', layout, '04_activity_main_xml.png')

# 4. ProgramAdviser.kt
with open(r'E:\Android exeperise\exeperise2\app\src\main\java\cn\edu\sicnu\cs\yn\exeperise2\ProgramAdviser.kt', encoding='utf-8') as f:
    model = f.read()
render_code('ProgramAdviser.kt  (Model 层)', model, '05_program_adviser_model.png')

# 5. MainActivity.kt
with open(r'E:\Android exeperise\exeperise2\app\src\main\java\cn\edu\sicnu\cs\yn\exeperise2\MainActivity.kt', encoding='utf-8') as f:
    main = f.read()
render_code('MainActivity.kt  (Controller)', main, '06_main_activity_controller.png')

print('ALL DONE')

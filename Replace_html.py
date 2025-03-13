import re
from os import listdir
from os.path import isfile, join
import os

def modify_html(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 確保只處理 .html 檔案
    if not file_path.lower().endswith('.html'):
        return
    
    # 檢查是否已經修改過，避免重複修改
    if 'selectRandomDish()' in content or 'class="dish"' in content:
        print(file_path,"has already fixed.")
        return
    
    # 替換 <head> 和 <body> 開頭部分
    old_body_start = """</head>\n<body bgcolor=\"#FFFFFF\" leftmargin=\"0\" topmargin=\"0\" marginwidth=\"0\" marginheight=\"0\">"""
    new_body_start = """<link rel=\"stylesheet\" href=\"frameStyle.css\">\n<script>function selectRandomDish() {document.querySelectorAll('.dish').forEach(img => img.classList.remove('selected'));let dishes = document.querySelectorAll('.dish');let randomIndex = Math.floor(Math.random() * dishes.length);let selectedDish = dishes[randomIndex];selectedDish.classList.add('selected');}\n</script>\n</head>\n<body bgcolor=\"#FFFFFF\" leftmargin=\"0\" topmargin=\"0\" marginwidth=\"0\" marginheight=\"0\">\n<button onclick=\"selectRandomDish()\">抽選餐點</button>"""
    content = content.replace(old_body_start, new_body_start)
    
    # 替換 alt="a" 為 alt="a" class="dish"
    content = re.sub(r'alt="a"(?! class="dish")', 'alt="a" class="dish"', content)
    
    # 儲存修改後的內容
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print("Complete with",file_path)

path = "DetailMenu//"
FileName = [f for f in listdir(path) if isfile(join(path, f))]
for i in range(len(FileName)):
    modify_html(path+FileName[i], path+FileName[i])
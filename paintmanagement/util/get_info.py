import requests
import datetime

def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def get_text_from_url(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    
    if response.status_code == 200:
        try:
            text = response.content.decode('utf-8')
        except UnicodeDecodeError:
            text = response.content.decode('utf-8', errors='ignore')
            print("一部の文字は無視されました。")
        return text
    else:
        print(f"Error: {response.status_code}")
        return None

# 指定のURLからテキストを取得する例
url = "https://www.gaianotes.com/products/gaia-color_basic.html"
text = get_text_from_url(url)
if text:
    now = datetime.datetime.now()
    file_name = '.\\paintmanagement\\temp\\output_' + now.strftime('%Y-%m-%d_%H-%M-%S') + '.txt'
    save_text_to_file(text, file_name)
    print("テキストがファイルに保存されました。")

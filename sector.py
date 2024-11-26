import json
import requests
from bs4 import BeautifulSoup

# 取得臺灣證券交易所公告內容的 URL
urls = [
    "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2",  # 上市證券
    # "https://isin.twse.com.tw/isin/C_public.jsp?strMode=4",  # 上櫃證券
    # "https://isin.twse.com.tw/isin/C_public.jsp?strMode=5"   # 興櫃證券
]

# 分類規則
category_mapping = {
    "半導體業": ["半導體業"],
    "電腦及週邊設備業": ["電腦及週邊設備業"],
    "電子零組件業": ["電子零組件業"],
    "航運業": ["航運業"],
    "通信網路業": ["通信網路業"],
    "其他": ["其他"],
    "汽車工業": ["汽車工業"],
    "橡膠工業": ["橡膠工業"],
    "建材營造": ["建材營造"],
    "玻璃陶瓷": ["玻璃陶瓷"],
    "造紙工業": ["造紙工業"],
    "鋼鐵工業": ["鋼鐵工業"],
    "塑膠工業": ["塑膠工業"],
    "紡織纖維": ["紡織纖維"],
    "生技醫療業": ["生技醫療業"],
    "化學工業": ["化學工業"],
    "水泥工業": ["水泥工業"],
    "油電燃氣業": ["油電燃氣業"],
    "貿易百貨": ["貿易百貨"],
    "觀光事業": ["觀光事業"],
    "資訊服務業": ["資訊服務業"],
    "電機機械": ["電機機械"],
    "電器電纜": ["電器電纜"],
    "金融保險": ["金融保險"],
    "食品工業": ["食品工業"],
    "其他電子業": ["其他電子業"],
    "光電業": ["光電業"],
    "電子通路業": ["電子通路業"],
    "綜合": ["綜合"]
}

# 初始化分類結果
classified_data = {category: [] for category in category_mapping.keys()}

# 取得和處理公告內容
data = {}
total_urls = len(urls)
for index, url in enumerate(urls, start=1):
    print(f"Processing URL {index}/{total_urls}: {url}")

    response = requests.get(url)
    response.encoding = 'big5'  # 設定正確的編碼格式

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'h4'})

    if not table:
        print(f"Table not found for URL: {url}")
        continue

    for row in table.find_all('tr')[1:]:  # 跳過表頭
        cells = row.find_all('td')
        if len(cells) != 7:
            continue

        try:
            code, name = cells[0].text.split("\u3000")
        except ValueError:
            continue  # 避免資料格式不符導致的錯誤

        internationality = cells[1].text
        list_date = cells[2].text
        market_type = cells[3].text
        industry_type = cells[4].text

        data[code] = {
            "名稱": name,
            "代號": code,
            "市場別": market_type,
            "產業別": industry_type,
            "上市日期": list_date,
            "國際代碼": internationality
        }

# 將資料分類
for code, info in data.items():
    # 只處理純數字代號
    if code.isdigit() and 1000 < int(code) < 10000:
        industry = info["產業別"]
        for category, industries in category_mapping.items():
            if industry in industries:
                classified_data[category].append(info)
                break

# 儲存完整資料和分類結果到 JSON 檔案
with open("stock_infos.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("classified_stocks.json", "w", encoding="utf-8") as f:
    json.dump(classified_data, f, ensure_ascii=False, indent=2)

print("資料已處理完畢，分別儲存到 stock_infos.json 和 classified_stocks.json")

import time
import yfinance as yf
import json
import os
import re

# 讀取台股資料，假設 'stock_infos.json' 內有台股資料
with open('stock_infos.json', 'r', encoding='utf-8') as f:
    tickers_data = json.load(f)

# 設定資料夾來儲存每個 sector 的檔案
output_dir = 'TWSE_sector_data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 初始化請求計數
request_count = 0
hourly_limit = 2000  # 每小時最多 2000 次請求
max_request_per_second = 0.75  # 每次請求之間的最小時間間隔（秒）

# 追蹤今天的請求次數
today_request_count = 0
start_time = time.time()  # 開始計算時間

# 只處理四位數的代號
for key, company in tickers_data.items():
    if not re.fullmatch(r"\d{4}", key):  # 如果代號不是四位數，跳過
        continue

    ticker = f"{key}.TW"  # 加上 .TW 作為台股的後綴
    print(f"Downloading data for {ticker}...")

    # 檢查是否超過每小時請求限制
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= 3600:  # 如果已經過了一小時
        start_time = current_time  # 重設時間
        request_count = 0  # 重設每小時計數
        print(f"Resetting hourly request counter.")

    if request_count >= hourly_limit:  # 如果達到每小時限制
        print("Reached hourly request limit, pausing for 1 hour.")
        time.sleep(3600)  # 停頓 1 小時
        request_count = 0  # 重設計數

    try:
        stock = yf.Ticker(ticker)
        sector = stock.info.get('sector', 'Unknown')  # 取得 sector 資訊
        company["sector"] = sector
        print(f"Sector for {ticker}: {sector}")
    except Exception as e:
        print(f"Error for {ticker}: {e}")
        sector = 'Unknown'

    # 更新請求計數
    request_count += 1
    today_request_count += 1

    # 儲存分類資料
    safe_sector_name = re.sub(r'[\/:*?"<>|]', '_', sector)  # 替換非法字符
    sector_file = os.path.join(output_dir, f"{safe_sector_name}.json")

    # 讀取現有檔案（如果有的話）
    if os.path.exists(sector_file):
        with open(sector_file, 'r', encoding='utf-8') as f:
            sector_data = json.load(f)
    else:
        sector_data = {}

    # 將當前公司資料加入對應 sector 的資料中
    sector_data[key] = company  # 使用代號作為鍵，將公司資料加入

    # 儲存更新後的 sector 檔案
    with open(sector_file, 'w', encoding='utf-8') as f:
        json.dump(sector_data, f, indent=4, ensure_ascii=False)

    # 延遲請求避免過快
    time.sleep(max_request_per_second)

print("Finished downloading data for all tickers.")

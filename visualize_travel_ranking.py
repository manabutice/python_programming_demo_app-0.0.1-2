# visualize_travel_ranking.py

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Hiragino Sans'

# CSVファイルの読み込み（Travel用）
csv_path = "travel_ranking.csv"

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    print("⚠️ CSVファイルが見つかりません:", csv_path)
    exit()

if df.empty:
    print("⚠️ CSVファイルが空です")
    exit()

# ソート（多い順）
df_sorted = df.sort_values(by="COUNT", ascending=False)

# グラフ描画
plt.figure(figsize=(8, 6))
plt.bar(df_sorted["NAME"], df_sorted["COUNT"])
plt.title("旅行先人気ランキング")
plt.xlabel("場所名")
plt.ylabel("投票数")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

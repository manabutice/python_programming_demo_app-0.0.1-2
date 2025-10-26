previous_num = 0

for current_num in range(10):
  total = current_num + previous_num
  print(f"現在の数{current_num} 前の数 {previous_num} 合計: {total}")
  previous_num = current_num
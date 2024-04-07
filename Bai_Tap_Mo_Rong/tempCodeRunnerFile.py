def tinh_tong_so(chuoi):
  """
  Hàm tính tổng các số nguyên dương và âm trong chuỗi.

  Tham số:
    chuoi: Chuỗi chứa các số nguyên.

  Trả về:
    Tuple (tong_duong, tong_am) chứa tổng các số nguyên dương và âm.
  """
  tong_duong = 0
  tong_am = 0
  for so in chuoi.split(","):
    so_nguyen = int(so)
    if so_nguyen > 0:
      tong_duong += so_nguyen
    elif so_nguyen < 0:
      tong_am += so_nguyen
  return tong_duong, tong_am

chuoi_so = input("Nhập chuỗi số (phân cách bởi dấu phẩy): ")
tong_duong, tong_am = tinh_tong_so(chuoi_so)

print(f"Tổng các số nguyên dương: {tong_duong}")
print(f"Tổng các số nguyên âm: {tong_am}")
# format specifiers = {value:flags} format value based on flags inserted


price1=3000.23456789
price2=1234.977777

print(f"price1 is:{price1}")
print(f"price1 is:{price1:,}") # thousand seperator
print(f"price1 is:{price1:.2f}") # after decial take 2 digits only
print(f"price1 is:{price1:+}")  # add + sign before number starts
print(f"price1 is:{price1: }")  # just number with space starts
print(f"price1 is:{price1:20}")  # number prints with length 20 ,spaces padding
print(f"price1 is:{price1:020}")  # 20 length with 0 padded
print(f"price1 is:{price1:#>20}") # 20 length with # padded
print(f"price1 is:{price1:<20}") # right justified
print(f"price1 is:{price1:>20}") # left justified
print(f"price1 is:{price1:^20}") # center alignment
print(f"price1 is:{price1:+,.2f}") # + starts, thousand seperator,2 decimal digits


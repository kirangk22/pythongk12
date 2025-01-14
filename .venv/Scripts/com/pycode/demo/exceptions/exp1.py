
print("Start of prog")

try:
    x=int("aaa")
except Exception as e:
    print(f"====>{e}")
    exit(0)
else:
    print("else block as no exceptions came... and x val is:",x)
finally:
    print("finally always executing")

print(f"Remaing prog part")

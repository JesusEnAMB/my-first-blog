n=25
for y in range(n):
    row="".join("▲" if x&y==0 else " " for x in range(n))
    print(row)
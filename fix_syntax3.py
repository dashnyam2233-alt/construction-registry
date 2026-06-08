path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\templates\registry\budget_calculator.html"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line_num in [1825, 1826, 1827, 1828, 1829, 1830, 1855, 1856, 1857, 1858, 1859, 1860, 1897, 1898, 1899, 1900, 1901, 1902, 1928, 1929, 1930, 1931, 1932, 1933]:
    if line_num <= len(lines):
        print(f"{line_num}: {lines[line_num-1]}", end='')
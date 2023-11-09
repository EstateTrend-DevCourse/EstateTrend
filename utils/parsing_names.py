from local_name import local_name_2
import json

gugun_keys = []
for k, value in local_name_2.items():
    for v in value:
        gugun_keys.append(f"{k} {v}")

# print(gugun_keys)

local_name_3 = {k: [] for k in gugun_keys}


f = open("utils/local_names.txt", "r", encoding="euc-kr")
lines = f.readlines()

f.close()

for l in lines:
    l_str = l.strip().split(" ")
    # print(l_str)
    if len(l_str) >= 3:
        gg1 = " ".join(l_str[:2])
        if gg1 in local_name_3:
            local_name_3[gg1].append(" ".join(l_str[2:]))
            continue

    if len(l_str) >= 4:
        gg2 = " ".join(l_str[:3])
        if gg2 in local_name_3:
            local_name_3[gg2].append(" ".join(l_str[3:]))

with open("utils/output.py", "a", encoding="utf-8") as f:
    f.write(json.dumps(local_name_3, ensure_ascii=False))

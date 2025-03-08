protein_cc_tt = {}
go_cc_tt = "dataset/Krogan14K/krogan14k_go_cc_tt_information.txt"
with open(go_cc_tt) as f:
    for line in f:
        tt = line.strip().split("TT:")[1]
        cc = line.strip().split("CC:")[1:]

        if tt != 'set()' and len(cc) != 0:
            cc[-1] = cc[-1].split(" TT:")[0]
            cc_c = []
            for c in cc:
                c_r = c.strip()
                cc_c.append(c_r)

            tt_1 = tt.split(",")
            tt_1[0] = tt_1[0].split("{")[1]
            tt_1[-1] = tt_1[-1].split("}")[0]
            tt_t = []
            for t in tt_1:
                t_r = t.strip()
                tt_t.append(int(t_r))

            protein = line.strip().split(" ", 1)[0]

            cc_tt = []
            tt_t.sort()
            cc_tt.append(cc_c)
            cc_tt.append(tt_t)
            protein_cc_tt[protein] = cc_tt
print("protein_cc_tt")
print("GO_CC")

protein_map = {}


def reco_c(x):
    GO_CC_map = {}
    for i in range(len(GO_CC)):
        GO_CC_map[GO_CC[i]] = i
    return GO_CC_map[x]


for key, value in protein_cc_tt.items():
    map_value = []
    c = value[0]
    c_map = list(map(reco_c, c))
    map_value.append(c_map)
    map_value.append(value[1])
    protein_map[key] = map_value

print("protein_map")
with open('dataset/Krogan14K/krogan14k_re.txt', 'r') as r, \
     open('dataset/Krogan14K/krogan14k_edges_marked.txt', 'w') as out:
    for lin in r:
        # 解析蛋白质对和 flag 值
        pp = lin.strip().split(' ')[:2]  # 蛋白质对
        fl = lin.strip().split('[')[-1]  # flag 部分
        el = fl.split(']')[:-1]          # 提取 flag 列表
        for f in el:
            fla = f.split(',')
        flag = []
        for f in fla:
            f_r = f.strip()
            flag.append(int(f_r))

        # 判断是否删除边
        # 假设 flag 值大于某个阈值（例如 144）时删除边，可以根据需求调整规则
        threshold = 144  # 示例阈值，可根据实际需求调整
        if any(f > threshold for f in flag):
            status = "DELETED"  # 标记为删除
        else:
            status = "KEPT"     # 标记为保留

        # 写入结果文件
        out.write(f"{pp[0]} {pp[1]} {status}\n")

print('Edges marked and processed!')

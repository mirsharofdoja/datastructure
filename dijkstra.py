from collections import deque
graph={
    'A':{'B':2, 'C':6},
    'B':{'C':3, 'D':4},
    'C':{'D':5, 'E':6},
    'D':{'F':5},
    'E':{'F':0},
    'F':{}
}
narxlar = {
    'B': 2,
    'C': 6,
    'D': float('inf'),
    'E': float('inf'),
    'F': float('inf')
}
otalar = {
    'B': 'A',
    'C': 'A',
    'D': None,
    'E': None,
    'F': None,
}
ishlandi = []
def eng_arzon_tugun_top(narxlar):
    eng_arzon=float('inf')
    eng_arzon_tugun=None
    for tugun in narxlar:
        narx=narxlar[tugun]
        if narx<eng_arzon and tugun not in ishlandi:
            eng_arzon=narx
            eng_arzon_tugun=tugun
    return eng_arzon_tugun
# print(eng_arzon_tugun_top(narxlar))
tugun=eng_arzon_tugun_top(narxlar)
while tugun is not None:
    qoshnlar=graph[tugun]
    narx=narxlar[tugun]
    for qoshni in qoshnlar.keys():
        yangi_narx=narx+qoshnlar[qoshni]
        if narxlar[qoshni]>yangi_narx:
            narxlar[qoshni]=yangi_narx
            otalar[qoshni]=tugun
    ishlandi.append(tugun)
    tugun=eng_arzon_tugun_top(narxlar)
print(narxlar)

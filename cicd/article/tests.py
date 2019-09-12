import codecs

# read input file
from pytz import unicode

with codecs.open('未処理DL_abc.csv', 'r', encoding='utf8') as file:
    lines = file.read()

# write output file
with open(unicode("未処理DL_abc.csv".encode('utf-8'), 'utf-8').encode('shift-jis'), 'w', encoding='shift_jis') as file:
    file.write(lines)

print("".join(map(chr, "未処理DL_abc.csv".encode('shift_jis'))))

print("未処理DL_abc.csv".encode('shift_jis'))

print(unicode("未処理DL_abc.csv".encode('shift-jis'), 'shift-jis').encode('utf-8'))

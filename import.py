import jieba
#第一種
#import jieba.analyse
#第二種import
#from jieba import analyse
#第三種
from jieba.analyse import extract_tags

#讀取三部曲
#放在專案下
#檔案路徑=相對路徑
f = open("a.txt", "r", encoding="utf-8")
article = f.read()
f.close()

#jieba.load_userdict("./my dict.txt")
jieba.add_word("自主健康管理")
#["詞1","詞2","詞3"]
sep=" ".join(jieba.cut(article))
print(sep)

print("keyword=", (extract_tags(article, 5)))
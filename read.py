#讀取三部曲
#放在專案下
#檔案路徑=相對路徑
f = open("a.txt", "r", encoding="utf-8")
article = f.read()
f.close()

print(article)
result = {}
for c in article:
    # 對, 第二次遇到
    if c in result:
        result[c] = result[c] + 1
    else:
        result[c] = 1
print(result)
import jieba.analyse
keywords = jieba.analyse.extract_tags(article, 5)
print("keywords", keywords)
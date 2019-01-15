# -*- coding:UTF-8 -*-

def method1():
    from __future__ import unicode_literals
    import types
    import chardet
    import json
    import codecs

    a = "这是中文"
    # print chardet.detect(a)
    fo = codecs.open("test.txt", "w", "utf-8")
    b = {"test": a}
    c = json.dumps(b, ensure_ascii=False)
    # print chardet.detect(c)
    fo.write(a)
    fo.write(c)
    fo.close()

def method2():
    import types
    import chardet
    import json

    a = "这是中文"
    # print chardet.detect(a)
    fo = open("test.txt", "w", "utf-8")
    b = {"test": a}
    c = json.dumps(b, ensure_ascii=False).decode('utf8').encode('utf8')
    # print chardet.detect(c)
    fo.write(a)
    fo.write(c)
    fo.close()

if __name__ == "__main__":
    pass

# antlr4Paser
使用`antlr4`解析`/proc/meminfo`文件,查看剩余内存容量,内存不足时通过SMTP报警

## 环境
```
python3+
```

## 使用
```
git clone https://github.com/ylighgh/antlr4Paser.git
```

```
cd antlr4Paser
# 生成解析antlr4解析文件
antlr4 -Dlanguage=Python3 *.g4 -visitor -o antlr
```

```
# 执行
python3 meminfo.py
```

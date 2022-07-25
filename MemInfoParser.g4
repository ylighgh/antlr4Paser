parser grammar MemInfoParser;

options {
    tokenVocab = MemInfoLexer;
}

// MemAvailable:   12259720 kB
prog :  nameStat colon spaces memSizeStat spaces unitStat
;

nameStat : nameRule
;

unitStat : unitRule 
;

memSizeStat : memSizeRule # sizeStatHandler
;

nameRule: memAvailable
;
unitRule: dataType ;


colon: COLON_SYMBOL;
dataType: BYTE_UNIT;
memAvailable : MEM_AVAILABLE;

memSizeRule : memSize=leastOneDigit;

// 至少1个数字
leastOneDigit: singleDigit+;
spaces: space+;

space: SPACE_SYMBOL;
singleDigit: SINGLE_DIGIT;
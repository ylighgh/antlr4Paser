# Generated from MemInfoParser.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,
        1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,55,8,10,11,10,12,10,
        56,1,11,4,11,60,8,11,11,11,12,11,61,1,12,1,12,1,13,1,13,1,13,0,0,
        14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,0,55,0,28,1,0,0,0,2,35,
        1,0,0,0,4,37,1,0,0,0,6,39,1,0,0,0,8,41,1,0,0,0,10,43,1,0,0,0,12,
        45,1,0,0,0,14,47,1,0,0,0,16,49,1,0,0,0,18,51,1,0,0,0,20,54,1,0,0,
        0,22,59,1,0,0,0,24,63,1,0,0,0,26,65,1,0,0,0,28,29,3,2,1,0,29,30,
        3,12,6,0,30,31,3,22,11,0,31,32,3,6,3,0,32,33,3,22,11,0,33,34,3,4,
        2,0,34,1,1,0,0,0,35,36,3,8,4,0,36,3,1,0,0,0,37,38,3,10,5,0,38,5,
        1,0,0,0,39,40,3,18,9,0,40,7,1,0,0,0,41,42,3,16,8,0,42,9,1,0,0,0,
        43,44,3,14,7,0,44,11,1,0,0,0,45,46,5,11,0,0,46,13,1,0,0,0,47,48,
        5,61,0,0,48,15,1,0,0,0,49,50,5,59,0,0,50,17,1,0,0,0,51,52,3,20,10,
        0,52,19,1,0,0,0,53,55,3,26,13,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,
        1,0,0,0,56,57,1,0,0,0,57,21,1,0,0,0,58,60,3,24,12,0,59,58,1,0,0,
        0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,23,1,0,0,0,63,64,
        5,1,0,0,64,25,1,0,0,0,65,66,5,22,0,0,66,27,1,0,0,0,2,56,61
    ]

class MemInfoParser ( Parser ):

    grammarFileName = "MemInfoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'='", "'-'", "'+'", "'~'", 
                     "'_'", "'['", "']'", "'<'", "'>'", "':'", "';'", "'.'", 
                     "<INVALID>", "'*'", "'#'", "'/'", "','", "'\"'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "SPACE_SYMBOL", "EQUALS_SYMBOL", "HYPHEN_SYMBOL", 
                      "PLUS_SYMBOL", "TILDE_SYMBOL", "UNDERSCORE_SYMBOL", 
                      "OPENING_BRACKET_SYMBOL", "CLOSING_BRACKET_SYMBOL", 
                      "OPEN_ANGLED_BRACKET_SYMBOL", "CLOSE_ANGLED_BRACKET_SYMBOL", 
                      "COLON_SYMBOL", "SEMICOLON_SYMBOL", "DOT_SYMBOL", 
                      "WS", "ASTERISK_SYMBOL", "NUMBER_SIGN_SYMBOL", "SLASH_SYMBOL", 
                      "COMMA_SYMBOL", "DOUBLE_QUOTES_SYMBOL", "OPENING_PARENTHESIS_SYMBOL", 
                      "CLOSING_PARENTHESIS_SYMBOL", "SINGLE_DIGIT", "UPPER_ALPHABET_SYMBOL", 
                      "LOWER_ALPHABET_SYMBOL", "JAN_MONTH_PHRASE", "FEB_MONTH_PHRASE", 
                      "MAR_MONTH_PHRASE", "APR_MONTH_PHRASE", "MAY_MONTH_PHRASE", 
                      "JUN_MONTH_PHRASE", "JUL_MONTH_PHRASE", "AUG_MONTH_PHRASE", 
                      "SEP_MONTH_PHRASE", "OCT_MONTH_PHRASE", "NOV_MONTH_PHRASE", 
                      "DEC_MONTH_PHRASE", "GET_HTTP_METHOD_PHRASE", "POST_HTTP_METHOD_PHRASE", 
                      "PUT_HTTP_METHOD_PHRASE", "DELETE_HTTP_METHOD_PHRASE", 
                      "CONNECT_HTTP_METHOD_PHRASE", "OPTIONS_HTTP_METHOD_PHRASE", 
                      "TRACE_HTTP_METHOD_PHRASE", "PATCH_HTTP_METHOD_PHRASE", 
                      "HTTP_VERSION_1_0_PHRASE", "HTTP_VERSION_1_1_PHRASE", 
                      "HTTP_VERSION_2_0_PHRASE", "SCHEME_HTTP_PHRASE", "SCHEME_HTTPS_PHRASE", 
                      "MISS_UCS_PHRASE", "BYPASS_UCS_PHRASE", "EXPIRED_UCS_PHRASE", 
                      "STALE_UCS_PHRASE", "UPDATING_UCS_PHRASE", "REVALIDATED_UCS_PHRASE", 
                      "HIT_UCS_PHRASE", "PRIORITY_LOCAL7_INFO_PHRASE", "PRIORITY_LOCAL7_ERROR_PHRASE", 
                      "MEM_AVAILABLE", "MEM_TOTAL", "BYTE_UNIT" ]

    RULE_prog = 0
    RULE_nameStat = 1
    RULE_unitStat = 2
    RULE_memSizeStat = 3
    RULE_nameRule = 4
    RULE_unitRule = 5
    RULE_colon = 6
    RULE_dataType = 7
    RULE_memAvailable = 8
    RULE_memSizeRule = 9
    RULE_leastOneDigit = 10
    RULE_spaces = 11
    RULE_space = 12
    RULE_singleDigit = 13

    ruleNames =  [ "prog", "nameStat", "unitStat", "memSizeStat", "nameRule", 
                   "unitRule", "colon", "dataType", "memAvailable", "memSizeRule", 
                   "leastOneDigit", "spaces", "space", "singleDigit" ]

    EOF = Token.EOF
    SPACE_SYMBOL=1
    EQUALS_SYMBOL=2
    HYPHEN_SYMBOL=3
    PLUS_SYMBOL=4
    TILDE_SYMBOL=5
    UNDERSCORE_SYMBOL=6
    OPENING_BRACKET_SYMBOL=7
    CLOSING_BRACKET_SYMBOL=8
    OPEN_ANGLED_BRACKET_SYMBOL=9
    CLOSE_ANGLED_BRACKET_SYMBOL=10
    COLON_SYMBOL=11
    SEMICOLON_SYMBOL=12
    DOT_SYMBOL=13
    WS=14
    ASTERISK_SYMBOL=15
    NUMBER_SIGN_SYMBOL=16
    SLASH_SYMBOL=17
    COMMA_SYMBOL=18
    DOUBLE_QUOTES_SYMBOL=19
    OPENING_PARENTHESIS_SYMBOL=20
    CLOSING_PARENTHESIS_SYMBOL=21
    SINGLE_DIGIT=22
    UPPER_ALPHABET_SYMBOL=23
    LOWER_ALPHABET_SYMBOL=24
    JAN_MONTH_PHRASE=25
    FEB_MONTH_PHRASE=26
    MAR_MONTH_PHRASE=27
    APR_MONTH_PHRASE=28
    MAY_MONTH_PHRASE=29
    JUN_MONTH_PHRASE=30
    JUL_MONTH_PHRASE=31
    AUG_MONTH_PHRASE=32
    SEP_MONTH_PHRASE=33
    OCT_MONTH_PHRASE=34
    NOV_MONTH_PHRASE=35
    DEC_MONTH_PHRASE=36
    GET_HTTP_METHOD_PHRASE=37
    POST_HTTP_METHOD_PHRASE=38
    PUT_HTTP_METHOD_PHRASE=39
    DELETE_HTTP_METHOD_PHRASE=40
    CONNECT_HTTP_METHOD_PHRASE=41
    OPTIONS_HTTP_METHOD_PHRASE=42
    TRACE_HTTP_METHOD_PHRASE=43
    PATCH_HTTP_METHOD_PHRASE=44
    HTTP_VERSION_1_0_PHRASE=45
    HTTP_VERSION_1_1_PHRASE=46
    HTTP_VERSION_2_0_PHRASE=47
    SCHEME_HTTP_PHRASE=48
    SCHEME_HTTPS_PHRASE=49
    MISS_UCS_PHRASE=50
    BYPASS_UCS_PHRASE=51
    EXPIRED_UCS_PHRASE=52
    STALE_UCS_PHRASE=53
    UPDATING_UCS_PHRASE=54
    REVALIDATED_UCS_PHRASE=55
    HIT_UCS_PHRASE=56
    PRIORITY_LOCAL7_INFO_PHRASE=57
    PRIORITY_LOCAL7_ERROR_PHRASE=58
    MEM_AVAILABLE=59
    MEM_TOTAL=60
    BYTE_UNIT=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameStat(self):
            return self.getTypedRuleContext(MemInfoParser.NameStatContext,0)


        def colon(self):
            return self.getTypedRuleContext(MemInfoParser.ColonContext,0)


        def spaces(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MemInfoParser.SpacesContext)
            else:
                return self.getTypedRuleContext(MemInfoParser.SpacesContext,i)


        def memSizeStat(self):
            return self.getTypedRuleContext(MemInfoParser.MemSizeStatContext,0)


        def unitStat(self):
            return self.getTypedRuleContext(MemInfoParser.UnitStatContext,0)


        def getRuleIndex(self):
            return MemInfoParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MemInfoParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.nameStat()
            self.state = 29
            self.colon()
            self.state = 30
            self.spaces()
            self.state = 31
            self.memSizeStat()
            self.state = 32
            self.spaces()
            self.state = 33
            self.unitStat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameRule(self):
            return self.getTypedRuleContext(MemInfoParser.NameRuleContext,0)


        def getRuleIndex(self):
            return MemInfoParser.RULE_nameStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameStat" ):
                listener.enterNameStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameStat" ):
                listener.exitNameStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameStat" ):
                return visitor.visitNameStat(self)
            else:
                return visitor.visitChildren(self)




    def nameStat(self):

        localctx = MemInfoParser.NameStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nameStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.nameRule()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unitRule(self):
            return self.getTypedRuleContext(MemInfoParser.UnitRuleContext,0)


        def getRuleIndex(self):
            return MemInfoParser.RULE_unitStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnitStat" ):
                listener.enterUnitStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnitStat" ):
                listener.exitUnitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnitStat" ):
                return visitor.visitUnitStat(self)
            else:
                return visitor.visitChildren(self)




    def unitStat(self):

        localctx = MemInfoParser.UnitStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_unitStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.unitRule()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemSizeStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MemInfoParser.RULE_memSizeStat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SizeStatHandlerContext(MemSizeStatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MemInfoParser.MemSizeStatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def memSizeRule(self):
            return self.getTypedRuleContext(MemInfoParser.MemSizeRuleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeStatHandler" ):
                listener.enterSizeStatHandler(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeStatHandler" ):
                listener.exitSizeStatHandler(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeStatHandler" ):
                return visitor.visitSizeStatHandler(self)
            else:
                return visitor.visitChildren(self)



    def memSizeStat(self):

        localctx = MemInfoParser.MemSizeStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memSizeStat)
        try:
            localctx = MemInfoParser.SizeStatHandlerContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.memSizeRule()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memAvailable(self):
            return self.getTypedRuleContext(MemInfoParser.MemAvailableContext,0)


        def getRuleIndex(self):
            return MemInfoParser.RULE_nameRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameRule" ):
                listener.enterNameRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameRule" ):
                listener.exitNameRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameRule" ):
                return visitor.visitNameRule(self)
            else:
                return visitor.visitChildren(self)




    def nameRule(self):

        localctx = MemInfoParser.NameRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nameRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.memAvailable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(MemInfoParser.DataTypeContext,0)


        def getRuleIndex(self):
            return MemInfoParser.RULE_unitRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnitRule" ):
                listener.enterUnitRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnitRule" ):
                listener.exitUnitRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnitRule" ):
                return visitor.visitUnitRule(self)
            else:
                return visitor.visitChildren(self)




    def unitRule(self):

        localctx = MemInfoParser.UnitRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unitRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.dataType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON_SYMBOL(self):
            return self.getToken(MemInfoParser.COLON_SYMBOL, 0)

        def getRuleIndex(self):
            return MemInfoParser.RULE_colon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColon" ):
                listener.enterColon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColon" ):
                listener.exitColon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColon" ):
                return visitor.visitColon(self)
            else:
                return visitor.visitChildren(self)




    def colon(self):

        localctx = MemInfoParser.ColonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_colon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(MemInfoParser.COLON_SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BYTE_UNIT(self):
            return self.getToken(MemInfoParser.BYTE_UNIT, 0)

        def getRuleIndex(self):
            return MemInfoParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = MemInfoParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dataType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MemInfoParser.BYTE_UNIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemAvailableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEM_AVAILABLE(self):
            return self.getToken(MemInfoParser.MEM_AVAILABLE, 0)

        def getRuleIndex(self):
            return MemInfoParser.RULE_memAvailable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemAvailable" ):
                listener.enterMemAvailable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemAvailable" ):
                listener.exitMemAvailable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemAvailable" ):
                return visitor.visitMemAvailable(self)
            else:
                return visitor.visitChildren(self)




    def memAvailable(self):

        localctx = MemInfoParser.MemAvailableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_memAvailable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(MemInfoParser.MEM_AVAILABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemSizeRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.memSize = None # LeastOneDigitContext

        def leastOneDigit(self):
            return self.getTypedRuleContext(MemInfoParser.LeastOneDigitContext,0)


        def getRuleIndex(self):
            return MemInfoParser.RULE_memSizeRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemSizeRule" ):
                listener.enterMemSizeRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemSizeRule" ):
                listener.exitMemSizeRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemSizeRule" ):
                return visitor.visitMemSizeRule(self)
            else:
                return visitor.visitChildren(self)




    def memSizeRule(self):

        localctx = MemInfoParser.MemSizeRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_memSizeRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            localctx.memSize = self.leastOneDigit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeastOneDigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleDigit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MemInfoParser.SingleDigitContext)
            else:
                return self.getTypedRuleContext(MemInfoParser.SingleDigitContext,i)


        def getRuleIndex(self):
            return MemInfoParser.RULE_leastOneDigit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeastOneDigit" ):
                listener.enterLeastOneDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeastOneDigit" ):
                listener.exitLeastOneDigit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeastOneDigit" ):
                return visitor.visitLeastOneDigit(self)
            else:
                return visitor.visitChildren(self)




    def leastOneDigit(self):

        localctx = MemInfoParser.LeastOneDigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_leastOneDigit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.singleDigit()
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MemInfoParser.SINGLE_DIGIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpacesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MemInfoParser.SpaceContext)
            else:
                return self.getTypedRuleContext(MemInfoParser.SpaceContext,i)


        def getRuleIndex(self):
            return MemInfoParser.RULE_spaces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpaces" ):
                listener.enterSpaces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpaces" ):
                listener.exitSpaces(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpaces" ):
                return visitor.visitSpaces(self)
            else:
                return visitor.visitChildren(self)




    def spaces(self):

        localctx = MemInfoParser.SpacesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_spaces)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.space()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MemInfoParser.SPACE_SYMBOL):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE_SYMBOL(self):
            return self.getToken(MemInfoParser.SPACE_SYMBOL, 0)

        def getRuleIndex(self):
            return MemInfoParser.RULE_space

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpace" ):
                listener.enterSpace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpace" ):
                listener.exitSpace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpace" ):
                return visitor.visitSpace(self)
            else:
                return visitor.visitChildren(self)




    def space(self):

        localctx = MemInfoParser.SpaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_space)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MemInfoParser.SPACE_SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleDigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_DIGIT(self):
            return self.getToken(MemInfoParser.SINGLE_DIGIT, 0)

        def getRuleIndex(self):
            return MemInfoParser.RULE_singleDigit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleDigit" ):
                listener.enterSingleDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleDigit" ):
                listener.exitSingleDigit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleDigit" ):
                return visitor.visitSingleDigit(self)
            else:
                return visitor.visitChildren(self)




    def singleDigit(self):

        localctx = MemInfoParser.SingleDigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_singleDigit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MemInfoParser.SINGLE_DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






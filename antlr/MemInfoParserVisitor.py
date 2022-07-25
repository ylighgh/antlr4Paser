# Generated from MemInfoParser.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MemInfoParser import MemInfoParser
else:
    from MemInfoParser import MemInfoParser

# This class defines a complete generic visitor for a parse tree produced by MemInfoParser.

class MemInfoParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MemInfoParser#prog.
    def visitProg(self, ctx:MemInfoParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#nameStat.
    def visitNameStat(self, ctx:MemInfoParser.NameStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#unitStat.
    def visitUnitStat(self, ctx:MemInfoParser.UnitStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#sizeStatHandler.
    def visitSizeStatHandler(self, ctx:MemInfoParser.SizeStatHandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#nameRule.
    def visitNameRule(self, ctx:MemInfoParser.NameRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#unitRule.
    def visitUnitRule(self, ctx:MemInfoParser.UnitRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#colon.
    def visitColon(self, ctx:MemInfoParser.ColonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#dataType.
    def visitDataType(self, ctx:MemInfoParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#memAvailable.
    def visitMemAvailable(self, ctx:MemInfoParser.MemAvailableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#memSizeRule.
    def visitMemSizeRule(self, ctx:MemInfoParser.MemSizeRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#leastOneDigit.
    def visitLeastOneDigit(self, ctx:MemInfoParser.LeastOneDigitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#spaces.
    def visitSpaces(self, ctx:MemInfoParser.SpacesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#space.
    def visitSpace(self, ctx:MemInfoParser.SpaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemInfoParser#singleDigit.
    def visitSingleDigit(self, ctx:MemInfoParser.SingleDigitContext):
        return self.visitChildren(ctx)



del MemInfoParser
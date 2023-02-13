# Generated from LTL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LTLParser import LTLParser
else:
    from LTLParser import LTLParser

# This class defines a complete generic visitor for a parse tree produced by LTLParser.

class LTLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LTLParser#Evaluation.
    def visitEvaluation(self, ctx:LTLParser.EvaluationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Disjunction.
    def visitDisjunction(self, ctx:LTLParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Implies.
    def visitImplies(self, ctx:LTLParser.ImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Negation.
    def visitNegation(self, ctx:LTLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Next.
    def visitNext(self, ctx:LTLParser.NextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Eventually.
    def visitEventually(self, ctx:LTLParser.EventuallyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Conjunction.
    def visitConjunction(self, ctx:LTLParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Grouping.
    def visitGrouping(self, ctx:LTLParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Always.
    def visitAlways(self, ctx:LTLParser.AlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Release.
    def visitRelease(self, ctx:LTLParser.ReleaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#Until.
    def visitUntil(self, ctx:LTLParser.UntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LTLParser#atomExpr.
    def visitAtomExpr(self, ctx:LTLParser.AtomExprContext):
        return self.visitChildren(ctx)



del LTLParser
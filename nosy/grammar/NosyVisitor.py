# Generated from ./nosy/grammar/Nosy.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NosyParser import NosyParser
else:
    from NosyParser import NosyParser

# This class defines a complete generic visitor for a parse tree produced by NosyParser.

class NosyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NosyParser#prog.
    def visitProg(self, ctx:NosyParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#query.
    def visitQuery(self, ctx:NosyParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#find_spec.
    def visitFind_spec(self, ctx:NosyParser.Find_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#find_rel.
    def visitFind_rel(self, ctx:NosyParser.Find_relContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#find_elem.
    def visitFind_elem(self, ctx:NosyParser.Find_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#aggregate.
    def visitAggregate(self, ctx:NosyParser.AggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#aggregate_fn_name.
    def visitAggregate_fn_name(self, ctx:NosyParser.Aggregate_fn_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#fn_arg.
    def visitFn_arg(self, ctx:NosyParser.Fn_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#variable.
    def visitVariable(self, ctx:NosyParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#where_clauses.
    def visitWhere_clauses(self, ctx:NosyParser.Where_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#and_clause.
    def visitAnd_clause(self, ctx:NosyParser.And_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#not_clause.
    def visitNot_clause(self, ctx:NosyParser.Not_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#not_join_clause.
    def visitNot_join_clause(self, ctx:NosyParser.Not_join_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#or_clause.
    def visitOr_clause(self, ctx:NosyParser.Or_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#or_join_clause.
    def visitOr_join_clause(self, ctx:NosyParser.Or_join_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#expression_clause.
    def visitExpression_clause(self, ctx:NosyParser.Expression_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#clause.
    def visitClause(self, ctx:NosyParser.ClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#data_pattern.
    def visitData_pattern(self, ctx:NosyParser.Data_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#entity_spec.
    def visitEntity_spec(self, ctx:NosyParser.Entity_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#value_spec.
    def visitValue_spec(self, ctx:NosyParser.Value_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#attribute_name.
    def visitAttribute_name(self, ctx:NosyParser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#constant.
    def visitConstant(self, ctx:NosyParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#range_predicate.
    def visitRange_predicate(self, ctx:NosyParser.Range_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#range_predicate_symbol.
    def visitRange_predicate_symbol(self, ctx:NosyParser.Range_predicate_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#pred_expr.
    def visitPred_expr(self, ctx:NosyParser.Pred_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#fn_expr.
    def visitFn_expr(self, ctx:NosyParser.Fn_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#fn.
    def visitFn(self, ctx:NosyParser.FnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#binding.
    def visitBinding(self, ctx:NosyParser.BindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#bind_scalar.
    def visitBind_scalar(self, ctx:NosyParser.Bind_scalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NosyParser#bind_tuple.
    def visitBind_tuple(self, ctx:NosyParser.Bind_tupleContext):
        return self.visitChildren(ctx)



del NosyParser
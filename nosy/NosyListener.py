# Generated from ./nosy/grammar/Nosy.g4 by ANTLR 4.9.3
from antlr4 import ParseTreeListener
from nosy.grammar.NosyParser import NosyParser

# This class defines a complete listener for a parse tree produced by NosyParser.


class NosyListener(ParseTreeListener):

    # Enter a parse tree produced by NosyParser#prog.
    def enterProg(self, ctx: NosyParser.ProgContext):
        pass

    # Exit a parse tree produced by NosyParser#prog.
    def exitProg(self, ctx: NosyParser.ProgContext):
        pass

    # Enter a parse tree produced by NosyParser#query.
    def enterQuery(self, ctx: NosyParser.QueryContext):
        pass

    # Exit a parse tree produced by NosyParser#query.
    def exitQuery(self, ctx: NosyParser.QueryContext):
        pass

    # Enter a parse tree produced by NosyParser#find_spec.
    def enterFind_spec(self, ctx: NosyParser.Find_specContext):
        pass

    # Exit a parse tree produced by NosyParser#find_spec.
    def exitFind_spec(self, ctx: NosyParser.Find_specContext):
        pass

    # Enter a parse tree produced by NosyParser#find_rel.
    def enterFind_rel(self, ctx: NosyParser.Find_relContext):
        pass

    # Exit a parse tree produced by NosyParser#find_rel.
    def exitFind_rel(self, ctx: NosyParser.Find_relContext):
        pass

    # Enter a parse tree produced by NosyParser#find_elem.
    def enterFind_elem(self, ctx: NosyParser.Find_elemContext):
        pass

    # Exit a parse tree produced by NosyParser#find_elem.
    def exitFind_elem(self, ctx: NosyParser.Find_elemContext):
        pass

    # Enter a parse tree produced by NosyParser#aggregate.
    def enterAggregate(self, ctx: NosyParser.AggregateContext):
        pass

    # Exit a parse tree produced by NosyParser#aggregate.
    def exitAggregate(self, ctx: NosyParser.AggregateContext):
        pass

    # Enter a parse tree produced by NosyParser#aggregate_fn_name.
    def enterAggregate_fn_name(self, ctx: NosyParser.Aggregate_fn_nameContext):
        pass

    # Exit a parse tree produced by NosyParser#aggregate_fn_name.
    def exitAggregate_fn_name(self, ctx: NosyParser.Aggregate_fn_nameContext):
        pass

    # Enter a parse tree produced by NosyParser#fn_arg.
    def enterFn_arg(self, ctx: NosyParser.Fn_argContext):
        pass

    # Exit a parse tree produced by NosyParser#fn_arg.
    def exitFn_arg(self, ctx: NosyParser.Fn_argContext):
        pass

    # Enter a parse tree produced by NosyParser#variable.
    def enterVariable(self, ctx: NosyParser.VariableContext):
        pass

    # Exit a parse tree produced by NosyParser#variable.
    def exitVariable(self, ctx: NosyParser.VariableContext):
        pass

    # Enter a parse tree produced by NosyParser#where_clauses.
    def enterWhere_clauses(self, ctx: NosyParser.Where_clausesContext):
        pass

    # Exit a parse tree produced by NosyParser#where_clauses.
    def exitWhere_clauses(self, ctx: NosyParser.Where_clausesContext):
        pass

    # Enter a parse tree produced by NosyParser#and_clause.
    def enterAnd_clause(self, ctx: NosyParser.And_clauseContext):
        pass

    # Exit a parse tree produced by NosyParser#and_clause.
    def exitAnd_clause(self, ctx: NosyParser.And_clauseContext):
        pass

    # Enter a parse tree produced by NosyParser#not_clause.
    def enterNot_clause(self, ctx: NosyParser.Not_clauseContext):
        pass

    # Exit a parse tree produced by NosyParser#not_clause.
    def exitNot_clause(self, ctx: NosyParser.Not_clauseContext):
        pass

    # Enter a parse tree produced by NosyParser#not_join_clause.
    def enterNot_join_clause(self, ctx: NosyParser.Not_join_clauseContext):
        pass

    # Exit a parse tree produced by NosyParser#not_join_clause.
    def exitNot_join_clause(self, ctx: NosyParser.Not_join_clauseContext):
        pass

    # Enter a parse tree produced by NosyParser#or_clause.
    def enterOr_clause(self, ctx: NosyParser.Or_clauseContext):
        pass

    # Exit a parse tree produced by NosyParser#or_clause.
    def exitOr_clause(self, ctx: NosyParser.Or_clauseContext):
        pass

    # Enter a parse tree produced by NosyParser#or_join_clause.
    def enterOr_join_clause(self, ctx: NosyParser.Or_join_clauseContext):
        pass

    # Exit a parse tree produced by NosyParser#or_join_clause.
    def exitOr_join_clause(self, ctx: NosyParser.Or_join_clauseContext):
        pass

    # Enter a parse tree produced by NosyParser#expression_clause.
    def enterExpression_clause(self, ctx: NosyParser.Expression_clauseContext):
        pass

    # Exit a parse tree produced by NosyParser#expression_clause.
    def exitExpression_clause(self, ctx: NosyParser.Expression_clauseContext):
        pass

    # Enter a parse tree produced by NosyParser#clause.
    def enterClause(self, ctx: NosyParser.ClauseContext):
        pass

    # Exit a parse tree produced by NosyParser#clause.
    def exitClause(self, ctx: NosyParser.ClauseContext):
        pass

    # Enter a parse tree produced by NosyParser#data_pattern.
    def enterData_pattern(self, ctx: NosyParser.Data_patternContext):
        pass

    # Exit a parse tree produced by NosyParser#data_pattern.
    def exitData_pattern(self, ctx: NosyParser.Data_patternContext):
        pass

    # Enter a parse tree produced by NosyParser#attribute_name.
    def enterAttribute_name(self, ctx: NosyParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by NosyParser#attribute_name.
    def exitAttribute_name(self, ctx: NosyParser.Attribute_nameContext):
        pass

    # Enter a parse tree produced by NosyParser#constant.
    def enterConstant(self, ctx: NosyParser.ConstantContext):
        pass

    # Exit a parse tree produced by NosyParser#constant.
    def exitConstant(self, ctx: NosyParser.ConstantContext):
        pass

    # Enter a parse tree produced by NosyParser#pred_expr.
    def enterPred_expr(self, ctx: NosyParser.Pred_exprContext):
        pass

    # Exit a parse tree produced by NosyParser#pred_expr.
    def exitPred_expr(self, ctx: NosyParser.Pred_exprContext):
        pass

    # Enter a parse tree produced by NosyParser#pred.
    def enterPred(self, ctx: NosyParser.PredContext):
        pass

    # Exit a parse tree produced by NosyParser#pred.
    def exitPred(self, ctx: NosyParser.PredContext):
        pass

    # Enter a parse tree produced by NosyParser#range_predicate.
    def enterRange_predicate(self, ctx: NosyParser.Range_predicateContext):
        pass

    # Exit a parse tree produced by NosyParser#range_predicate.
    def exitRange_predicate(self, ctx: NosyParser.Range_predicateContext):
        pass

    # Enter a parse tree produced by NosyParser#fn_expr.
    def enterFn_expr(self, ctx: NosyParser.Fn_exprContext):
        pass

    # Exit a parse tree produced by NosyParser#fn_expr.
    def exitFn_expr(self, ctx: NosyParser.Fn_exprContext):
        pass

    # Enter a parse tree produced by NosyParser#fn.
    def enterFn(self, ctx: NosyParser.FnContext):
        pass

    # Exit a parse tree produced by NosyParser#fn.
    def exitFn(self, ctx: NosyParser.FnContext):
        pass

    # Enter a parse tree produced by NosyParser#binding.
    def enterBinding(self, ctx: NosyParser.BindingContext):
        pass

    # Exit a parse tree produced by NosyParser#binding.
    def exitBinding(self, ctx: NosyParser.BindingContext):
        pass

    # Enter a parse tree produced by NosyParser#bind_scalar.
    def enterBind_scalar(self, ctx: NosyParser.Bind_scalarContext):
        pass

    # Exit a parse tree produced by NosyParser#bind_scalar.
    def exitBind_scalar(self, ctx: NosyParser.Bind_scalarContext):
        pass

    # Enter a parse tree produced by NosyParser#bind_tuple.
    def enterBind_tuple(self, ctx: NosyParser.Bind_tupleContext):
        pass

    # Exit a parse tree produced by NosyParser#bind_tuple.
    def exitBind_tuple(self, ctx: NosyParser.Bind_tupleContext):
        pass


del NosyParser

from typing import List, Union
from dataclasses import dataclass, field
from antlr4 import InputStream, CommonTokenStream
from grammar.NosyLexer import NosyLexer
from grammar.NosyParser import NosyParser
from grammar.NosyVisitor import NosyVisitor

QUERY_01 = '[:find ?e ?e1 ?e2 :where [?e Character/name "Zuko"]]'


@dataclass
class NosyClauseNode:
    text: str


@dataclass
class NosyDataPatternNode:
    entity: Union[str, int, None]
    attribute: str
    value: Union[str, int, bool, float, None]


@dataclass
class NosyQueryNode:
    find_vars: List[str] = field(default_factory=list)
    clauses: List[NosyClauseNode] = field(default_factory=list)


@dataclass
class NosyProgramNode:
    """Root node for the query AST

    Attributes
    ----------
    queries: List[NosyQueryNode]
        Query defined in the program
    """
    queries: List[NosyQueryNode] = field(default_factory=list)


class QuerryProcessingError(Exception):
    """Error raised when processing a query's abstract syntax tree"""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message: str = message

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message


class CustomVisitor(NosyVisitor):

    def visit(self, tree) -> NosyProgramNode:
        return super().visit(tree)

    def visitProg(self, ctx: NosyParser.ProgContext) -> NosyProgramNode:
        if ctx.children:
            node = NosyProgramNode()
            for child in ctx.children:
                node.queries.append(self.visitQuery(child))
            return node
        raise QuerryProcessingError("Missing Node in Program AST")

    def visitQuery(self, ctx: NosyParser.QueryContext) -> NosyQueryNode:
        return NosyQueryNode(
            find_vars=self.visitFind_spec(ctx.find_spec()),
            clauses=self.visitWhere_clauses(ctx.where_clauses())
        )

    def visitWhere_clauses(self, ctx: NosyParser.Where_clausesContext) -> List[NosyClauseNode]:
        clause_nodes: List[NosyClauseNode] = []
        clauses = ctx.clause()
        if clauses:
            if isinstance(clauses, list):
                for c in clauses:
                    clause_nodes.append(self.visitClause(c))
            else:
                clause_nodes.append(self.visitClause(clauses))
        return clause_nodes

    def visitClause(self, ctx: NosyParser.ClauseContext):
        if ctx.expression_clause():
            return self.visitExpression_clause(ctx.expression_clause())
        return super().visitClause(ctx)

    def visitExpression_clause(self, ctx: NosyParser.Expression_clauseContext):
        if ctx.data_pattern:
            return self.visitData_pattern(ctx.data_pattern())
        return super().visitExpression_clause(ctx)

    def visitFind_spec(self, ctx: NosyParser.Find_specContext) -> List[str]:
        return self.visitFind_rel(ctx.find_rel())

    def visitFind_rel(self, ctx: NosyParser.Find_relContext) -> List[str]:
        find_vars: List[str] = []
        find_elem = ctx.find_elem()
        if find_elem:
            if isinstance(find_elem, list):
                for el in find_elem:
                    find_vars.append(self.visitFind_elem(el))
            else:
                find_vars.append(self.visitFind_elem(find_elem))

        return find_vars

    def visitFind_elem(self, ctx: NosyParser.Find_elemContext) -> str:
        return self.visitVariable(ctx.variable())

    def visitVariable(self, ctx: NosyParser.VariableContext) -> str:
        return ctx.getText()

    def visitData_pattern(self, ctx: NosyParser.Data_patternContext) -> NosyDataPatternNode:
        return NosyDataPatternNode(
            entity=self.visitEntity_spec(ctx.entity_spec()),
            attribute=self.visitAttribute_name(ctx.attribute_name()),
            value=self.visitValue_spec(ctx.value_spec()),
        )

    def visitEntity_spec(self, ctx: NosyParser.Entity_specContext) -> Union[str, int, None]:
        if ctx.variable():
            return self.visitVariable(ctx.variable())
        if ctx.UINT():
            return int(ctx.getText())
        else:
            return None

    def visitValue_spec(self, ctx: NosyParser.Value_specContext) -> Union[str, int, bool, float, None]:
        if ctx.variable():
            return self.visitVariable(ctx.variable())
        if ctx.constant():
            return self.visitConstant(ctx.constant())
        else:
            return None

    def visitAttribute_name(self, ctx: NosyParser.Attribute_nameContext) -> str:
        return ctx.getText()

    def visitConstant(self, ctx: NosyParser.ConstantContext) -> Union[int, float, str]:
        text: str = ctx.getText()
        if text.isnumeric():
            return int(text)
        elif text.isdecimal():
            return float(text)
        elif text.lower in ['true', 'false']:
            return bool(text)
        elif len(text) >= 2 and text[0] == '"' and text[-1] == '"':
            return str(text[1:-1])
        raise QuerryProcessingError(f"'{text}' is not a valid constant value")


def parse_nosy_program(query: str) -> NosyProgramNode:
    """Parse a given query string and return the root of the Abstract Syntax Tree"""
    lexer = NosyLexer(InputStream(query))
    token_stream = CommonTokenStream(lexer)
    parser = NosyParser(token_stream)
    tree = parser.prog()
    visitor = CustomVisitor()
    root = visitor.visit(tree)
    return root


def main():
    program = parse_nosy_program(QUERY_01)
    print(program)


if __name__ == "__main__":
    main()

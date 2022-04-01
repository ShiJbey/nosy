# Generated from ./nosy/grammar/Nosy.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("\u0115\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\3\2\3\3\3\3\3\3\5\3D\n\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\5\6\5L\n\5\r\5\16\5M\3\6\3\6\3\7\3\7\3\7\6\7")
        buf.write("U\n\7\r\7\16\7V\3\7\3\7\3\b\3\b\3\b\7\b^\n\b\f\b\16\b")
        buf.write("a\13\b\3\t\3\t\5\te\n\t\3\n\3\n\3\n\3\13\3\13\6\13l\n")
        buf.write("\13\r\13\16\13m\3\f\3\f\3\f\6\fs\n\f\r\f\16\ft\3\f\3\f")
        buf.write("\3\r\3\r\3\r\6\r|\n\r\r\r\16\r}\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\6\16\u0086\n\16\r\16\16\16\u0087\3\16\3\16\6\16")
        buf.write("\u008c\n\16\r\16\16\16\u008d\3\16\3\16\3\17\3\17\3\17")
        buf.write("\6\17\u0095\n\17\r\17\16\17\u0096\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\6\20\u009f\n\20\r\20\16\20\u00a0\3\20\3\20")
        buf.write("\3\20\6\20\u00a6\n\20\r\20\16\20\u00a7\3\20\3\20\3\21")
        buf.write("\3\21\3\21\5\21\u00af\n\21\3\22\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u00b6\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\5\24\u00c1\n\24\3\25\3\25\3\25\5\25\u00c6\n\25\3")
        buf.write("\26\5\26\u00c9\n\26\3\26\3\26\3\26\7\26\u00ce\n\26\f\26")
        buf.write("\16\26\u00d1\13\26\3\26\3\26\3\26\3\26\7\26\u00d7\n\26")
        buf.write("\f\26\16\26\u00da\13\26\7\26\u00dc\n\26\f\26\16\26\u00df")
        buf.write("\13\26\3\27\3\27\3\30\3\30\3\30\3\30\6\30\u00e7\n\30\r")
        buf.write("\30\16\30\u00e8\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\6\33\u00f6\n\33\r\33\16\33\u00f7\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\7\34\u0101\n\34\f\34\16")
        buf.write("\34\u0104\13\34\3\35\3\35\5\35\u0108\n\35\3\36\3\36\3")
        buf.write("\37\3\37\3\37\6\37\u010f\n\37\r\37\16\37\u0110\3\37\3")
        buf.write("\37\3\37\2\2 \2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<\2\4\4\2\30\30\33\34\3\2\22\27")
        buf.write("\2\u0118\2>\3\2\2\2\4@\3\2\2\2\6G\3\2\2\2\bK\3\2\2\2\n")
        buf.write("O\3\2\2\2\fQ\3\2\2\2\16Z\3\2\2\2\20d\3\2\2\2\22f\3\2\2")
        buf.write("\2\24i\3\2\2\2\26o\3\2\2\2\30x\3\2\2\2\32\u0081\3\2\2")
        buf.write("\2\34\u0091\3\2\2\2\36\u009a\3\2\2\2 \u00ae\3\2\2\2\"")
        buf.write("\u00b5\3\2\2\2$\u00b7\3\2\2\2&\u00c0\3\2\2\2(\u00c5\3")
        buf.write("\2\2\2*\u00c8\3\2\2\2,\u00e0\3\2\2\2.\u00e2\3\2\2\2\60")
        buf.write("\u00ed\3\2\2\2\62\u00ef\3\2\2\2\64\u00f1\3\2\2\2\66\u00fd")
        buf.write("\3\2\2\28\u0107\3\2\2\2:\u0109\3\2\2\2<\u010b\3\2\2\2")
        buf.write(">?\5\4\3\2?\3\3\2\2\2@A\7\3\2\2AC\5\6\4\2BD\5\24\13\2")
        buf.write("CB\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\7\4\2\2F\5\3\2\2\2GH")
        buf.write("\7\5\2\2HI\5\b\5\2I\7\3\2\2\2JL\5\n\6\2KJ\3\2\2\2LM\3")
        buf.write("\2\2\2MK\3\2\2\2MN\3\2\2\2N\t\3\2\2\2OP\5\22\n\2P\13\3")
        buf.write("\2\2\2QR\7\3\2\2RT\5\16\b\2SU\5\20\t\2TS\3\2\2\2UV\3\2")
        buf.write("\2\2VT\3\2\2\2VW\3\2\2\2WX\3\2\2\2XY\7\4\2\2Y\r\3\2\2")
        buf.write("\2Z_\7\35\2\2[\\\7\6\2\2\\^\7\35\2\2][\3\2\2\2^a\3\2\2")
        buf.write("\2_]\3\2\2\2_`\3\2\2\2`\17\3\2\2\2a_\3\2\2\2be\5\22\n")
        buf.write("\2ce\5,\27\2db\3\2\2\2dc\3\2\2\2e\21\3\2\2\2fg\7\7\2\2")
        buf.write("gh\7\35\2\2h\23\3\2\2\2ik\7\b\2\2jl\5\"\22\2kj\3\2\2\2")
        buf.write("lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2n\25\3\2\2\2op\7\3\2\2p")
        buf.write("r\7\t\2\2qs\5\"\22\2rq\3\2\2\2st\3\2\2\2tr\3\2\2\2tu\3")
        buf.write("\2\2\2uv\3\2\2\2vw\7\4\2\2w\27\3\2\2\2xy\7\3\2\2y{\7\n")
        buf.write("\2\2z|\5\"\22\2{z\3\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2")
        buf.write("\2~\177\3\2\2\2\177\u0080\7\4\2\2\u0080\31\3\2\2\2\u0081")
        buf.write("\u0082\7\3\2\2\u0082\u0083\7\13\2\2\u0083\u0085\7\3\2")
        buf.write("\2\u0084\u0086\5\22\n\2\u0085\u0084\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0089\u008b\7\4\2\2\u008a\u008c\5\"\22")
        buf.write("\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0090\7\4\2\2\u0090\33\3\2\2\2\u0091\u0092\7\3\2\2\u0092")
        buf.write("\u0094\7\f\2\2\u0093\u0095\5\"\22\2\u0094\u0093\3\2\2")
        buf.write("\2\u0095\u0096\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\7\4\2\2\u0099")
        buf.write("\35\3\2\2\2\u009a\u009b\7\3\2\2\u009b\u009c\7\r\2\2\u009c")
        buf.write("\u009e\7\3\2\2\u009d\u009f\5\22\n\2\u009e\u009d\3\2\2")
        buf.write("\2\u009f\u00a0\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a5\7\4\2\2\u00a3")
        buf.write("\u00a6\5\"\22\2\u00a4\u00a6\5\26\f\2\u00a5\u00a3\3\2\2")
        buf.write("\2\u00a5\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00aa\7\4\2\2\u00aa\37\3\2\2\2\u00ab\u00af\5$\23\2\u00ac")
        buf.write("\u00af\5\62\32\2\u00ad\u00af\5\64\33\2\u00ae\u00ab\3\2")
        buf.write("\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af!\3")
        buf.write("\2\2\2\u00b0\u00b6\5\30\r\2\u00b1\u00b6\5\32\16\2\u00b2")
        buf.write("\u00b6\5\34\17\2\u00b3\u00b6\5\36\20\2\u00b4\u00b6\5 ")
        buf.write("\21\2\u00b5\u00b0\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b5\u00b2")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write("#\3\2\2\2\u00b7\u00b8\7\3\2\2\u00b8\u00b9\5&\24\2\u00b9")
        buf.write("\u00ba\5*\26\2\u00ba\u00bb\5(\25\2\u00bb\u00bc\7\4\2\2")
        buf.write("\u00bc%\3\2\2\2\u00bd\u00c1\5\22\n\2\u00be\u00c1\7\31")
        buf.write("\2\2\u00bf\u00c1\7\6\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\'\3\2\2\2\u00c2\u00c6")
        buf.write("\5\22\n\2\u00c3\u00c6\5,\27\2\u00c4\u00c6\7\6\2\2\u00c5")
        buf.write("\u00c2\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2")
        buf.write("\u00c6)\3\2\2\2\u00c7\u00c9\7\16\2\2\u00c8\u00c7\3\2\2")
        buf.write("\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cf")
        buf.write("\7\35\2\2\u00cb\u00cc\7\6\2\2\u00cc\u00ce\7\35\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\u00dd\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d2\u00d3\7\17\2\2\u00d3\u00d8\7\35\2\2\u00d4")
        buf.write("\u00d5\7\6\2\2\u00d5\u00d7\7\35\2\2\u00d6\u00d4\3\2\2")
        buf.write("\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00db")
        buf.write("\u00d2\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de+\3\2\2\2\u00df\u00dd\3\2\2")
        buf.write("\2\u00e0\u00e1\t\2\2\2\u00e1-\3\2\2\2\u00e2\u00e3\7\3")
        buf.write("\2\2\u00e3\u00e4\7\20\2\2\u00e4\u00e6\5\60\31\2\u00e5")
        buf.write("\u00e7\5\20\t\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2")
        buf.write("\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea")
        buf.write("\3\2\2\2\u00ea\u00eb\7\21\2\2\u00eb\u00ec\7\4\2\2\u00ec")
        buf.write("/\3\2\2\2\u00ed\u00ee\t\3\2\2\u00ee\61\3\2\2\2\u00ef\u00f0")
        buf.write("\5.\30\2\u00f0\63\3\2\2\2\u00f1\u00f2\7\3\2\2\u00f2\u00f3")
        buf.write("\7\20\2\2\u00f3\u00f5\5\66\34\2\u00f4\u00f6\5\20\t\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f5\3\2\2\2")
        buf.write("\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\7")
        buf.write("\21\2\2\u00fa\u00fb\58\35\2\u00fb\u00fc\7\4\2\2\u00fc")
        buf.write("\65\3\2\2\2\u00fd\u0102\7\35\2\2\u00fe\u00ff\7\6\2\2\u00ff")
        buf.write("\u0101\7\35\2\2\u0100\u00fe\3\2\2\2\u0101\u0104\3\2\2")
        buf.write("\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\67\3")
        buf.write("\2\2\2\u0104\u0102\3\2\2\2\u0105\u0108\5:\36\2\u0106\u0108")
        buf.write("\5<\37\2\u0107\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u0108")
        buf.write("9\3\2\2\2\u0109\u010a\5\22\n\2\u010a;\3\2\2\2\u010b\u010e")
        buf.write("\7\3\2\2\u010c\u010f\5\22\n\2\u010d\u010f\7\6\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3")
        buf.write("\2\2\2\u0112\u0113\7\4\2\2\u0113=\3\2\2\2\36CMV_dmt}\u0087")
        buf.write("\u008d\u0096\u00a0\u00a5\u00a7\u00ae\u00b5\u00c0\u00c5")
        buf.write("\u00c8\u00cf\u00d8\u00dd\u00e8\u00f7\u0102\u0107\u010e")
        buf.write("\u0110")
        return buf.getvalue()


class NosyParser ( Parser ):

    grammarFileName = "Nosy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "':find'", "'_'", "'?'", 
                     "':where'", "'and'", "'not'", "'not-join'", "'or'", 
                     "'or-join'", "':'", "'/'", "'('", "')'", "'='", "'!='", 
                     "'<='", "'<'", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "UINT", "INT", 
                      "BOOLEAN", "STRING", "SYMBOL", "WS" ]

    RULE_prog = 0
    RULE_query = 1
    RULE_find_spec = 2
    RULE_find_rel = 3
    RULE_find_elem = 4
    RULE_aggregate = 5
    RULE_aggregate_fn_name = 6
    RULE_fn_arg = 7
    RULE_variable = 8
    RULE_where_clauses = 9
    RULE_and_clause = 10
    RULE_not_clause = 11
    RULE_not_join_clause = 12
    RULE_or_clause = 13
    RULE_or_join_clause = 14
    RULE_expression_clause = 15
    RULE_clause = 16
    RULE_data_pattern = 17
    RULE_entity_spec = 18
    RULE_value_spec = 19
    RULE_attribute_name = 20
    RULE_constant = 21
    RULE_range_predicate = 22
    RULE_range_predicate_symbol = 23
    RULE_pred_expr = 24
    RULE_fn_expr = 25
    RULE_fn = 26
    RULE_binding = 27
    RULE_bind_scalar = 28
    RULE_bind_tuple = 29

    ruleNames =  [ "prog", "query", "find_spec", "find_rel", "find_elem", 
                   "aggregate", "aggregate_fn_name", "fn_arg", "variable", 
                   "where_clauses", "and_clause", "not_clause", "not_join_clause", 
                   "or_clause", "or_join_clause", "expression_clause", "clause", 
                   "data_pattern", "entity_spec", "value_spec", "attribute_name", 
                   "constant", "range_predicate", "range_predicate_symbol", 
                   "pred_expr", "fn_expr", "fn", "binding", "bind_scalar", 
                   "bind_tuple" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    NUMBER=22
    UINT=23
    INT=24
    BOOLEAN=25
    STRING=26
    SYMBOL=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def query(self):
            return self.getTypedRuleContext(NosyParser.QueryContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_prog

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

        localctx = NosyParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.query()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def find_spec(self):
            return self.getTypedRuleContext(NosyParser.Find_specContext,0)


        def where_clauses(self):
            return self.getTypedRuleContext(NosyParser.Where_clausesContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = NosyParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(NosyParser.T__0)
            self.state = 63
            self.find_spec()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NosyParser.T__5:
                self.state = 64
                self.where_clauses()


            self.state = 67
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Find_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def find_rel(self):
            return self.getTypedRuleContext(NosyParser.Find_relContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_find_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFind_spec" ):
                listener.enterFind_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFind_spec" ):
                listener.exitFind_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFind_spec" ):
                return visitor.visitFind_spec(self)
            else:
                return visitor.visitChildren(self)




    def find_spec(self):

        localctx = NosyParser.Find_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_find_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(NosyParser.T__2)
            self.state = 70
            self.find_rel()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Find_relContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def find_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.Find_elemContext)
            else:
                return self.getTypedRuleContext(NosyParser.Find_elemContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_find_rel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFind_rel" ):
                listener.enterFind_rel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFind_rel" ):
                listener.exitFind_rel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFind_rel" ):
                return visitor.visitFind_rel(self)
            else:
                return visitor.visitChildren(self)




    def find_rel(self):

        localctx = NosyParser.Find_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_find_rel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.find_elem()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Find_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(NosyParser.VariableContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_find_elem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFind_elem" ):
                listener.enterFind_elem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFind_elem" ):
                listener.exitFind_elem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFind_elem" ):
                return visitor.visitFind_elem(self)
            else:
                return visitor.visitChildren(self)




    def find_elem(self):

        localctx = NosyParser.Find_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_find_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregate_fn_name(self):
            return self.getTypedRuleContext(NosyParser.Aggregate_fn_nameContext,0)


        def fn_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.Fn_argContext)
            else:
                return self.getTypedRuleContext(NosyParser.Fn_argContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_aggregate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregate" ):
                listener.enterAggregate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregate" ):
                listener.exitAggregate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregate" ):
                return visitor.visitAggregate(self)
            else:
                return visitor.visitChildren(self)




    def aggregate(self):

        localctx = NosyParser.AggregateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_aggregate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(NosyParser.T__0)
            self.state = 80
            self.aggregate_fn_name()
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.fn_arg()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NosyParser.T__4) | (1 << NosyParser.NUMBER) | (1 << NosyParser.BOOLEAN) | (1 << NosyParser.STRING))) != 0)):
                    break

            self.state = 86
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregate_fn_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(NosyParser.SYMBOL)
            else:
                return self.getToken(NosyParser.SYMBOL, i)

        def getRuleIndex(self):
            return NosyParser.RULE_aggregate_fn_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregate_fn_name" ):
                listener.enterAggregate_fn_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregate_fn_name" ):
                listener.exitAggregate_fn_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregate_fn_name" ):
                return visitor.visitAggregate_fn_name(self)
            else:
                return visitor.visitChildren(self)




    def aggregate_fn_name(self):

        localctx = NosyParser.Aggregate_fn_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aggregate_fn_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(NosyParser.SYMBOL)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NosyParser.T__3:
                self.state = 89
                self.match(NosyParser.T__3)
                self.state = 90
                self.match(NosyParser.SYMBOL)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fn_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(NosyParser.VariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(NosyParser.ConstantContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_fn_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFn_arg" ):
                listener.enterFn_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFn_arg" ):
                listener.exitFn_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFn_arg" ):
                return visitor.visitFn_arg(self)
            else:
                return visitor.visitChildren(self)




    def fn_arg(self):

        localctx = NosyParser.Fn_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fn_arg)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NosyParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.variable()
                pass
            elif token in [NosyParser.NUMBER, NosyParser.BOOLEAN, NosyParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self):
            return self.getToken(NosyParser.SYMBOL, 0)

        def getRuleIndex(self):
            return NosyParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = NosyParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(NosyParser.T__4)
            self.state = 101
            self.match(NosyParser.SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_clausesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.ClauseContext)
            else:
                return self.getTypedRuleContext(NosyParser.ClauseContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_where_clauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_clauses" ):
                listener.enterWhere_clauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_clauses" ):
                listener.exitWhere_clauses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_clauses" ):
                return visitor.visitWhere_clauses(self)
            else:
                return visitor.visitChildren(self)




    def where_clauses(self):

        localctx = NosyParser.Where_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_where_clauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(NosyParser.T__5)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.clause()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.ClauseContext)
            else:
                return self.getTypedRuleContext(NosyParser.ClauseContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_and_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_clause" ):
                listener.enterAnd_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_clause" ):
                listener.exitAnd_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_clause" ):
                return visitor.visitAnd_clause(self)
            else:
                return visitor.visitChildren(self)




    def and_clause(self):

        localctx = NosyParser.And_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_and_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(NosyParser.T__0)
            self.state = 110
            self.match(NosyParser.T__6)
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 111
                self.clause()
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__0):
                    break

            self.state = 116
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.ClauseContext)
            else:
                return self.getTypedRuleContext(NosyParser.ClauseContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_not_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_clause" ):
                listener.enterNot_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_clause" ):
                listener.exitNot_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_clause" ):
                return visitor.visitNot_clause(self)
            else:
                return visitor.visitChildren(self)




    def not_clause(self):

        localctx = NosyParser.Not_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_not_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(NosyParser.T__0)
            self.state = 119
            self.match(NosyParser.T__7)
            self.state = 121 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120
                self.clause()
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__0):
                    break

            self.state = 125
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_join_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.VariableContext)
            else:
                return self.getTypedRuleContext(NosyParser.VariableContext,i)


        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.ClauseContext)
            else:
                return self.getTypedRuleContext(NosyParser.ClauseContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_not_join_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_join_clause" ):
                listener.enterNot_join_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_join_clause" ):
                listener.exitNot_join_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_join_clause" ):
                return visitor.visitNot_join_clause(self)
            else:
                return visitor.visitChildren(self)




    def not_join_clause(self):

        localctx = NosyParser.Not_join_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_not_join_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(NosyParser.T__0)
            self.state = 128
            self.match(NosyParser.T__8)
            self.state = 129
            self.match(NosyParser.T__0)
            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.variable()
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__4):
                    break

            self.state = 135
            self.match(NosyParser.T__1)
            self.state = 137 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 136
                self.clause()
                self.state = 139 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__0):
                    break

            self.state = 141
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.ClauseContext)
            else:
                return self.getTypedRuleContext(NosyParser.ClauseContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_or_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_clause" ):
                listener.enterOr_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_clause" ):
                listener.exitOr_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_clause" ):
                return visitor.visitOr_clause(self)
            else:
                return visitor.visitChildren(self)




    def or_clause(self):

        localctx = NosyParser.Or_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_or_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(NosyParser.T__0)
            self.state = 144
            self.match(NosyParser.T__9)
            self.state = 146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 145
                self.clause()
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__0):
                    break

            self.state = 150
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_join_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.VariableContext)
            else:
                return self.getTypedRuleContext(NosyParser.VariableContext,i)


        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.ClauseContext)
            else:
                return self.getTypedRuleContext(NosyParser.ClauseContext,i)


        def and_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.And_clauseContext)
            else:
                return self.getTypedRuleContext(NosyParser.And_clauseContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_or_join_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_join_clause" ):
                listener.enterOr_join_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_join_clause" ):
                listener.exitOr_join_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_join_clause" ):
                return visitor.visitOr_join_clause(self)
            else:
                return visitor.visitChildren(self)




    def or_join_clause(self):

        localctx = NosyParser.Or_join_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_or_join_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(NosyParser.T__0)
            self.state = 153
            self.match(NosyParser.T__10)
            self.state = 154
            self.match(NosyParser.T__0)
            self.state = 156 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 155
                self.variable()
                self.state = 158 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__4):
                    break

            self.state = 160
            self.match(NosyParser.T__1)
            self.state = 163 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 163
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 161
                    self.clause()
                    pass

                elif la_ == 2:
                    self.state = 162
                    self.and_clause()
                    pass


                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__0):
                    break

            self.state = 167
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_pattern(self):
            return self.getTypedRuleContext(NosyParser.Data_patternContext,0)


        def pred_expr(self):
            return self.getTypedRuleContext(NosyParser.Pred_exprContext,0)


        def fn_expr(self):
            return self.getTypedRuleContext(NosyParser.Fn_exprContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_expression_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_clause" ):
                listener.enterExpression_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_clause" ):
                listener.exitExpression_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_clause" ):
                return visitor.visitExpression_clause(self)
            else:
                return visitor.visitChildren(self)




    def expression_clause(self):

        localctx = NosyParser.Expression_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression_clause)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.data_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.pred_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.fn_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_clause(self):
            return self.getTypedRuleContext(NosyParser.Not_clauseContext,0)


        def not_join_clause(self):
            return self.getTypedRuleContext(NosyParser.Not_join_clauseContext,0)


        def or_clause(self):
            return self.getTypedRuleContext(NosyParser.Or_clauseContext,0)


        def or_join_clause(self):
            return self.getTypedRuleContext(NosyParser.Or_join_clauseContext,0)


        def expression_clause(self):
            return self.getTypedRuleContext(NosyParser.Expression_clauseContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClause" ):
                listener.enterClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClause" ):
                listener.exitClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClause" ):
                return visitor.visitClause(self)
            else:
                return visitor.visitChildren(self)




    def clause(self):

        localctx = NosyParser.ClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_clause)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.not_clause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.not_join_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.or_clause()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.or_join_clause()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.expression_clause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entity_spec(self):
            return self.getTypedRuleContext(NosyParser.Entity_specContext,0)


        def attribute_name(self):
            return self.getTypedRuleContext(NosyParser.Attribute_nameContext,0)


        def value_spec(self):
            return self.getTypedRuleContext(NosyParser.Value_specContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_data_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_pattern" ):
                listener.enterData_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_pattern" ):
                listener.exitData_pattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_pattern" ):
                return visitor.visitData_pattern(self)
            else:
                return visitor.visitChildren(self)




    def data_pattern(self):

        localctx = NosyParser.Data_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_data_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(NosyParser.T__0)
            self.state = 182
            self.entity_spec()
            self.state = 183
            self.attribute_name()
            self.state = 184
            self.value_spec()
            self.state = 185
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Entity_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(NosyParser.VariableContext,0)


        def UINT(self):
            return self.getToken(NosyParser.UINT, 0)

        def getRuleIndex(self):
            return NosyParser.RULE_entity_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity_spec" ):
                listener.enterEntity_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity_spec" ):
                listener.exitEntity_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity_spec" ):
                return visitor.visitEntity_spec(self)
            else:
                return visitor.visitChildren(self)




    def entity_spec(self):

        localctx = NosyParser.Entity_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_entity_spec)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NosyParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.variable()
                pass
            elif token in [NosyParser.UINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(NosyParser.UINT)
                pass
            elif token in [NosyParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.match(NosyParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(NosyParser.VariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(NosyParser.ConstantContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_value_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_spec" ):
                listener.enterValue_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_spec" ):
                listener.exitValue_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_spec" ):
                return visitor.visitValue_spec(self)
            else:
                return visitor.visitChildren(self)




    def value_spec(self):

        localctx = NosyParser.Value_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_value_spec)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NosyParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.variable()
                pass
            elif token in [NosyParser.NUMBER, NosyParser.BOOLEAN, NosyParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.constant()
                pass
            elif token in [NosyParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.match(NosyParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(NosyParser.SYMBOL)
            else:
                return self.getToken(NosyParser.SYMBOL, i)

        def getRuleIndex(self):
            return NosyParser.RULE_attribute_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_name" ):
                listener.enterAttribute_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_name" ):
                listener.exitAttribute_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_name" ):
                return visitor.visitAttribute_name(self)
            else:
                return visitor.visitChildren(self)




    def attribute_name(self):

        localctx = NosyParser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_attribute_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NosyParser.T__11:
                self.state = 197
                self.match(NosyParser.T__11)


            self.state = 200
            self.match(NosyParser.SYMBOL)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 201
                    self.match(NosyParser.T__3)
                    self.state = 202
                    self.match(NosyParser.SYMBOL) 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NosyParser.T__12:
                self.state = 208
                self.match(NosyParser.T__12)
                self.state = 209
                self.match(NosyParser.SYMBOL)
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 210
                        self.match(NosyParser.T__3)
                        self.state = 211
                        self.match(NosyParser.SYMBOL) 
                    self.state = 216
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(NosyParser.BOOLEAN, 0)

        def NUMBER(self):
            return self.getToken(NosyParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(NosyParser.STRING, 0)

        def getRuleIndex(self):
            return NosyParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = NosyParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NosyParser.NUMBER) | (1 << NosyParser.BOOLEAN) | (1 << NosyParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_predicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def range_predicate_symbol(self):
            return self.getTypedRuleContext(NosyParser.Range_predicate_symbolContext,0)


        def fn_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.Fn_argContext)
            else:
                return self.getTypedRuleContext(NosyParser.Fn_argContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_range_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_predicate" ):
                listener.enterRange_predicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_predicate" ):
                listener.exitRange_predicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_predicate" ):
                return visitor.visitRange_predicate(self)
            else:
                return visitor.visitChildren(self)




    def range_predicate(self):

        localctx = NosyParser.Range_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_range_predicate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(NosyParser.T__0)
            self.state = 225
            self.match(NosyParser.T__13)
            self.state = 226
            self.range_predicate_symbol()
            self.state = 228 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 227
                self.fn_arg()
                self.state = 230 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NosyParser.T__4) | (1 << NosyParser.NUMBER) | (1 << NosyParser.BOOLEAN) | (1 << NosyParser.STRING))) != 0)):
                    break

            self.state = 232
            self.match(NosyParser.T__14)
            self.state = 233
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_predicate_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NosyParser.RULE_range_predicate_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_predicate_symbol" ):
                listener.enterRange_predicate_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_predicate_symbol" ):
                listener.exitRange_predicate_symbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_predicate_symbol" ):
                return visitor.visitRange_predicate_symbol(self)
            else:
                return visitor.visitChildren(self)




    def range_predicate_symbol(self):

        localctx = NosyParser.Range_predicate_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_range_predicate_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NosyParser.T__15) | (1 << NosyParser.T__16) | (1 << NosyParser.T__17) | (1 << NosyParser.T__18) | (1 << NosyParser.T__19) | (1 << NosyParser.T__20))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pred_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def range_predicate(self):
            return self.getTypedRuleContext(NosyParser.Range_predicateContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_pred_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPred_expr" ):
                listener.enterPred_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPred_expr" ):
                listener.exitPred_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPred_expr" ):
                return visitor.visitPred_expr(self)
            else:
                return visitor.visitChildren(self)




    def pred_expr(self):

        localctx = NosyParser.Pred_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_pred_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.range_predicate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fn_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fn(self):
            return self.getTypedRuleContext(NosyParser.FnContext,0)


        def binding(self):
            return self.getTypedRuleContext(NosyParser.BindingContext,0)


        def fn_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.Fn_argContext)
            else:
                return self.getTypedRuleContext(NosyParser.Fn_argContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_fn_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFn_expr" ):
                listener.enterFn_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFn_expr" ):
                listener.exitFn_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFn_expr" ):
                return visitor.visitFn_expr(self)
            else:
                return visitor.visitChildren(self)




    def fn_expr(self):

        localctx = NosyParser.Fn_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_fn_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(NosyParser.T__0)
            self.state = 240
            self.match(NosyParser.T__13)
            self.state = 241
            self.fn()
            self.state = 243 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 242
                self.fn_arg()
                self.state = 245 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NosyParser.T__4) | (1 << NosyParser.NUMBER) | (1 << NosyParser.BOOLEAN) | (1 << NosyParser.STRING))) != 0)):
                    break

            self.state = 247
            self.match(NosyParser.T__14)
            self.state = 248
            self.binding()
            self.state = 249
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(NosyParser.SYMBOL)
            else:
                return self.getToken(NosyParser.SYMBOL, i)

        def getRuleIndex(self):
            return NosyParser.RULE_fn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFn" ):
                listener.enterFn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFn" ):
                listener.exitFn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFn" ):
                return visitor.visitFn(self)
            else:
                return visitor.visitChildren(self)




    def fn(self):

        localctx = NosyParser.FnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_fn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(NosyParser.SYMBOL)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NosyParser.T__3:
                self.state = 252
                self.match(NosyParser.T__3)
                self.state = 253
                self.match(NosyParser.SYMBOL)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bind_scalar(self):
            return self.getTypedRuleContext(NosyParser.Bind_scalarContext,0)


        def bind_tuple(self):
            return self.getTypedRuleContext(NosyParser.Bind_tupleContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_binding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinding" ):
                listener.enterBinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinding" ):
                listener.exitBinding(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinding" ):
                return visitor.visitBinding(self)
            else:
                return visitor.visitChildren(self)




    def binding(self):

        localctx = NosyParser.BindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_binding)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NosyParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.bind_scalar()
                pass
            elif token in [NosyParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.bind_tuple()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bind_scalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(NosyParser.VariableContext,0)


        def getRuleIndex(self):
            return NosyParser.RULE_bind_scalar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBind_scalar" ):
                listener.enterBind_scalar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBind_scalar" ):
                listener.exitBind_scalar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBind_scalar" ):
                return visitor.visitBind_scalar(self)
            else:
                return visitor.visitChildren(self)




    def bind_scalar(self):

        localctx = NosyParser.Bind_scalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_bind_scalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bind_tupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NosyParser.VariableContext)
            else:
                return self.getTypedRuleContext(NosyParser.VariableContext,i)


        def getRuleIndex(self):
            return NosyParser.RULE_bind_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBind_tuple" ):
                listener.enterBind_tuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBind_tuple" ):
                listener.exitBind_tuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBind_tuple" ):
                return visitor.visitBind_tuple(self)
            else:
                return visitor.visitChildren(self)




    def bind_tuple(self):

        localctx = NosyParser.Bind_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_bind_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(NosyParser.T__0)
            self.state = 268 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 268
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [NosyParser.T__4]:
                    self.state = 266
                    self.variable()
                    pass
                elif token in [NosyParser.T__3]:
                    self.state = 267
                    self.match(NosyParser.T__3)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 270 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==NosyParser.T__3 or _la==NosyParser.T__4):
                    break

            self.state = 272
            self.match(NosyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






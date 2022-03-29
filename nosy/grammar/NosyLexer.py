# Generated from ./nosy/grammar/Nosy.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35")
        buf.write("\u00bb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27")
        buf.write("\u0086\n\27\f\27\16\27\u0089\13\27\3\27\3\27\5\27\u008d")
        buf.write("\n\27\3\30\3\30\5\30\u0091\n\30\3\30\3\30\7\30\u0095\n")
        buf.write("\30\f\30\16\30\u0098\13\30\5\30\u009a\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00a5\n\31\3\32")
        buf.write("\3\32\7\32\u00a9\n\32\f\32\16\32\u00ac\13\32\3\32\3\32")
        buf.write("\3\33\6\33\u00b1\n\33\r\33\16\33\u00b2\3\34\6\34\u00b6")
        buf.write("\n\34\r\34\16\34\u00b7\3\34\3\34\2\2\35\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\35\3\2\7\3\2\62;\3\2\63;\3\2\"\u0080\4\2C\\c|\5")
        buf.write("\2\13\f\17\17\"\"\2\u00c3\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\39\3\2\2\2\5;\3\2\2")
        buf.write("\2\7=\3\2\2\2\tC\3\2\2\2\13E\3\2\2\2\rG\3\2\2\2\17N\3")
        buf.write("\2\2\2\21R\3\2\2\2\23V\3\2\2\2\25_\3\2\2\2\27b\3\2\2\2")
        buf.write("\31j\3\2\2\2\33l\3\2\2\2\35n\3\2\2\2\37p\3\2\2\2!r\3\2")
        buf.write("\2\2#t\3\2\2\2%w\3\2\2\2\'z\3\2\2\2)|\3\2\2\2+~\3\2\2")
        buf.write("\2-\u008c\3\2\2\2/\u0099\3\2\2\2\61\u00a4\3\2\2\2\63\u00a6")
        buf.write("\3\2\2\2\65\u00b0\3\2\2\2\67\u00b5\3\2\2\29:\7]\2\2:\4")
        buf.write("\3\2\2\2;<\7_\2\2<\6\3\2\2\2=>\7<\2\2>?\7h\2\2?@\7k\2")
        buf.write("\2@A\7p\2\2AB\7f\2\2B\b\3\2\2\2CD\7a\2\2D\n\3\2\2\2EF")
        buf.write("\7A\2\2F\f\3\2\2\2GH\7<\2\2HI\7y\2\2IJ\7j\2\2JK\7g\2\2")
        buf.write("KL\7t\2\2LM\7g\2\2M\16\3\2\2\2NO\7c\2\2OP\7p\2\2PQ\7f")
        buf.write("\2\2Q\20\3\2\2\2RS\7p\2\2ST\7q\2\2TU\7v\2\2U\22\3\2\2")
        buf.write("\2VW\7p\2\2WX\7q\2\2XY\7v\2\2YZ\7/\2\2Z[\7l\2\2[\\\7q")
        buf.write("\2\2\\]\7k\2\2]^\7p\2\2^\24\3\2\2\2_`\7q\2\2`a\7t\2\2")
        buf.write("a\26\3\2\2\2bc\7q\2\2cd\7t\2\2de\7/\2\2ef\7l\2\2fg\7q")
        buf.write("\2\2gh\7k\2\2hi\7p\2\2i\30\3\2\2\2jk\7<\2\2k\32\3\2\2")
        buf.write("\2lm\7\61\2\2m\34\3\2\2\2no\7*\2\2o\36\3\2\2\2pq\7+\2")
        buf.write("\2q \3\2\2\2rs\7?\2\2s\"\3\2\2\2tu\7#\2\2uv\7?\2\2v$\3")
        buf.write("\2\2\2wx\7>\2\2xy\7?\2\2y&\3\2\2\2z{\7>\2\2{(\3\2\2\2")
        buf.write("|}\7@\2\2}*\3\2\2\2~\177\7@\2\2\177\u0080\7?\2\2\u0080")
        buf.write(",\3\2\2\2\u0081\u008d\5/\30\2\u0082\u0083\5/\30\2\u0083")
        buf.write("\u0087\7\60\2\2\u0084\u0086\t\2\2\2\u0085\u0084\3\2\2")
        buf.write("\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a")
        buf.write("\u008b\t\3\2\2\u008b\u008d\3\2\2\2\u008c\u0081\3\2\2\2")
        buf.write("\u008c\u0082\3\2\2\2\u008d.\3\2\2\2\u008e\u009a\7\62\2")
        buf.write("\2\u008f\u0091\7/\2\2\u0090\u008f\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0096\t\3\2\2\u0093")
        buf.write("\u0095\t\2\2\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2")
        buf.write("\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u009a\3")
        buf.write("\2\2\2\u0098\u0096\3\2\2\2\u0099\u008e\3\2\2\2\u0099\u0090")
        buf.write("\3\2\2\2\u009a\60\3\2\2\2\u009b\u009c\7V\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\u009e\7w\2\2\u009e\u00a5\7g\2\2\u009f\u00a0")
        buf.write("\7H\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3")
        buf.write("\7u\2\2\u00a3\u00a5\7g\2\2\u00a4\u009b\3\2\2\2\u00a4\u009f")
        buf.write("\3\2\2\2\u00a5\62\3\2\2\2\u00a6\u00aa\7$\2\2\u00a7\u00a9")
        buf.write("\t\4\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ad\u00ae\7$\2\2\u00ae\64\3\2\2")
        buf.write("\2\u00af\u00b1\t\5\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\66\3\2\2\2\u00b4\u00b6\t\6\2\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\u00ba\b\34\2\2\u00ba8\3\2\2")
        buf.write("\2\f\2\u0087\u008c\u0090\u0096\u0099\u00a4\u00aa\u00b2")
        buf.write("\u00b7\3\b\2\2")
        return buf.getvalue()


class NosyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    NUMBER = 22
    INT = 23
    BOOLEAN = 24
    STRING = 25
    SYMBOL = 26
    WS = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "':find'", "'_'", "'?'", "':where'", "'and'", 
            "'not'", "'not-join'", "'or'", "'or-join'", "':'", "'/'", "'('", 
            "')'", "'='", "'!='", "'<='", "'<'", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "INT", "BOOLEAN", "STRING", "SYMBOL", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "NUMBER", "INT", "BOOLEAN", "STRING", "SYMBOL", 
                  "WS" ]

    grammarFileName = "Nosy.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



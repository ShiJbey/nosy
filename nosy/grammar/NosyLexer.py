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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u00c2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\7\27\u0088\n\27\f\27\16\27\u008b\13\27\3\27\3\27\5\27")
        buf.write("\u008f\n\27\3\30\3\30\3\30\3\31\3\31\5\31\u0096\n\31\3")
        buf.write("\31\3\31\7\31\u009a\n\31\f\31\16\31\u009d\13\31\5\31\u009f")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u00aa\n\32\3\33\3\33\7\33\u00ae\n\33\f\33\16\33\u00b1")
        buf.write("\13\33\3\33\3\33\3\34\3\34\7\34\u00b7\n\34\f\34\16\34")
        buf.write("\u00ba\13\34\3\35\6\35\u00bd\n\35\r\35\16\35\u00be\3\35")
        buf.write("\3\35\2\2\36\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36\3\2\b\3\2\62")
        buf.write(";\3\2\63;\3\2\"\u0080\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f")
        buf.write("\17\17\"\"\2\u00ca\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\3;\3\2\2\2\5=\3\2")
        buf.write("\2\2\7?\3\2\2\2\tE\3\2\2\2\13G\3\2\2\2\rI\3\2\2\2\17P")
        buf.write("\3\2\2\2\21T\3\2\2\2\23X\3\2\2\2\25a\3\2\2\2\27d\3\2\2")
        buf.write("\2\31l\3\2\2\2\33n\3\2\2\2\35p\3\2\2\2\37r\3\2\2\2!t\3")
        buf.write("\2\2\2#v\3\2\2\2%y\3\2\2\2\'|\3\2\2\2)~\3\2\2\2+\u0080")
        buf.write("\3\2\2\2-\u008e\3\2\2\2/\u0090\3\2\2\2\61\u009e\3\2\2")
        buf.write("\2\63\u00a9\3\2\2\2\65\u00ab\3\2\2\2\67\u00b4\3\2\2\2")
        buf.write("9\u00bc\3\2\2\2;<\7]\2\2<\4\3\2\2\2=>\7_\2\2>\6\3\2\2")
        buf.write("\2?@\7<\2\2@A\7h\2\2AB\7k\2\2BC\7p\2\2CD\7f\2\2D\b\3\2")
        buf.write("\2\2EF\7a\2\2F\n\3\2\2\2GH\7A\2\2H\f\3\2\2\2IJ\7<\2\2")
        buf.write("JK\7y\2\2KL\7j\2\2LM\7g\2\2MN\7t\2\2NO\7g\2\2O\16\3\2")
        buf.write("\2\2PQ\7c\2\2QR\7p\2\2RS\7f\2\2S\20\3\2\2\2TU\7p\2\2U")
        buf.write("V\7q\2\2VW\7v\2\2W\22\3\2\2\2XY\7p\2\2YZ\7q\2\2Z[\7v\2")
        buf.write("\2[\\\7/\2\2\\]\7l\2\2]^\7q\2\2^_\7k\2\2_`\7p\2\2`\24")
        buf.write("\3\2\2\2ab\7q\2\2bc\7t\2\2c\26\3\2\2\2de\7q\2\2ef\7t\2")
        buf.write("\2fg\7/\2\2gh\7l\2\2hi\7q\2\2ij\7k\2\2jk\7p\2\2k\30\3")
        buf.write("\2\2\2lm\7<\2\2m\32\3\2\2\2no\7\61\2\2o\34\3\2\2\2pq\7")
        buf.write("*\2\2q\36\3\2\2\2rs\7+\2\2s \3\2\2\2tu\7?\2\2u\"\3\2\2")
        buf.write("\2vw\7#\2\2wx\7?\2\2x$\3\2\2\2yz\7>\2\2z{\7?\2\2{&\3\2")
        buf.write("\2\2|}\7>\2\2}(\3\2\2\2~\177\7@\2\2\177*\3\2\2\2\u0080")
        buf.write("\u0081\7@\2\2\u0081\u0082\7?\2\2\u0082,\3\2\2\2\u0083")
        buf.write("\u008f\5\61\31\2\u0084\u0085\5\61\31\2\u0085\u0089\7\60")
        buf.write("\2\2\u0086\u0088\t\2\2\2\u0087\u0086\3\2\2\2\u0088\u008b")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\t\3\2\2")
        buf.write("\u008d\u008f\3\2\2\2\u008e\u0083\3\2\2\2\u008e\u0084\3")
        buf.write("\2\2\2\u008f.\3\2\2\2\u0090\u0091\t\3\2\2\u0091\u0092")
        buf.write("\t\2\2\2\u0092\60\3\2\2\2\u0093\u009f\7\62\2\2\u0094\u0096")
        buf.write("\7/\2\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u009b\t\3\2\2\u0098\u009a\t\2\2\2")
        buf.write("\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3")
        buf.write("\2\2\2\u009b\u009c\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b")
        buf.write("\3\2\2\2\u009e\u0093\3\2\2\2\u009e\u0095\3\2\2\2\u009f")
        buf.write("\62\3\2\2\2\u00a0\u00a1\7V\2\2\u00a1\u00a2\7t\2\2\u00a2")
        buf.write("\u00a3\7w\2\2\u00a3\u00aa\7g\2\2\u00a4\u00a5\7H\2\2\u00a5")
        buf.write("\u00a6\7c\2\2\u00a6\u00a7\7n\2\2\u00a7\u00a8\7u\2\2\u00a8")
        buf.write("\u00aa\7g\2\2\u00a9\u00a0\3\2\2\2\u00a9\u00a4\3\2\2\2")
        buf.write("\u00aa\64\3\2\2\2\u00ab\u00af\7$\2\2\u00ac\u00ae\t\4\2")
        buf.write("\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b2\u00b3\7$\2\2\u00b3\66\3\2\2\2\u00b4")
        buf.write("\u00b8\t\5\2\2\u00b5\u00b7\t\6\2\2\u00b6\u00b5\3\2\2\2")
        buf.write("\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b98\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bd")
        buf.write("\t\7\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\u00c1\b\35\2\2\u00c1:\3\2\2\2\f\2\u0089\u008e\u0095")
        buf.write("\u009b\u009e\u00a9\u00af\u00b8\u00be\3\b\2\2")
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
    UINT = 23
    INT = 24
    BOOLEAN = 25
    STRING = 26
    SYMBOL = 27
    WS = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "':find'", "'_'", "'?'", "':where'", "'and'", 
            "'not'", "'not-join'", "'or'", "'or-join'", "':'", "'/'", "'('", 
            "')'", "'='", "'!='", "'<='", "'<'", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "UINT", "INT", "BOOLEAN", "STRING", "SYMBOL", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "NUMBER", "UINT", "INT", "BOOLEAN", "STRING", 
                  "SYMBOL", "WS" ]

    grammarFileName = "Nosy.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
 # 2110342 - Nguyen Minh Loc



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01ea\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\7\64\u0153\n\64\f\64\16\64\u0156\13\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\7\65\u015e\n\65\f\65\16\65\u0161\13\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\66\6\66\u0169\n\66\r\66\16")
        buf.write("\66\u016a\3\66\3\66\3\67\3\67\7\67\u0171\n\67\f\67\16")
        buf.write("\67\u0174\13\67\38\38\39\39\39\59\u017b\n9\39\39\59\u017f")
        buf.write("\n9\39\39\59\u0183\n9\3:\3:\7:\u0187\n:\f:\16:\u018a\13")
        buf.write(":\3:\3:\3:\3;\3;\3;\7;\u0192\n;\f;\16;\u0195\13;\5;\u0197")
        buf.write("\n;\3<\3<\7<\u019b\n<\f<\16<\u019e\13<\3=\3=\5=\u01a2")
        buf.write("\n=\3=\6=\u01a5\n=\r=\16=\u01a6\3>\3>\5>\u01ab\n>\3?\3")
        buf.write("?\3?\3@\3@\5@\u01b2\n@\3@\3@\3@\7@\u01b7\n@\f@\16@\u01ba")
        buf.write("\13@\3A\3A\6A\u01be\nA\rA\16A\u01bf\3B\3B\3C\3C\3D\3D")
        buf.write("\3E\3E\3F\3F\5F\u01cc\nF\3G\3G\3H\3H\3H\3I\3I\7I\u01d5")
        buf.write("\nI\fI\16I\u01d8\13I\3I\5I\u01db\nI\3I\3I\3J\3J\7J\u01e1")
        buf.write("\nJ\fJ\16J\u01e4\13J\3J\3J\3J\3J\3J\3\u015f\2K\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w\2y\2")
        buf.write("{\2}\2\177<\u0081=\u0083\2\u0085\2\u0087\2\u0089\2\u008b")
        buf.write("\2\u008d\2\u008f>\u0091?\u0093@\3\2\r\4\2\f\f\17\17\5")
        buf.write("\2\13\f\17\17\"\"\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2")
        buf.write("\f\f\17\17$$^^\t\2$$^^ddhhppttvv\6\2\62;C\\aac|\3\2C\\")
        buf.write("\3\2c|\2\u01f5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\3\u0095\3\2\2\2\5\u009b\3\2\2\2\7\u00a4\3\2\2\2\t\u00a7")
        buf.write("\3\2\2\2\13\u00ac\3\2\2\2\r\u00b0\3\2\2\2\17\u00b5\3\2")
        buf.write("\2\2\21\u00bb\3\2\2\2\23\u00bf\3\2\2\2\25\u00c5\3\2\2")
        buf.write("\2\27\u00ca\3\2\2\2\31\u00d1\3\2\2\2\33\u00d8\3\2\2\2")
        buf.write("\35\u00dd\3\2\2\2\37\u00e3\3\2\2\2!\u00ef\3\2\2\2#\u00f3")
        buf.write("\3\2\2\2%\u00f8\3\2\2\2\'\u00fc\3\2\2\2)\u0101\3\2\2\2")
        buf.write("+\u0107\3\2\2\2-\u010c\3\2\2\2/\u010f\3\2\2\2\61\u0112")
        buf.write("\3\2\2\2\63\u0115\3\2\2\2\65\u0118\3\2\2\2\67\u011b\3")
        buf.write("\2\2\29\u011d\3\2\2\2;\u011f\3\2\2\2=\u0122\3\2\2\2?\u0125")
        buf.write("\3\2\2\2A\u0128\3\2\2\2C\u012a\3\2\2\2E\u012c\3\2\2\2")
        buf.write("G\u012e\3\2\2\2I\u0130\3\2\2\2K\u0132\3\2\2\2M\u0134\3")
        buf.write("\2\2\2O\u0136\3\2\2\2Q\u0138\3\2\2\2S\u013a\3\2\2\2U\u013c")
        buf.write("\3\2\2\2W\u013e\3\2\2\2Y\u0140\3\2\2\2[\u0142\3\2\2\2")
        buf.write("]\u0144\3\2\2\2_\u0146\3\2\2\2a\u0148\3\2\2\2c\u014a\3")
        buf.write("\2\2\2e\u014c\3\2\2\2g\u014e\3\2\2\2i\u0159\3\2\2\2k\u0168")
        buf.write("\3\2\2\2m\u016e\3\2\2\2o\u0175\3\2\2\2q\u0182\3\2\2\2")
        buf.write("s\u0184\3\2\2\2u\u0196\3\2\2\2w\u0198\3\2\2\2y\u019f\3")
        buf.write("\2\2\2{\u01aa\3\2\2\2}\u01ac\3\2\2\2\177\u01b1\3\2\2\2")
        buf.write("\u0081\u01bb\3\2\2\2\u0083\u01c1\3\2\2\2\u0085\u01c3\3")
        buf.write("\2\2\2\u0087\u01c5\3\2\2\2\u0089\u01c7\3\2\2\2\u008b\u01cb")
        buf.write("\3\2\2\2\u008d\u01cd\3\2\2\2\u008f\u01cf\3\2\2\2\u0091")
        buf.write("\u01d2\3\2\2\2\u0093\u01de\3\2\2\2\u0095\u0096\7d\2\2")
        buf.write("\u0096\u0097\7t\2\2\u0097\u0098\7g\2\2\u0098\u0099\7c")
        buf.write("\2\2\u0099\u009a\7m\2\2\u009a\4\3\2\2\2\u009b\u009c\7")
        buf.write("e\2\2\u009c\u009d\7q\2\2\u009d\u009e\7p\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2")
        buf.write("\7w\2\2\u00a2\u00a3\7g\2\2\u00a3\6\3\2\2\2\u00a4\u00a5")
        buf.write("\7k\2\2\u00a5\u00a6\7h\2\2\u00a6\b\3\2\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8\u00a9\7n\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab")
        buf.write("\7g\2\2\u00ab\n\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\u00af\7t\2\2\u00af\f\3\2\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7w\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\16\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7")
        buf.write("\7c\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\20\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\u00be\7v\2\2\u00be\22\3\2\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7v\2\2\u00c4\24\3\2\2\2\u00c5\u00c6")
        buf.write("\7d\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9")
        buf.write("\7n\2\2\u00c9\26\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7i\2\2\u00d0\30\3\2\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7w\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7p\2\2\u00d7\32")
        buf.write("\3\2\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7w\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\u00dc\7n\2\2\u00dc\34\3\2\2\2\u00dd\u00de")
        buf.write("\7e\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7u\2\2\u00e1\u00e2\7u\2\2\u00e2\36\3\2\2\2\u00e3\u00e4")
        buf.write("\7e\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7u\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea")
        buf.write("\7w\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7t\2\2\u00ee \3\2\2\2\u00ef\u00f0")
        buf.write("\7x\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7t\2\2\u00f2\"")
        buf.write("\3\2\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6")
        buf.write("\7n\2\2\u00f6\u00f7\7h\2\2\u00f7$\3\2\2\2\u00f8\u00f9")
        buf.write("\7p\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7y\2\2\u00fb&\3")
        buf.write("\2\2\2\u00fc\u00fd\7x\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7f\2\2\u0100(\3\2\2\2\u0101\u0102")
        buf.write("\7e\2\2\u0102\u0103\7q\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7u\2\2\u0105\u0106\7v\2\2\u0106*\3\2\2\2\u0107\u0108")
        buf.write("\7h\2\2\u0108\u0109\7w\2\2\u0109\u010a\7p\2\2\u010a\u010b")
        buf.write("\7e\2\2\u010b,\3\2\2\2\u010c\u010d\7(\2\2\u010d\u010e")
        buf.write("\7(\2\2\u010e.\3\2\2\2\u010f\u0110\7~\2\2\u0110\u0111")
        buf.write("\7~\2\2\u0111\60\3\2\2\2\u0112\u0113\7?\2\2\u0113\u0114")
        buf.write("\7?\2\2\u0114\62\3\2\2\2\u0115\u0116\7<\2\2\u0116\u0117")
        buf.write("\7?\2\2\u0117\64\3\2\2\2\u0118\u0119\7#\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a\66\3\2\2\2\u011b\u011c\7>\2\2\u011c8\3\2")
        buf.write("\2\2\u011d\u011e\7@\2\2\u011e:\3\2\2\2\u011f\u0120\7>")
        buf.write("\2\2\u0120\u0121\7?\2\2\u0121<\3\2\2\2\u0122\u0123\7@")
        buf.write("\2\2\u0123\u0124\7?\2\2\u0124>\3\2\2\2\u0125\u0126\7>")
        buf.write("\2\2\u0126\u0127\7/\2\2\u0127@\3\2\2\2\u0128\u0129\7-")
        buf.write("\2\2\u0129B\3\2\2\2\u012a\u012b\7/\2\2\u012bD\3\2\2\2")
        buf.write("\u012c\u012d\7,\2\2\u012dF\3\2\2\2\u012e\u012f\7\61\2")
        buf.write("\2\u012fH\3\2\2\2\u0130\u0131\7^\2\2\u0131J\3\2\2\2\u0132")
        buf.write("\u0133\7#\2\2\u0133L\3\2\2\2\u0134\u0135\7?\2\2\u0135")
        buf.write("N\3\2\2\2\u0136\u0137\7`\2\2\u0137P\3\2\2\2\u0138\u0139")
        buf.write("\7\'\2\2\u0139R\3\2\2\2\u013a\u013b\7.\2\2\u013bT\3\2")
        buf.write("\2\2\u013c\u013d\7=\2\2\u013dV\3\2\2\2\u013e\u013f\7<")
        buf.write("\2\2\u013fX\3\2\2\2\u0140\u0141\7\60\2\2\u0141Z\3\2\2")
        buf.write("\2\u0142\u0143\7*\2\2\u0143\\\3\2\2\2\u0144\u0145\7+\2")
        buf.write("\2\u0145^\3\2\2\2\u0146\u0147\7]\2\2\u0147`\3\2\2\2\u0148")
        buf.write("\u0149\7_\2\2\u0149b\3\2\2\2\u014a\u014b\7}\2\2\u014b")
        buf.write("d\3\2\2\2\u014c\u014d\7\177\2\2\u014df\3\2\2\2\u014e\u014f")
        buf.write("\7\61\2\2\u014f\u0150\7\61\2\2\u0150\u0154\3\2\2\2\u0151")
        buf.write("\u0153\n\2\2\2\u0152\u0151\3\2\2\2\u0153\u0156\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\3")
        buf.write("\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\b\64\2\2\u0158")
        buf.write("h\3\2\2\2\u0159\u015a\7\61\2\2\u015a\u015b\7,\2\2\u015b")
        buf.write("\u015f\3\2\2\2\u015c\u015e\13\2\2\2\u015d\u015c\3\2\2")
        buf.write("\2\u015e\u0161\3\2\2\2\u015f\u0160\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u015f\3\2\2\2\u0162")
        buf.write("\u0163\7,\2\2\u0163\u0164\7\61\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165\u0166\b\65\2\2\u0166j\3\2\2\2\u0167\u0169\t\3\2")
        buf.write("\2\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016d\b\66\2\2\u016dl\3\2\2\2\u016e\u0172\t\4\2\2\u016f")
        buf.write("\u0171\t\5\2\2\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2\2")
        buf.write("\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173n\3\2\2")
        buf.write("\2\u0174\u0172\3\2\2\2\u0175\u0176\5u;\2\u0176p\3\2\2")
        buf.write("\2\u0177\u0178\5u;\2\u0178\u017a\5w<\2\u0179\u017b\5y")
        buf.write("=\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u0183")
        buf.write("\3\2\2\2\u017c\u017e\5u;\2\u017d\u017f\5w<\2\u017e\u017d")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\5y=\2\u0181\u0183\3\2\2\2\u0182\u0177\3\2\2\2\u0182")
        buf.write("\u017c\3\2\2\2\u0183r\3\2\2\2\u0184\u0188\7$\2\2\u0185")
        buf.write("\u0187\5{>\2\u0186\u0185\3\2\2\2\u0187\u018a\3\2\2\2\u0188")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018b\3\2\2\2")
        buf.write("\u018a\u0188\3\2\2\2\u018b\u018c\7$\2\2\u018c\u018d\b")
        buf.write(":\3\2\u018dt\3\2\2\2\u018e\u0197\7\62\2\2\u018f\u0193")
        buf.write("\t\4\2\2\u0190\u0192\t\5\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u018e\3")
        buf.write("\2\2\2\u0196\u018f\3\2\2\2\u0197v\3\2\2\2\u0198\u019c")
        buf.write("\7\60\2\2\u0199\u019b\t\5\2\2\u019a\u0199\3\2\2\2\u019b")
        buf.write("\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019dx\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a1\t\6\2")
        buf.write("\2\u01a0\u01a2\t\7\2\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a5\t\5\2\2\u01a4")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a4\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7z\3\2\2\2\u01a8\u01ab\n\b\2")
        buf.write("\2\u01a9\u01ab\5}?\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3")
        buf.write("\2\2\2\u01ab|\3\2\2\2\u01ac\u01ad\7^\2\2\u01ad\u01ae\t")
        buf.write("\t\2\2\u01ae~\3\2\2\2\u01af\u01b2\5\u008bF\2\u01b0\u01b2")
        buf.write("\5\u0089E\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b8\3\2\2\2\u01b3\u01b7\5\u008bF\2\u01b4\u01b7\5\u0089")
        buf.write("E\2\u01b5\u01b7\5\u0087D\2\u01b6\u01b3\3\2\2\2\u01b6\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u0080\3\2\2\2")
        buf.write("\u01ba\u01b8\3\2\2\2\u01bb\u01bd\5\u008dG\2\u01bc\u01be")
        buf.write("\t\n\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u0082\3\2\2\2")
        buf.write("\u01c1\u01c2\t\13\2\2\u01c2\u0084\3\2\2\2\u01c3\u01c4")
        buf.write("\t\f\2\2\u01c4\u0086\3\2\2\2\u01c5\u01c6\t\5\2\2\u01c6")
        buf.write("\u0088\3\2\2\2\u01c7\u01c8\7a\2\2\u01c8\u008a\3\2\2\2")
        buf.write("\u01c9\u01cc\5\u0083B\2\u01ca\u01cc\5\u0085C\2\u01cb\u01c9")
        buf.write("\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u008c\3\2\2\2\u01cd")
        buf.write("\u01ce\7B\2\2\u01ce\u008e\3\2\2\2\u01cf\u01d0\13\2\2\2")
        buf.write("\u01d0\u01d1\bH\4\2\u01d1\u0090\3\2\2\2\u01d2\u01d6\7")
        buf.write("$\2\2\u01d3\u01d5\5{>\2\u01d4\u01d3\3\2\2\2\u01d5\u01d8")
        buf.write("\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01db\7\2\2\3")
        buf.write("\u01da\u01d9\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dc\3")
        buf.write("\2\2\2\u01dc\u01dd\bI\5\2\u01dd\u0092\3\2\2\2\u01de\u01e2")
        buf.write("\7$\2\2\u01df\u01e1\5{>\2\u01e0\u01df\3\2\2\2\u01e1\u01e4")
        buf.write("\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3")
        buf.write("\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6\7^\2\2")
        buf.write("\u01e6\u01e7\n\t\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\b")
        buf.write("J\6\2\u01e9\u0094\3\2\2\2\31\2\u0154\u015f\u016a\u0172")
        buf.write("\u017a\u017e\u0182\u0188\u0193\u0196\u019c\u01a1\u01a6")
        buf.write("\u01aa\u01b1\u01b6\u01b8\u01bf\u01cb\u01d6\u01da\u01e2")
        buf.write("\7\b\2\2\3:\2\3H\3\3I\4\3J\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    IF = 3
    ELSE = 4
    FOR = 5
    TRUE = 6
    FALSE = 7
    INT = 8
    FLOAT = 9
    BOOL = 10
    STRING = 11
    RETURN = 12
    NULL = 13
    CLASS = 14
    CONSTRUCTOR = 15
    VAR = 16
    SELF = 17
    NEW = 18
    VOID = 19
    CONST = 20
    FUNC = 21
    AND = 22
    OR = 23
    EQUAL = 24
    ASSIGN = 25
    NOT_EQUAL = 26
    LESS_THAN = 27
    GREATER_THAN = 28
    LESS_THAN_EQUAL = 29
    GREATER_THAN_EQUAL = 30
    SUPERCLASS = 31
    ADD = 32
    SUB = 33
    MUL = 34
    DIV_FLOAT = 35
    DIV_INT = 36
    NOT = 37
    EQ = 38
    STRING_CONCAT = 39
    MOD = 40
    COMMA = 41
    SEMI = 42
    COLON = 43
    DOT = 44
    LP = 45
    RP = 46
    LSB = 47
    RSB = 48
    LB = 49
    RB = 50
    LINE_COMMENT = 51
    BLOCK_COMMENT = 52
    WS = 53
    INTARR = 54
    INTLIT = 55
    FLOATLIT = 56
    STRINGLIT = 57
    ID = 58
    STATIC_ID = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'new'", 
            "'void'", "'const'", "'func'", "'&&'", "'||'", "'=='", "':='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "'<-'", "'+'", "'-'", 
            "'*'", "'/'", "'\\'", "'!'", "'='", "'^'", "'%'", "','", "';'", 
            "':'", "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "AND", "OR", 
            "EQUAL", "ASSIGN", "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", 
            "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", "SUPERCLASS", "ADD", 
            "SUB", "MUL", "DIV_FLOAT", "DIV_INT", "NOT", "EQ", "STRING_CONCAT", 
            "MOD", "COMMA", "SEMI", "COLON", "DOT", "LP", "RP", "LSB", "RSB", 
            "LB", "RB", "LINE_COMMENT", "BLOCK_COMMENT", "WS", "INTARR", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "ID", "STATIC_ID", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                  "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "FUNC", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LESS_THAN", 
                  "GREATER_THAN", "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", 
                  "SUPERCLASS", "ADD", "SUB", "MUL", "DIV_FLOAT", "DIV_INT", 
                  "NOT", "EQ", "STRING_CONCAT", "MOD", "COMMA", "SEMI", 
                  "COLON", "DOT", "LP", "RP", "LSB", "RSB", "LB", "RB", 
                  "LINE_COMMENT", "BLOCK_COMMENT", "WS", "INTARR", "INTLIT", 
                  "FLOATLIT", "STRINGLIT", "INTPART", "DECPART", "EXPPART", 
                  "CHAR", "ESCAPE", "ID", "STATIC_ID", "UPPER", "LOWER", 
                  "DIGIT", "UNDERSCORE", "LETTER", "AT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[56] = self.STRINGLIT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	y = str(self.text)
            	raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise IllegalEscape(self.text[1:])

     



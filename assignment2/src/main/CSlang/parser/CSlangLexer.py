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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01f0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\5\2\u009a\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$")
        buf.write("\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-")
        buf.write("\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u0159\n\65\f\65\16")
        buf.write("\65\u015c\13\65\3\65\3\65\3\66\3\66\3\66\3\66\7\66\u0164")
        buf.write("\n\66\f\66\16\66\u0167\13\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\6\67\u016f\n\67\r\67\16\67\u0170\3\67\3\67\38\3")
        buf.write("8\78\u0177\n8\f8\168\u017a\138\39\39\3:\3:\3:\5:\u0181")
        buf.write("\n:\3:\3:\5:\u0185\n:\3:\3:\5:\u0189\n:\3;\3;\7;\u018d")
        buf.write("\n;\f;\16;\u0190\13;\3;\3;\3;\3<\3<\3<\7<\u0198\n<\f<")
        buf.write("\16<\u019b\13<\5<\u019d\n<\3=\3=\7=\u01a1\n=\f=\16=\u01a4")
        buf.write("\13=\3>\3>\5>\u01a8\n>\3>\6>\u01ab\n>\r>\16>\u01ac\3?")
        buf.write("\3?\5?\u01b1\n?\3@\3@\3@\3A\3A\5A\u01b8\nA\3A\3A\3A\7")
        buf.write("A\u01bd\nA\fA\16A\u01c0\13A\3B\3B\6B\u01c4\nB\rB\16B\u01c5")
        buf.write("\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\5G\u01d2\nG\3H\3H\3I\3")
        buf.write("I\3I\3J\3J\7J\u01db\nJ\fJ\16J\u01de\13J\3J\5J\u01e1\n")
        buf.write("J\3J\3J\3K\3K\7K\u01e7\nK\fK\16K\u01ea\13K\3K\3K\3K\3")
        buf.write("K\3K\3\u0165\2L\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u<w\2y\2{\2}\2\177\2\u0081=\u0083>\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091?\u0093")
        buf.write("@\u0095A\3\2\r\4\2\f\f\17\17\5\2\13\f\17\17\"\"\3\2\63")
        buf.write(";\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2$$^^dd")
        buf.write("hhppttvv\6\2\62;C\\aac|\3\2C\\\3\2c|\2\u01fc\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u0099")
        buf.write("\3\2\2\2\5\u009b\3\2\2\2\7\u00a1\3\2\2\2\t\u00aa\3\2\2")
        buf.write("\2\13\u00ad\3\2\2\2\r\u00b2\3\2\2\2\17\u00b6\3\2\2\2\21")
        buf.write("\u00bb\3\2\2\2\23\u00c1\3\2\2\2\25\u00c5\3\2\2\2\27\u00cb")
        buf.write("\3\2\2\2\31\u00d0\3\2\2\2\33\u00d7\3\2\2\2\35\u00de\3")
        buf.write("\2\2\2\37\u00e3\3\2\2\2!\u00e9\3\2\2\2#\u00f5\3\2\2\2")
        buf.write("%\u00f9\3\2\2\2\'\u00fe\3\2\2\2)\u0102\3\2\2\2+\u0107")
        buf.write("\3\2\2\2-\u010d\3\2\2\2/\u0112\3\2\2\2\61\u0115\3\2\2")
        buf.write("\2\63\u0118\3\2\2\2\65\u011b\3\2\2\2\67\u011e\3\2\2\2")
        buf.write("9\u0121\3\2\2\2;\u0123\3\2\2\2=\u0125\3\2\2\2?\u0128\3")
        buf.write("\2\2\2A\u012b\3\2\2\2C\u012e\3\2\2\2E\u0130\3\2\2\2G\u0132")
        buf.write("\3\2\2\2I\u0134\3\2\2\2K\u0136\3\2\2\2M\u0138\3\2\2\2")
        buf.write("O\u013a\3\2\2\2Q\u013c\3\2\2\2S\u013e\3\2\2\2U\u0140\3")
        buf.write("\2\2\2W\u0142\3\2\2\2Y\u0144\3\2\2\2[\u0146\3\2\2\2]\u0148")
        buf.write("\3\2\2\2_\u014a\3\2\2\2a\u014c\3\2\2\2c\u014e\3\2\2\2")
        buf.write("e\u0150\3\2\2\2g\u0152\3\2\2\2i\u0154\3\2\2\2k\u015f\3")
        buf.write("\2\2\2m\u016e\3\2\2\2o\u0174\3\2\2\2q\u017b\3\2\2\2s\u0188")
        buf.write("\3\2\2\2u\u018a\3\2\2\2w\u019c\3\2\2\2y\u019e\3\2\2\2")
        buf.write("{\u01a5\3\2\2\2}\u01b0\3\2\2\2\177\u01b2\3\2\2\2\u0081")
        buf.write("\u01b7\3\2\2\2\u0083\u01c1\3\2\2\2\u0085\u01c7\3\2\2\2")
        buf.write("\u0087\u01c9\3\2\2\2\u0089\u01cb\3\2\2\2\u008b\u01cd\3")
        buf.write("\2\2\2\u008d\u01d1\3\2\2\2\u008f\u01d3\3\2\2\2\u0091\u01d5")
        buf.write("\3\2\2\2\u0093\u01d8\3\2\2\2\u0095\u01e4\3\2\2\2\u0097")
        buf.write("\u009a\5#\22\2\u0098\u009a\5+\26\2\u0099\u0097\3\2\2\2")
        buf.write("\u0099\u0098\3\2\2\2\u009a\4\3\2\2\2\u009b\u009c\7d\2")
        buf.write("\2\u009c\u009d\7t\2\2\u009d\u009e\7g\2\2\u009e\u009f\7")
        buf.write("c\2\2\u009f\u00a0\7m\2\2\u00a0\6\3\2\2\2\u00a1\u00a2\7")
        buf.write("e\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8")
        buf.write("\7w\2\2\u00a8\u00a9\7g\2\2\u00a9\b\3\2\2\2\u00aa\u00ab")
        buf.write("\7k\2\2\u00ab\u00ac\7h\2\2\u00ac\n\3\2\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\u00af\7n\2\2\u00af\u00b0\7u\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\f\3\2\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4")
        buf.write("\7q\2\2\u00b4\u00b5\7t\2\2\u00b5\16\3\2\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\20\3\2\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd")
        buf.write("\7c\2\2\u00bd\u00be\7n\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\22\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\24\3\2\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9")
        buf.write("\7c\2\2\u00c9\u00ca\7v\2\2\u00ca\26\3\2\2\2\u00cb\u00cc")
        buf.write("\7d\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\30\3\2\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\u00d6\7i\2\2\u00d6\32\3\2\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7w\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7p\2\2\u00dd\34")
        buf.write("\3\2\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1")
        buf.write("\7n\2\2\u00e1\u00e2\7n\2\2\u00e2\36\3\2\2\2\u00e3\u00e4")
        buf.write("\7e\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7u\2\2\u00e7\u00e8\7u\2\2\u00e8 \3\2\2\2\u00e9\u00ea")
        buf.write("\7e\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7u\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0")
        buf.write("\7w\2\2\u00f0\u00f1\7e\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7t\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7x\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7t\2\2\u00f8$\3")
        buf.write("\2\2\2\u00f9\u00fa\7u\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc")
        buf.write("\7n\2\2\u00fc\u00fd\7h\2\2\u00fd&\3\2\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7y\2\2\u0101(\3")
        buf.write("\2\2\2\u0102\u0103\7x\2\2\u0103\u0104\7q\2\2\u0104\u0105")
        buf.write("\7k\2\2\u0105\u0106\7f\2\2\u0106*\3\2\2\2\u0107\u0108")
        buf.write("\7e\2\2\u0108\u0109\7q\2\2\u0109\u010a\7p\2\2\u010a\u010b")
        buf.write("\7u\2\2\u010b\u010c\7v\2\2\u010c,\3\2\2\2\u010d\u010e")
        buf.write("\7h\2\2\u010e\u010f\7w\2\2\u010f\u0110\7p\2\2\u0110\u0111")
        buf.write("\7e\2\2\u0111.\3\2\2\2\u0112\u0113\7(\2\2\u0113\u0114")
        buf.write("\7(\2\2\u0114\60\3\2\2\2\u0115\u0116\7~\2\2\u0116\u0117")
        buf.write("\7~\2\2\u0117\62\3\2\2\2\u0118\u0119\7?\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a\64\3\2\2\2\u011b\u011c\7<\2\2\u011c\u011d")
        buf.write("\7?\2\2\u011d\66\3\2\2\2\u011e\u011f\7#\2\2\u011f\u0120")
        buf.write("\7?\2\2\u01208\3\2\2\2\u0121\u0122\7>\2\2\u0122:\3\2\2")
        buf.write("\2\u0123\u0124\7@\2\2\u0124<\3\2\2\2\u0125\u0126\7>\2")
        buf.write("\2\u0126\u0127\7?\2\2\u0127>\3\2\2\2\u0128\u0129\7@\2")
        buf.write("\2\u0129\u012a\7?\2\2\u012a@\3\2\2\2\u012b\u012c\7>\2")
        buf.write("\2\u012c\u012d\7/\2\2\u012dB\3\2\2\2\u012e\u012f\7-\2")
        buf.write("\2\u012fD\3\2\2\2\u0130\u0131\7/\2\2\u0131F\3\2\2\2\u0132")
        buf.write("\u0133\7,\2\2\u0133H\3\2\2\2\u0134\u0135\7\61\2\2\u0135")
        buf.write("J\3\2\2\2\u0136\u0137\7^\2\2\u0137L\3\2\2\2\u0138\u0139")
        buf.write("\7#\2\2\u0139N\3\2\2\2\u013a\u013b\7?\2\2\u013bP\3\2\2")
        buf.write("\2\u013c\u013d\7`\2\2\u013dR\3\2\2\2\u013e\u013f\7\'\2")
        buf.write("\2\u013fT\3\2\2\2\u0140\u0141\7.\2\2\u0141V\3\2\2\2\u0142")
        buf.write("\u0143\7=\2\2\u0143X\3\2\2\2\u0144\u0145\7<\2\2\u0145")
        buf.write("Z\3\2\2\2\u0146\u0147\7\60\2\2\u0147\\\3\2\2\2\u0148\u0149")
        buf.write("\7*\2\2\u0149^\3\2\2\2\u014a\u014b\7+\2\2\u014b`\3\2\2")
        buf.write("\2\u014c\u014d\7]\2\2\u014db\3\2\2\2\u014e\u014f\7_\2")
        buf.write("\2\u014fd\3\2\2\2\u0150\u0151\7}\2\2\u0151f\3\2\2\2\u0152")
        buf.write("\u0153\7\177\2\2\u0153h\3\2\2\2\u0154\u0155\7\61\2\2\u0155")
        buf.write("\u0156\7\61\2\2\u0156\u015a\3\2\2\2\u0157\u0159\n\2\2")
        buf.write("\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015d\u015e\b\65\2\2\u015ej\3\2\2\2\u015f")
        buf.write("\u0160\7\61\2\2\u0160\u0161\7,\2\2\u0161\u0165\3\2\2\2")
        buf.write("\u0162\u0164\13\2\2\2\u0163\u0162\3\2\2\2\u0164\u0167")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0165\u0163\3\2\2\2\u0166")
        buf.write("\u0168\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\7,\2\2")
        buf.write("\u0169\u016a\7\61\2\2\u016a\u016b\3\2\2\2\u016b\u016c")
        buf.write("\b\66\2\2\u016cl\3\2\2\2\u016d\u016f\t\3\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\b\67\2")
        buf.write("\2\u0173n\3\2\2\2\u0174\u0178\t\4\2\2\u0175\u0177\t\5")
        buf.write("\2\2\u0176\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179p\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017b\u017c\5w<\2\u017cr\3\2\2\2\u017d\u017e")
        buf.write("\5w<\2\u017e\u0180\5y=\2\u017f\u0181\5{>\2\u0180\u017f")
        buf.write("\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0189\3\2\2\2\u0182")
        buf.write("\u0184\5w<\2\u0183\u0185\5y=\2\u0184\u0183\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\5{>\2\u0187")
        buf.write("\u0189\3\2\2\2\u0188\u017d\3\2\2\2\u0188\u0182\3\2\2\2")
        buf.write("\u0189t\3\2\2\2\u018a\u018e\7$\2\2\u018b\u018d\5}?\2\u018c")
        buf.write("\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c\3\2\2\2")
        buf.write("\u018e\u018f\3\2\2\2\u018f\u0191\3\2\2\2\u0190\u018e\3")
        buf.write("\2\2\2\u0191\u0192\7$\2\2\u0192\u0193\b;\3\2\u0193v\3")
        buf.write("\2\2\2\u0194\u019d\7\62\2\2\u0195\u0199\t\4\2\2\u0196")
        buf.write("\u0198\t\5\2\2\u0197\u0196\3\2\2\2\u0198\u019b\3\2\2\2")
        buf.write("\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019d\3")
        buf.write("\2\2\2\u019b\u0199\3\2\2\2\u019c\u0194\3\2\2\2\u019c\u0195")
        buf.write("\3\2\2\2\u019dx\3\2\2\2\u019e\u01a2\7\60\2\2\u019f\u01a1")
        buf.write("\t\5\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3z\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a5\u01a7\t\6\2\2\u01a6\u01a8\t\7\2\2")
        buf.write("\u01a7\u01a6\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3")
        buf.write("\2\2\2\u01a9\u01ab\t\5\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("|\3\2\2\2\u01ae\u01b1\n\b\2\2\u01af\u01b1\5\177@\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1~\3\2\2\2\u01b2")
        buf.write("\u01b3\7^\2\2\u01b3\u01b4\t\t\2\2\u01b4\u0080\3\2\2\2")
        buf.write("\u01b5\u01b8\5\u008dG\2\u01b6\u01b8\5\u008bF\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01be\3\2\2\2\u01b9")
        buf.write("\u01bd\5\u008dG\2\u01ba\u01bd\5\u008bF\2\u01bb\u01bd\5")
        buf.write("\u0089E\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u0082\3\2\2\2\u01c0\u01be\3")
        buf.write("\2\2\2\u01c1\u01c3\5\u008fH\2\u01c2\u01c4\t\n\2\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c5\u01c6\3\2\2\2\u01c6\u0084\3\2\2\2\u01c7\u01c8\t")
        buf.write("\13\2\2\u01c8\u0086\3\2\2\2\u01c9\u01ca\t\f\2\2\u01ca")
        buf.write("\u0088\3\2\2\2\u01cb\u01cc\t\5\2\2\u01cc\u008a\3\2\2\2")
        buf.write("\u01cd\u01ce\7a\2\2\u01ce\u008c\3\2\2\2\u01cf\u01d2\5")
        buf.write("\u0085C\2\u01d0\u01d2\5\u0087D\2\u01d1\u01cf\3\2\2\2\u01d1")
        buf.write("\u01d0\3\2\2\2\u01d2\u008e\3\2\2\2\u01d3\u01d4\7B\2\2")
        buf.write("\u01d4\u0090\3\2\2\2\u01d5\u01d6\13\2\2\2\u01d6\u01d7")
        buf.write("\bI\4\2\u01d7\u0092\3\2\2\2\u01d8\u01dc\7$\2\2\u01d9\u01db")
        buf.write("\5}?\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01df\u01e1\7\2\2\3\u01e0\u01df\3\2\2\2")
        buf.write("\u01e0\u01e1\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\b")
        buf.write("J\5\2\u01e3\u0094\3\2\2\2\u01e4\u01e8\7$\2\2\u01e5\u01e7")
        buf.write("\5}?\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6")
        buf.write("\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb\3\2\2\2\u01ea")
        buf.write("\u01e8\3\2\2\2\u01eb\u01ec\7^\2\2\u01ec\u01ed\n\t\2\2")
        buf.write("\u01ed\u01ee\3\2\2\2\u01ee\u01ef\bK\6\2\u01ef\u0096\3")
        buf.write("\2\2\2\32\2\u0099\u015a\u0165\u0170\u0178\u0180\u0184")
        buf.write("\u0188\u018e\u0199\u019c\u01a2\u01a7\u01ac\u01b0\u01b7")
        buf.write("\u01bc\u01be\u01c5\u01d1\u01dc\u01e0\u01e8\7\b\2\2\3;")
        buf.write("\2\3I\3\3J\4\3K\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Attribute_name = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSE = 5
    FOR = 6
    TRUE = 7
    FALSE = 8
    INT = 9
    FLOAT = 10
    BOOL = 11
    STRING = 12
    RETURN = 13
    NULL = 14
    CLASS = 15
    CONSTRUCTOR = 16
    VAR = 17
    SELF = 18
    NEW = 19
    VOID = 20
    CONST = 21
    FUNC = 22
    AND = 23
    OR = 24
    EQUAL = 25
    ASSIGN = 26
    NOT_EQUAL = 27
    LESS_THAN = 28
    GREATER_THAN = 29
    LESS_THAN_EQUAL = 30
    GREATER_THAN_EQUAL = 31
    SUPERCLASS = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV_FLOAT = 36
    DIV_INT = 37
    NOT = 38
    EQ = 39
    STRING_CONCAT = 40
    MOD = 41
    COMMA = 42
    SEMI = 43
    COLON = 44
    DOT = 45
    LP = 46
    RP = 47
    LSB = 48
    RSB = 49
    LB = 50
    RB = 51
    LINE_COMMENT = 52
    BLOCK_COMMENT = 53
    WS = 54
    INTARR = 55
    INTLIT = 56
    FLOATLIT = 57
    STRINGLIT = 58
    ID = 59
    STATIC_ID = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

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
            "Attribute_name", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
            "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", 
            "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
            "CONST", "FUNC", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
            "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", 
            "SUPERCLASS", "ADD", "SUB", "MUL", "DIV_FLOAT", "DIV_INT", "NOT", 
            "EQ", "STRING_CONCAT", "MOD", "COMMA", "SEMI", "COLON", "DOT", 
            "LP", "RP", "LSB", "RSB", "LB", "RB", "LINE_COMMENT", "BLOCK_COMMENT", 
            "WS", "INTARR", "INTLIT", "FLOATLIT", "STRINGLIT", "ID", "STATIC_ID", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "Attribute_name", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
                  "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", 
                  "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
                  "VOID", "CONST", "FUNC", "AND", "OR", "EQUAL", "ASSIGN", 
                  "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUAL", 
                  "GREATER_THAN_EQUAL", "SUPERCLASS", "ADD", "SUB", "MUL", 
                  "DIV_FLOAT", "DIV_INT", "NOT", "EQ", "STRING_CONCAT", 
                  "MOD", "COMMA", "SEMI", "COLON", "DOT", "LP", "RP", "LSB", 
                  "RSB", "LB", "RB", "LINE_COMMENT", "BLOCK_COMMENT", "WS", 
                  "INTARR", "INTLIT", "FLOATLIT", "STRINGLIT", "INTPART", 
                  "DECPART", "EXPPART", "CHAR", "ESCAPE", "ID", "STATIC_ID", 
                  "UPPER", "LOWER", "DIGIT", "UNDERSCORE", "LETTER", "AT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[57] = self.STRINGLIT_action 
            actions[71] = self.ERROR_CHAR_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
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

     



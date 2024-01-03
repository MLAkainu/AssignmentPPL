# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0264\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u009a\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\5\6\u00a8\n\6\3\7\3\7\5\7\u00ac\n\7\3\b")
        buf.write("\3\b\3\b\3\b\5\b\u00b2\n\b\3\t\3\t\3\t\5\t\u00b7\n\t\3")
        buf.write("\n\3\n\5\n\u00bb\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00c8\n\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00da\n\16\3\17\3\17\3\17\5\17\u00df\n\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\5\23\u00ec")
        buf.write("\n\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\5\26\u00fb\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u0102\n\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u010c\n\31\3\32\3\32\3\32\5\32\u0111\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\5\35\u0120\n\35\3\36\3\36\3\36\3\36\5\36\u0126")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u0131\n\37\3 \3 \3 \5 \u0136\n \3 \3 \3!\3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0142\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\5#\u0150\n#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0165\n%\3&\3&\3&\3&\3&\3")
        buf.write("\'\3\'\5\'\u016e\n\'\3\'\3\'\3\'\3\'\5\'\u0174\n\'\3(")
        buf.write("\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\5,\u018a\n,\3,\3,\3-\3-\3-\3.\3.\5.\u0193\n.\3/\3")
        buf.write("/\3/\3/\5/\u0199\n/\3/\3/\3\60\3\60\3\60\5\60\u01a0\n")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\5\61\u01a7\n\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\5\62\u01b6\n\62\3\62\7\62\u01b9\n\62\f\62\16\62\u01bc")
        buf.write("\13\62\3\63\3\63\3\63\3\63\3\63\5\63\u01c3\n\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\5\64\u01ca\n\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\7\65\u01d2\n\65\f\65\16\65\u01d5\13\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\7\66\u01dd\n\66\f\66\16\66\u01e0")
        buf.write("\13\66\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u01e8\n\67\f")
        buf.write("\67\16\67\u01eb\13\67\38\38\38\58\u01f0\n8\39\39\39\5")
        buf.write("9\u01f5\n9\3:\3:\3:\3:\3:\7:\u01fc\n:\f:\16:\u01ff\13")
        buf.write(":\3;\3;\3;\3;\3;\3;\3;\5;\u0208\n;\7;\u020a\n;\f;\16;")
        buf.write("\u020d\13;\3<\3<\3<\5<\u0212\n<\3<\5<\u0215\n<\3=\3=\3")
        buf.write("=\3=\5=\u021b\n=\3=\3=\5=\u021f\n=\3>\3>\3>\5>\u0224\n")
        buf.write(">\3>\3>\3?\3?\3?\5?\u022b\n?\3?\3?\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\5@\u0237\n@\3A\3A\3A\3A\3A\3A\5A\u023f\nA\3B\3B\3")
        buf.write("B\3B\3B\5B\u0246\nB\3C\3C\3D\3D\3D\3D\3E\3E\3E\3E\3E\5")
        buf.write("E\u0253\nE\3F\3F\3F\3F\3F\5F\u025a\nF\3G\3G\3G\3G\3H\3")
        buf.write("H\3I\3I\3I\2\bbhjlrtJ\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\u0090\2\f\3\2\n\r\4\2\n\r\25\25\4\2\23\23<<\4\2")
        buf.write("\32\32\34 \3\2\30\31\3\2\"#\4\2$&**\3\2\b\t\4\2\22\22")
        buf.write("\26\26\3\2<=\2\u0266\2\u0092\3\2\2\2\4\u0099\3\2\2\2\6")
        buf.write("\u009b\3\2\2\2\b\u00a2\3\2\2\2\n\u00a7\3\2\2\2\f\u00ab")
        buf.write("\3\2\2\2\16\u00b1\3\2\2\2\20\u00b6\3\2\2\2\22\u00ba\3")
        buf.write("\2\2\2\24\u00bc\3\2\2\2\26\u00c7\3\2\2\2\30\u00c9\3\2")
        buf.write("\2\2\32\u00d9\3\2\2\2\34\u00de\3\2\2\2\36\u00e0\3\2\2")
        buf.write("\2 \u00e2\3\2\2\2\"\u00e4\3\2\2\2$\u00eb\3\2\2\2&\u00ed")
        buf.write("\3\2\2\2(\u00ef\3\2\2\2*\u00fa\3\2\2\2,\u0101\3\2\2\2")
        buf.write(".\u0103\3\2\2\2\60\u010b\3\2\2\2\62\u0110\3\2\2\2\64\u0112")
        buf.write("\3\2\2\2\66\u0119\3\2\2\28\u011f\3\2\2\2:\u0125\3\2\2")
        buf.write("\2<\u0130\3\2\2\2>\u0132\3\2\2\2@\u0139\3\2\2\2B\u0141")
        buf.write("\3\2\2\2D\u014f\3\2\2\2F\u0151\3\2\2\2H\u0164\3\2\2\2")
        buf.write("J\u0166\3\2\2\2L\u016b\3\2\2\2N\u0175\3\2\2\2P\u0179\3")
        buf.write("\2\2\2R\u0181\3\2\2\2T\u0184\3\2\2\2V\u0187\3\2\2\2X\u018d")
        buf.write("\3\2\2\2Z\u0192\3\2\2\2\\\u0194\3\2\2\2^\u019f\3\2\2\2")
        buf.write("`\u01a1\3\2\2\2b\u01aa\3\2\2\2d\u01c2\3\2\2\2f\u01c9\3")
        buf.write("\2\2\2h\u01cb\3\2\2\2j\u01d6\3\2\2\2l\u01e1\3\2\2\2n\u01ef")
        buf.write("\3\2\2\2p\u01f4\3\2\2\2r\u01f6\3\2\2\2t\u0200\3\2\2\2")
        buf.write("v\u0214\3\2\2\2x\u021e\3\2\2\2z\u0220\3\2\2\2|\u0227\3")
        buf.write("\2\2\2~\u0236\3\2\2\2\u0080\u023e\3\2\2\2\u0082\u0245")
        buf.write("\3\2\2\2\u0084\u0247\3\2\2\2\u0086\u0249\3\2\2\2\u0088")
        buf.write("\u0252\3\2\2\2\u008a\u0259\3\2\2\2\u008c\u025b\3\2\2\2")
        buf.write("\u008e\u025f\3\2\2\2\u0090\u0261\3\2\2\2\u0092\u0093\5")
        buf.write("\4\3\2\u0093\u0094\7\2\2\3\u0094\3\3\2\2\2\u0095\u0096")
        buf.write("\5\6\4\2\u0096\u0097\5\4\3\2\u0097\u009a\3\2\2\2\u0098")
        buf.write("\u009a\5\6\4\2\u0099\u0095\3\2\2\2\u0099\u0098\3\2\2\2")
        buf.write("\u009a\5\3\2\2\2\u009b\u009c\7\20\2\2\u009c\u009d\5\b")
        buf.write("\5\2\u009d\u009e\5\n\6\2\u009e\u009f\7\63\2\2\u009f\u00a0")
        buf.write("\5\f\7\2\u00a0\u00a1\7\64\2\2\u00a1\7\3\2\2\2\u00a2\u00a3")
        buf.write("\7<\2\2\u00a3\t\3\2\2\2\u00a4\u00a5\7!\2\2\u00a5\u00a8")
        buf.write("\7<\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\13\3\2\2\2\u00a9\u00ac\5\16\b\2\u00aa")
        buf.write("\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2")
        buf.write("\u00ac\r\3\2\2\2\u00ad\u00ae\5\20\t\2\u00ae\u00af\5\16")
        buf.write("\b\2\u00af\u00b2\3\2\2\2\u00b0\u00b2\5\20\t\2\u00b1\u00ad")
        buf.write("\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\17\3\2\2\2\u00b3\u00b7")
        buf.write("\5\22\n\2\u00b4\u00b7\5(\25\2\u00b5\u00b7\5\64\33\2\u00b6")
        buf.write("\u00b3\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2")
        buf.write("\u00b7\21\3\2\2\2\u00b8\u00bb\5\24\13\2\u00b9\u00bb\5")
        buf.write("\30\r\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb")
        buf.write("\23\3\2\2\2\u00bc\u00bd\5\u008eH\2\u00bd\u00be\5\26\f")
        buf.write("\2\u00be\u00bf\7-\2\2\u00bf\u00c0\5\34\17\2\u00c0\u00c1")
        buf.write("\7,\2\2\u00c1\25\3\2\2\2\u00c2\u00c3\5\u0090I\2\u00c3")
        buf.write("\u00c4\7+\2\2\u00c4\u00c5\5\26\f\2\u00c5\u00c8\3\2\2\2")
        buf.write("\u00c6\u00c8\5\u0090I\2\u00c7\u00c2\3\2\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\27\3\2\2\2\u00c9\u00ca\5\u008eH\2\u00ca")
        buf.write("\u00cb\5\u0090I\2\u00cb\u00cc\5\32\16\2\u00cc\u00cd\5")
        buf.write("d\63\2\u00cd\u00ce\7,\2\2\u00ce\31\3\2\2\2\u00cf\u00d0")
        buf.write("\7+\2\2\u00d0\u00d1\5\u0090I\2\u00d1\u00d2\5\32\16\2\u00d2")
        buf.write("\u00d3\5d\63\2\u00d3\u00d4\7+\2\2\u00d4\u00da\3\2\2\2")
        buf.write("\u00d5\u00d6\7-\2\2\u00d6\u00d7\5\34\17\2\u00d7\u00d8")
        buf.write("\7(\2\2\u00d8\u00da\3\2\2\2\u00d9\u00cf\3\2\2\2\u00d9")
        buf.write("\u00d5\3\2\2\2\u00da\33\3\2\2\2\u00db\u00df\5\36\20\2")
        buf.write("\u00dc\u00df\5\"\22\2\u00dd\u00df\5&\24\2\u00de\u00db")
        buf.write("\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df")
        buf.write("\35\3\2\2\2\u00e0\u00e1\t\2\2\2\u00e1\37\3\2\2\2\u00e2")
        buf.write("\u00e3\t\3\2\2\u00e3!\3\2\2\2\u00e4\u00e5\7\61\2\2\u00e5")
        buf.write("\u00e6\78\2\2\u00e6\u00e7\7\62\2\2\u00e7\u00e8\5$\23\2")
        buf.write("\u00e8#\3\2\2\2\u00e9\u00ec\5\36\20\2\u00ea\u00ec\5&\24")
        buf.write("\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec%\3\2")
        buf.write("\2\2\u00ed\u00ee\7<\2\2\u00ee\'\3\2\2\2\u00ef\u00f0\7")
        buf.write("\27\2\2\u00f0\u00f1\5\u0090I\2\u00f1\u00f2\7/\2\2\u00f2")
        buf.write("\u00f3\5*\26\2\u00f3\u00f4\7\60\2\2\u00f4\u00f5\7-\2\2")
        buf.write("\u00f5\u00f6\5\62\32\2\u00f6\u00f7\5\66\34\2\u00f7)\3")
        buf.write("\2\2\2\u00f8\u00fb\5,\27\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb+\3\2\2\2\u00fc\u00fd")
        buf.write("\5.\30\2\u00fd\u00fe\7+\2\2\u00fe\u00ff\5,\27\2\u00ff")
        buf.write("\u0102\3\2\2\2\u0100\u0102\5.\30\2\u0101\u00fc\3\2\2\2")
        buf.write("\u0101\u0100\3\2\2\2\u0102-\3\2\2\2\u0103\u0104\5\60\31")
        buf.write("\2\u0104\u0105\7-\2\2\u0105\u0106\5\34\17\2\u0106/\3\2")
        buf.write("\2\2\u0107\u0108\7<\2\2\u0108\u0109\7+\2\2\u0109\u010c")
        buf.write("\5\60\31\2\u010a\u010c\7<\2\2\u010b\u0107\3\2\2\2\u010b")
        buf.write("\u010a\3\2\2\2\u010c\61\3\2\2\2\u010d\u0111\5 \21\2\u010e")
        buf.write("\u0111\5\"\22\2\u010f\u0111\5&\24\2\u0110\u010d\3\2\2")
        buf.write("\2\u0110\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111\63\3")
        buf.write("\2\2\2\u0112\u0113\7\27\2\2\u0113\u0114\7\21\2\2\u0114")
        buf.write("\u0115\7/\2\2\u0115\u0116\5*\26\2\u0116\u0117\7\60\2\2")
        buf.write("\u0117\u0118\5\66\34\2\u0118\65\3\2\2\2\u0119\u011a\7")
        buf.write("\63\2\2\u011a\u011b\58\35\2\u011b\u011c\7\64\2\2\u011c")
        buf.write("\67\3\2\2\2\u011d\u0120\5:\36\2\u011e\u0120\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u01209\3\2\2\2\u0121")
        buf.write("\u0122\5<\37\2\u0122\u0123\5:\36\2\u0123\u0126\3\2\2\2")
        buf.write("\u0124\u0126\5<\37\2\u0125\u0121\3\2\2\2\u0125\u0124\3")
        buf.write("\2\2\2\u0126;\3\2\2\2\u0127\u0131\5> \2\u0128\u0131\5")
        buf.write("F$\2\u0129\u0131\5L\'\2\u012a\u0131\5P)\2\u012b\u0131")
        buf.write("\5R*\2\u012c\u0131\5T+\2\u012d\u0131\5V,\2\u012e\u0131")
        buf.write("\5X-\2\u012f\u0131\5\66\34\2\u0130\u0127\3\2\2\2\u0130")
        buf.write("\u0128\3\2\2\2\u0130\u0129\3\2\2\2\u0130\u012a\3\2\2\2")
        buf.write("\u0130\u012b\3\2\2\2\u0130\u012c\3\2\2\2\u0130\u012d\3")
        buf.write("\2\2\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131=")
        buf.write("\3\2\2\2\u0132\u0135\5\u008eH\2\u0133\u0136\5@!\2\u0134")
        buf.write("\u0136\5D#\2\u0135\u0133\3\2\2\2\u0135\u0134\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0138\7,\2\2\u0138?\3\2\2\2\u0139")
        buf.write("\u013a\5B\"\2\u013a\u013b\7-\2\2\u013b\u013c\5\34\17\2")
        buf.write("\u013cA\3\2\2\2\u013d\u013e\7<\2\2\u013e\u013f\7+\2\2")
        buf.write("\u013f\u0142\5B\"\2\u0140\u0142\7<\2\2\u0141\u013d\3\2")
        buf.write("\2\2\u0141\u0140\3\2\2\2\u0142C\3\2\2\2\u0143\u0144\7")
        buf.write("<\2\2\u0144\u0145\7+\2\2\u0145\u0146\5D#\2\u0146\u0147")
        buf.write("\7+\2\2\u0147\u0148\5d\63\2\u0148\u0150\3\2\2\2\u0149")
        buf.write("\u014a\7<\2\2\u014a\u014b\7-\2\2\u014b\u014c\5\34\17\2")
        buf.write("\u014c\u014d\7(\2\2\u014d\u014e\5d\63\2\u014e\u0150\3")
        buf.write("\2\2\2\u014f\u0143\3\2\2\2\u014f\u0149\3\2\2\2\u0150E")
        buf.write("\3\2\2\2\u0151\u0152\5H%\2\u0152\u0153\7\33\2\2\u0153")
        buf.write("\u0154\5d\63\2\u0154\u0155\7,\2\2\u0155G\3\2\2\2\u0156")
        buf.write("\u0165\7<\2\2\u0157\u0158\5^\60\2\u0158\u0159\7=\2\2\u0159")
        buf.write("\u0165\3\2\2\2\u015a\u015b\5t;\2\u015b\u015c\7.\2\2\u015c")
        buf.write("\u015d\7<\2\2\u015d\u0165\3\2\2\2\u015e\u015f\5t;\2\u015f")
        buf.write("\u0160\5\u008cG\2\u0160\u0161\7.\2\2\u0161\u0162\7<\2")
        buf.write("\2\u0162\u0165\3\2\2\2\u0163\u0165\5J&\2\u0164\u0156\3")
        buf.write("\2\2\2\u0164\u0157\3\2\2\2\u0164\u015a\3\2\2\2\u0164\u015e")
        buf.write("\3\2\2\2\u0164\u0163\3\2\2\2\u0165I\3\2\2\2\u0166\u0167")
        buf.write("\5r:\2\u0167\u0168\7\61\2\2\u0168\u0169\5d\63\2\u0169")
        buf.write("\u016a\7\62\2\2\u016aK\3\2\2\2\u016b\u016d\7\5\2\2\u016c")
        buf.write("\u016e\5\66\34\2\u016d\u016c\3\2\2\2\u016d\u016e\3\2\2")
        buf.write("\2\u016e\u016f\3\2\2\2\u016f\u0170\5d\63\2\u0170\u0173")
        buf.write("\5\66\34\2\u0171\u0172\7\6\2\2\u0172\u0174\5\66\34\2\u0173")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174M\3\2\2\2\u0175")
        buf.write("\u0176\5H%\2\u0176\u0177\7\33\2\2\u0177\u0178\5d\63\2")
        buf.write("\u0178O\3\2\2\2\u0179\u017a\7\7\2\2\u017a\u017b\5N(\2")
        buf.write("\u017b\u017c\7,\2\2\u017c\u017d\5d\63\2\u017d\u017e\7")
        buf.write(",\2\2\u017e\u017f\5N(\2\u017f\u0180\5\66\34\2\u0180Q\3")
        buf.write("\2\2\2\u0181\u0182\7\3\2\2\u0182\u0183\7,\2\2\u0183S\3")
        buf.write("\2\2\2\u0184\u0185\7\4\2\2\u0185\u0186\7,\2\2\u0186U\3")
        buf.write("\2\2\2\u0187\u0189\7\16\2\2\u0188\u018a\5d\63\2\u0189")
        buf.write("\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u018c\7,\2\2\u018cW\3\2\2\2\u018d\u018e\5Z.\2\u018e")
        buf.write("\u018f\7,\2\2\u018fY\3\2\2\2\u0190\u0193\5\\/\2\u0191")
        buf.write("\u0193\5`\61\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2")
        buf.write("\u0193[\3\2\2\2\u0194\u0195\5^\60\2\u0195\u0196\7=\2\2")
        buf.write("\u0196\u0198\7/\2\2\u0197\u0199\5\u008aF\2\u0198\u0197")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u019b\7\60\2\2\u019b]\3\2\2\2\u019c\u019d\t\4\2\2\u019d")
        buf.write("\u01a0\7.\2\2\u019e\u01a0\3\2\2\2\u019f\u019c\3\2\2\2")
        buf.write("\u019f\u019e\3\2\2\2\u01a0_\3\2\2\2\u01a1\u01a2\5b\62")
        buf.write("\2\u01a2\u01a3\7.\2\2\u01a3\u01a4\7<\2\2\u01a4\u01a6\7")
        buf.write("/\2\2\u01a5\u01a7\5\u008aF\2\u01a6\u01a5\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\7\60\2")
        buf.write("\2\u01a9a\3\2\2\2\u01aa\u01ab\b\62\1\2\u01ab\u01ac\5v")
        buf.write("<\2\u01ac\u01ba\3\2\2\2\u01ad\u01ae\f\5\2\2\u01ae\u01af")
        buf.write("\7.\2\2\u01af\u01b9\7<\2\2\u01b0\u01b1\f\4\2\2\u01b1\u01b2")
        buf.write("\7.\2\2\u01b2\u01b3\7<\2\2\u01b3\u01b5\7/\2\2\u01b4\u01b6")
        buf.write("\5\u008aF\2\u01b5\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b9\7\60\2\2\u01b8\u01ad\3\2\2")
        buf.write("\2\u01b8\u01b0\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bbc\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bd\u01be\5f\64\2\u01be\u01bf\7)\2\2\u01bf")
        buf.write("\u01c0\5f\64\2\u01c0\u01c3\3\2\2\2\u01c1\u01c3\5f\64\2")
        buf.write("\u01c2\u01bd\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3e\3\2\2")
        buf.write("\2\u01c4\u01c5\5h\65\2\u01c5\u01c6\t\5\2\2\u01c6\u01c7")
        buf.write("\5h\65\2\u01c7\u01ca\3\2\2\2\u01c8\u01ca\5h\65\2\u01c9")
        buf.write("\u01c4\3\2\2\2\u01c9\u01c8\3\2\2\2\u01cag\3\2\2\2\u01cb")
        buf.write("\u01cc\b\65\1\2\u01cc\u01cd\5j\66\2\u01cd\u01d3\3\2\2")
        buf.write("\2\u01ce\u01cf\f\4\2\2\u01cf\u01d0\t\6\2\2\u01d0\u01d2")
        buf.write("\5j\66\2\u01d1\u01ce\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4i\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d6\u01d7\b\66\1\2\u01d7\u01d8\5l\67")
        buf.write("\2\u01d8\u01de\3\2\2\2\u01d9\u01da\f\4\2\2\u01da\u01db")
        buf.write("\t\7\2\2\u01db\u01dd\5l\67\2\u01dc\u01d9\3\2\2\2\u01dd")
        buf.write("\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01dfk\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e2\b\67\1")
        buf.write("\2\u01e2\u01e3\5n8\2\u01e3\u01e9\3\2\2\2\u01e4\u01e5\f")
        buf.write("\4\2\2\u01e5\u01e6\t\b\2\2\u01e6\u01e8\5n8\2\u01e7\u01e4")
        buf.write("\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9")
        buf.write("\u01ea\3\2\2\2\u01eam\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec")
        buf.write("\u01ed\7\'\2\2\u01ed\u01f0\5n8\2\u01ee\u01f0\5p9\2\u01ef")
        buf.write("\u01ec\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0o\3\2\2\2\u01f1")
        buf.write("\u01f2\7#\2\2\u01f2\u01f5\5p9\2\u01f3\u01f5\5r:\2\u01f4")
        buf.write("\u01f1\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5q\3\2\2\2\u01f6")
        buf.write("\u01f7\b:\1\2\u01f7\u01f8\5t;\2\u01f8\u01fd\3\2\2\2\u01f9")
        buf.write("\u01fa\f\4\2\2\u01fa\u01fc\5\u008cG\2\u01fb\u01f9\3\2")
        buf.write("\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fes\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0201")
        buf.write("\b;\1\2\u0201\u0202\5v<\2\u0202\u020b\3\2\2\2\u0203\u0204")
        buf.write("\f\4\2\2\u0204\u0207\7.\2\2\u0205\u0208\7<\2\2\u0206\u0208")
        buf.write("\5z>\2\u0207\u0205\3\2\2\2\u0207\u0206\3\2\2\2\u0208\u020a")
        buf.write("\3\2\2\2\u0209\u0203\3\2\2\2\u020a\u020d\3\2\2\2\u020b")
        buf.write("\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020cu\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020e\u0211\5^\60\2\u020f\u0212\7=\2\2")
        buf.write("\u0210\u0212\5|?\2\u0211\u020f\3\2\2\2\u0211\u0210\3\2")
        buf.write("\2\2\u0212\u0215\3\2\2\2\u0213\u0215\5x=\2\u0214\u020e")
        buf.write("\3\2\2\2\u0214\u0213\3\2\2\2\u0215w\3\2\2\2\u0216\u0217")
        buf.write("\7\24\2\2\u0217\u0218\7<\2\2\u0218\u021a\7/\2\2\u0219")
        buf.write("\u021b\5\u008aF\2\u021a\u0219\3\2\2\2\u021a\u021b\3\2")
        buf.write("\2\2\u021b\u021c\3\2\2\2\u021c\u021f\7\60\2\2\u021d\u021f")
        buf.write("\5~@\2\u021e\u0216\3\2\2\2\u021e\u021d\3\2\2\2\u021fy")
        buf.write("\3\2\2\2\u0220\u0221\7<\2\2\u0221\u0223\7/\2\2\u0222\u0224")
        buf.write("\5\u008aF\2\u0223\u0222\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u0225\3\2\2\2\u0225\u0226\7\60\2\2\u0226{\3\2\2\2\u0227")
        buf.write("\u0228\7=\2\2\u0228\u022a\7/\2\2\u0229\u022b\5\u008aF")
        buf.write("\2\u022a\u0229\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c")
        buf.write("\3\2\2\2\u022c\u022d\7\60\2\2\u022d}\3\2\2\2\u022e\u0237")
        buf.write("\7<\2\2\u022f\u0230\7/\2\2\u0230\u0231\5d\63\2\u0231\u0232")
        buf.write("\7\60\2\2\u0232\u0237\3\2\2\2\u0233\u0237\5\u0080A\2\u0234")
        buf.write("\u0237\7\23\2\2\u0235\u0237\7\17\2\2\u0236\u022e\3\2\2")
        buf.write("\2\u0236\u022f\3\2\2\2\u0236\u0233\3\2\2\2\u0236\u0234")
        buf.write("\3\2\2\2\u0236\u0235\3\2\2\2\u0237\177\3\2\2\2\u0238\u023f")
        buf.write("\78\2\2\u0239\u023f\79\2\2\u023a\u023f\7:\2\2\u023b\u023f")
        buf.write("\7;\2\2\u023c\u023f\5\u0084C\2\u023d\u023f\5\u0086D\2")
        buf.write("\u023e\u0238\3\2\2\2\u023e\u0239\3\2\2\2\u023e\u023a\3")
        buf.write("\2\2\2\u023e\u023b\3\2\2\2\u023e\u023c\3\2\2\2\u023e\u023d")
        buf.write("\3\2\2\2\u023f\u0081\3\2\2\2\u0240\u0246\78\2\2\u0241")
        buf.write("\u0246\79\2\2\u0242\u0246\7:\2\2\u0243\u0246\7;\2\2\u0244")
        buf.write("\u0246\5\u0084C\2\u0245\u0240\3\2\2\2\u0245\u0241\3\2")
        buf.write("\2\2\u0245\u0242\3\2\2\2\u0245\u0243\3\2\2\2\u0245\u0244")
        buf.write("\3\2\2\2\u0246\u0083\3\2\2\2\u0247\u0248\t\t\2\2\u0248")
        buf.write("\u0085\3\2\2\2\u0249\u024a\7\61\2\2\u024a\u024b\5\u0088")
        buf.write("E\2\u024b\u024c\7\62\2\2\u024c\u0087\3\2\2\2\u024d\u024e")
        buf.write("\5\u0082B\2\u024e\u024f\7+\2\2\u024f\u0250\5\u0088E\2")
        buf.write("\u0250\u0253\3\2\2\2\u0251\u0253\5\u0082B\2\u0252\u024d")
        buf.write("\3\2\2\2\u0252\u0251\3\2\2\2\u0253\u0089\3\2\2\2\u0254")
        buf.write("\u0255\5d\63\2\u0255\u0256\7+\2\2\u0256\u0257\5\u008a")
        buf.write("F\2\u0257\u025a\3\2\2\2\u0258\u025a\5d\63\2\u0259\u0254")
        buf.write("\3\2\2\2\u0259\u0258\3\2\2\2\u025a\u008b\3\2\2\2\u025b")
        buf.write("\u025c\7\61\2\2\u025c\u025d\5d\63\2\u025d\u025e\7\62\2")
        buf.write("\2\u025e\u008d\3\2\2\2\u025f\u0260\t\n\2\2\u0260\u008f")
        buf.write("\3\2\2\2\u0261\u0262\t\13\2\2\u0262\u0091\3\2\2\2\66\u0099")
        buf.write("\u00a7\u00ab\u00b1\u00b6\u00ba\u00c7\u00d9\u00de\u00eb")
        buf.write("\u00fa\u0101\u010b\u0110\u011f\u0125\u0130\u0135\u0141")
        buf.write("\u014f\u0164\u016d\u0173\u0189\u0192\u0198\u019f\u01a6")
        buf.write("\u01b5\u01b8\u01ba\u01c2\u01c9\u01d3\u01de\u01e9\u01ef")
        buf.write("\u01f4\u01fd\u0207\u020b\u0211\u0214\u021a\u021e\u0223")
        buf.write("\u022a\u0236\u023e\u0245\u0252\u0259")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'continue'", "'if'", "'else'", 
                     "'for'", "'true'", "'false'", "'int'", "'float'", "'bool'", 
                     "'string'", "'return'", "'null'", "'class'", "'constructor'", 
                     "'var'", "'self'", "'new'", "'void'", "'const'", "'func'", 
                     "'&&'", "'||'", "'=='", "':='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'<-'", "'+'", "'-'", "'*'", "'/'", 
                     "'\\'", "'!'", "'='", "'^'", "'%'", "','", "';'", "':'", 
                     "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
                      "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
                      "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                      "NEW", "VOID", "CONST", "FUNC", "AND", "OR", "EQUAL", 
                      "ASSIGN", "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", 
                      "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", "SUPERCLASS", 
                      "ADD", "SUB", "MUL", "DIV_FLOAT", "DIV_INT", "NOT", 
                      "EQ", "STRING_CONCAT", "MOD", "COMMA", "SEMI", "COLON", 
                      "DOT", "LP", "RP", "LSB", "RSB", "LB", "RB", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "WS", "INTARR", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "ID", "STATIC_ID", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_declarelist = 1
    RULE_class_declare = 2
    RULE_name_class = 3
    RULE_name_superclass = 4
    RULE_body_class_list = 5
    RULE_body_class_prime = 6
    RULE_body_class = 7
    RULE_attribute_declare = 8
    RULE_attdecl_ = 9
    RULE_indenlist = 10
    RULE_attdecl = 11
    RULE_varlist = 12
    RULE_type_att = 13
    RULE_primitive_type = 14
    RULE_primitive_type_ = 15
    RULE_array_type = 16
    RULE_element_type = 17
    RULE_class_type = 18
    RULE_method_declare = 19
    RULE_paramlist = 20
    RULE_paramprime = 21
    RULE_param = 22
    RULE_idlist = 23
    RULE_type_return = 24
    RULE_constructor_declare = 25
    RULE_blockstmt = 26
    RULE_stmtlist = 27
    RULE_stmtprime = 28
    RULE_stmt = 29
    RULE_var_and_const_declstmt = 30
    RULE_varstmt_decl = 31
    RULE_variable_namelist = 32
    RULE_varstmt_declass = 33
    RULE_assignment_stmt = 34
    RULE_assign_lhs = 35
    RULE_index_exp_for_scalar_variable = 36
    RULE_if_stmt = 37
    RULE_assignstmt = 38
    RULE_for_stmt = 39
    RULE_break_stmt = 40
    RULE_continue_stmt = 41
    RULE_return_stmt = 42
    RULE_method_invocation_stmt = 43
    RULE_method_invocation = 44
    RULE_static_method_invocation = 45
    RULE_name_class_access = 46
    RULE_instance_method_invocation = 47
    RULE_pre_exp = 48
    RULE_expr = 49
    RULE_expr1 = 50
    RULE_expr2 = 51
    RULE_expr3 = 52
    RULE_expr4 = 53
    RULE_expr5 = 54
    RULE_expr6 = 55
    RULE_expr7 = 56
    RULE_expr8 = 57
    RULE_expr9 = 58
    RULE_expr10 = 59
    RULE_funcall = 60
    RULE_static_funcall = 61
    RULE_operands = 62
    RULE_literals = 63
    RULE_literal_array = 64
    RULE_boolean_literal = 65
    RULE_array_literal = 66
    RULE_litarray_list = 67
    RULE_exp_list = 68
    RULE_index_operator = 69
    RULE_attribute_name = 70
    RULE_identifier_name = 71

    ruleNames =  [ "program", "class_declarelist", "class_declare", "name_class", 
                   "name_superclass", "body_class_list", "body_class_prime", 
                   "body_class", "attribute_declare", "attdecl_", "indenlist", 
                   "attdecl", "varlist", "type_att", "primitive_type", "primitive_type_", 
                   "array_type", "element_type", "class_type", "method_declare", 
                   "paramlist", "paramprime", "param", "idlist", "type_return", 
                   "constructor_declare", "blockstmt", "stmtlist", "stmtprime", 
                   "stmt", "var_and_const_declstmt", "varstmt_decl", "variable_namelist", 
                   "varstmt_declass", "assignment_stmt", "assign_lhs", "index_exp_for_scalar_variable", 
                   "if_stmt", "assignstmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invocation_stmt", "method_invocation", 
                   "static_method_invocation", "name_class_access", "instance_method_invocation", 
                   "pre_exp", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "funcall", "static_funcall", "operands", "literals", 
                   "literal_array", "boolean_literal", "array_literal", 
                   "litarray_list", "exp_list", "index_operator", "attribute_name", 
                   "identifier_name" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSE=4
    FOR=5
    TRUE=6
    FALSE=7
    INT=8
    FLOAT=9
    BOOL=10
    STRING=11
    RETURN=12
    NULL=13
    CLASS=14
    CONSTRUCTOR=15
    VAR=16
    SELF=17
    NEW=18
    VOID=19
    CONST=20
    FUNC=21
    AND=22
    OR=23
    EQUAL=24
    ASSIGN=25
    NOT_EQUAL=26
    LESS_THAN=27
    GREATER_THAN=28
    LESS_THAN_EQUAL=29
    GREATER_THAN_EQUAL=30
    SUPERCLASS=31
    ADD=32
    SUB=33
    MUL=34
    DIV_FLOAT=35
    DIV_INT=36
    NOT=37
    EQ=38
    STRING_CONCAT=39
    MOD=40
    COMMA=41
    SEMI=42
    COLON=43
    DOT=44
    LP=45
    RP=46
    LSB=47
    RSB=48
    LB=49
    RB=50
    LINE_COMMENT=51
    BLOCK_COMMENT=52
    WS=53
    INTARR=54
    INTLIT=55
    FLOATLIT=56
    STRINGLIT=57
    ID=58
    STATIC_ID=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declarelist(self):
            return self.getTypedRuleContext(CSlangParser.Class_declarelistContext,0)


        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.class_declarelist()
            self.state = 145
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declare(self):
            return self.getTypedRuleContext(CSlangParser.Class_declareContext,0)


        def class_declarelist(self):
            return self.getTypedRuleContext(CSlangParser.Class_declarelistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_declarelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declarelist" ):
                return visitor.visitClass_declarelist(self)
            else:
                return visitor.visitChildren(self)




    def class_declarelist(self):

        localctx = CSlangParser.Class_declarelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declarelist)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.class_declare()
                self.state = 148
                self.class_declarelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.class_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def name_class(self):
            return self.getTypedRuleContext(CSlangParser.Name_classContext,0)


        def name_superclass(self):
            return self.getTypedRuleContext(CSlangParser.Name_superclassContext,0)


        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def body_class_list(self):
            return self.getTypedRuleContext(CSlangParser.Body_class_listContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = CSlangParser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(CSlangParser.CLASS)
            self.state = 154
            self.name_class()
            self.state = 155
            self.name_superclass()
            self.state = 156
            self.match(CSlangParser.LB)
            self.state = 157
            self.body_class_list()
            self.state = 158
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_name_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_class" ):
                return visitor.visitName_class(self)
            else:
                return visitor.visitChildren(self)




    def name_class(self):

        localctx = CSlangParser.Name_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(CSlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_superclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUPERCLASS(self):
            return self.getToken(CSlangParser.SUPERCLASS, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_name_superclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_superclass" ):
                return visitor.visitName_superclass(self)
            else:
                return visitor.visitChildren(self)




    def name_superclass(self):

        localctx = CSlangParser.Name_superclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_name_superclass)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUPERCLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(CSlangParser.SUPERCLASS)
                self.state = 163
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.LB]:
                self.enterOuterAlt(localctx, 2)

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


    class Body_class_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_class_prime(self):
            return self.getTypedRuleContext(CSlangParser.Body_class_primeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_body_class_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_class_list" ):
                return visitor.visitBody_class_list(self)
            else:
                return visitor.visitChildren(self)




    def body_class_list(self):

        localctx = CSlangParser.Body_class_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_body_class_list)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.body_class_prime()
                pass
            elif token in [CSlangParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class Body_class_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_class(self):
            return self.getTypedRuleContext(CSlangParser.Body_classContext,0)


        def body_class_prime(self):
            return self.getTypedRuleContext(CSlangParser.Body_class_primeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_body_class_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_class_prime" ):
                return visitor.visitBody_class_prime(self)
            else:
                return visitor.visitChildren(self)




    def body_class_prime(self):

        localctx = CSlangParser.Body_class_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body_class_prime)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.body_class()
                self.state = 172
                self.body_class_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.body_class()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declare(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_declareContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(CSlangParser.Method_declareContext,0)


        def constructor_declare(self):
            return self.getTypedRuleContext(CSlangParser.Constructor_declareContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_body_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_class" ):
                return visitor.visitBody_class(self)
            else:
                return visitor.visitChildren(self)




    def body_class(self):

        localctx = CSlangParser.Body_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_body_class)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.attribute_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.method_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.constructor_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attdecl_(self):
            return self.getTypedRuleContext(CSlangParser.Attdecl_Context,0)


        def attdecl(self):
            return self.getTypedRuleContext(CSlangParser.AttdeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declare" ):
                return visitor.visitAttribute_declare(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declare(self):

        localctx = CSlangParser.Attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_declare)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.attdecl_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.attdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attdecl_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_nameContext,0)


        def indenlist(self):
            return self.getTypedRuleContext(CSlangParser.IndenlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def type_att(self):
            return self.getTypedRuleContext(CSlangParser.Type_attContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attdecl_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttdecl_" ):
                return visitor.visitAttdecl_(self)
            else:
                return visitor.visitChildren(self)




    def attdecl_(self):

        localctx = CSlangParser.Attdecl_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attdecl_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.attribute_name()
            self.state = 187
            self.indenlist()
            self.state = 188
            self.match(CSlangParser.COLON)
            self.state = 189
            self.type_att()
            self.state = 190
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndenlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_name(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_nameContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def indenlist(self):
            return self.getTypedRuleContext(CSlangParser.IndenlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_indenlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndenlist" ):
                return visitor.visitIndenlist(self)
            else:
                return visitor.visitChildren(self)




    def indenlist(self):

        localctx = CSlangParser.IndenlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_indenlist)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.identifier_name()
                self.state = 193
                self.match(CSlangParser.COMMA)
                self.state = 194
                self.indenlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.identifier_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_nameContext,0)


        def identifier_name(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_nameContext,0)


        def varlist(self):
            return self.getTypedRuleContext(CSlangParser.VarlistContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttdecl" ):
                return visitor.visitAttdecl(self)
            else:
                return visitor.visitChildren(self)




    def attdecl(self):

        localctx = CSlangParser.AttdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.attribute_name()
            self.state = 200
            self.identifier_name()
            self.state = 201
            self.varlist()
            self.state = 202
            self.expr()
            self.state = 203
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def identifier_name(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_nameContext,0)


        def varlist(self):
            return self.getTypedRuleContext(CSlangParser.VarlistContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def type_att(self):
            return self.getTypedRuleContext(CSlangParser.Type_attContext,0)


        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_varlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist" ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = CSlangParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varlist)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(CSlangParser.COMMA)
                self.state = 206
                self.identifier_name()
                self.state = 207
                self.varlist()
                self.state = 208
                self.expr()
                self.state = 209
                self.match(CSlangParser.COMMA)
                pass
            elif token in [CSlangParser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(CSlangParser.COLON)
                self.state = 212
                self.type_att()
                self.state = 213
                self.match(CSlangParser.EQ)
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


    class Type_attContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(CSlangParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(CSlangParser.Class_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_type_att

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_att" ):
                return visitor.visitType_att(self)
            else:
                return visitor.visitChildren(self)




    def type_att(self):

        localctx = CSlangParser.Type_attContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type_att)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.primitive_type()
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.array_type()
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.class_type()
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


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = CSlangParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING))) != 0)):
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


    class Primitive_type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_primitive_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type_" ):
                return visitor.visitPrimitive_type_(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type_(self):

        localctx = CSlangParser.Primitive_type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_primitive_type_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING) | (1 << CSlangParser.VOID))) != 0)):
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def INTARR(self):
            return self.getToken(CSlangParser.INTARR, 0)

        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def element_type(self):
            return self.getTypedRuleContext(CSlangParser.Element_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(CSlangParser.LSB)
            self.state = 227
            self.match(CSlangParser.INTARR)
            self.state = 228
            self.match(CSlangParser.RSB)
            self.state = 229
            self.element_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(CSlangParser.Primitive_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(CSlangParser.Class_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_type" ):
                return visitor.visitElement_type(self)
            else:
                return visitor.visitChildren(self)




    def element_type(self):

        localctx = CSlangParser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_element_type)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.primitive_type()
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.class_type()
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


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = CSlangParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(CSlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def identifier_name(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_nameContext,0)


        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def type_return(self):
            return self.getTypedRuleContext(CSlangParser.Type_returnContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = CSlangParser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_method_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(CSlangParser.FUNC)
            self.state = 238
            self.identifier_name()
            self.state = 239
            self.match(CSlangParser.LP)
            self.state = 240
            self.paramlist()
            self.state = 241
            self.match(CSlangParser.RP)
            self.state = 242
            self.match(CSlangParser.COLON)
            self.state = 243
            self.type_return()
            self.state = 244
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(CSlangParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = CSlangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_paramlist)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.paramprime()
                pass
            elif token in [CSlangParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(CSlangParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(CSlangParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = CSlangParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_paramprime)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.param()
                self.state = 251
                self.match(CSlangParser.COMMA)
                self.state = 252
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(CSlangParser.IdlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def type_att(self):
            return self.getTypedRuleContext(CSlangParser.Type_attContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.idlist()
            self.state = 258
            self.match(CSlangParser.COLON)
            self.state = 259
            self.type_att()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(CSlangParser.IdlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = CSlangParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_idlist)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(CSlangParser.ID)
                self.state = 262
                self.match(CSlangParser.COMMA)
                self.state = 263
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(CSlangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type_(self):
            return self.getTypedRuleContext(CSlangParser.Primitive_type_Context,0)


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(CSlangParser.Class_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_type_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_return" ):
                return visitor.visitType_return(self)
            else:
                return visitor.visitChildren(self)




    def type_return(self):

        localctx = CSlangParser.Type_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_type_return)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.primitive_type_()
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.array_type()
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.class_type()
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


    class Constructor_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_declare" ):
                return visitor.visitConstructor_declare(self)
            else:
                return visitor.visitChildren(self)




    def constructor_declare(self):

        localctx = CSlangParser.Constructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_constructor_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(CSlangParser.FUNC)
            self.state = 273
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 274
            self.match(CSlangParser.LP)
            self.state = 275
            self.paramlist()
            self.state = 276
            self.match(CSlangParser.RP)
            self.state = 277
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(CSlangParser.StmtlistContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = CSlangParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(CSlangParser.LB)
            self.state = 280
            self.stmtlist()
            self.state = 281
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtprime(self):
            return self.getTypedRuleContext(CSlangParser.StmtprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = CSlangParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmtlist)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.LP, CSlangParser.LSB, CSlangParser.LB, CSlangParser.INTARR, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.STATIC_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.stmtprime()
                pass
            elif token in [CSlangParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class StmtprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CSlangParser.StmtContext,0)


        def stmtprime(self):
            return self.getTypedRuleContext(CSlangParser.StmtprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtprime" ):
                return visitor.visitStmtprime(self)
            else:
                return visitor.visitChildren(self)




    def stmtprime(self):

        localctx = CSlangParser.StmtprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmtprime)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.stmt()
                self.state = 288
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_and_const_declstmt(self):
            return self.getTypedRuleContext(CSlangParser.Var_and_const_declstmtContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Assignment_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(CSlangParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(CSlangParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Return_stmtContext,0)


        def method_invocation_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Method_invocation_stmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.var_and_const_declstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 297
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 298
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 299
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 300
                self.method_invocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 301
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_and_const_declstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_nameContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def varstmt_decl(self):
            return self.getTypedRuleContext(CSlangParser.Varstmt_declContext,0)


        def varstmt_declass(self):
            return self.getTypedRuleContext(CSlangParser.Varstmt_declassContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_var_and_const_declstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_and_const_declstmt" ):
                return visitor.visitVar_and_const_declstmt(self)
            else:
                return visitor.visitChildren(self)




    def var_and_const_declstmt(self):

        localctx = CSlangParser.Var_and_const_declstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_var_and_const_declstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.attribute_name()
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 305
                self.varstmt_decl()
                pass

            elif la_ == 2:
                self.state = 306
                self.varstmt_declass()
                pass


            self.state = 309
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varstmt_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_namelist(self):
            return self.getTypedRuleContext(CSlangParser.Variable_namelistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def type_att(self):
            return self.getTypedRuleContext(CSlangParser.Type_attContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_varstmt_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarstmt_decl" ):
                return visitor.visitVarstmt_decl(self)
            else:
                return visitor.visitChildren(self)




    def varstmt_decl(self):

        localctx = CSlangParser.Varstmt_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_varstmt_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.variable_namelist()
            self.state = 312
            self.match(CSlangParser.COLON)
            self.state = 313
            self.type_att()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_namelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def variable_namelist(self):
            return self.getTypedRuleContext(CSlangParser.Variable_namelistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_variable_namelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_namelist" ):
                return visitor.visitVariable_namelist(self)
            else:
                return visitor.visitChildren(self)




    def variable_namelist(self):

        localctx = CSlangParser.Variable_namelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_variable_namelist)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(CSlangParser.ID)
                self.state = 316
                self.match(CSlangParser.COMMA)
                self.state = 317
                self.variable_namelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(CSlangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varstmt_declassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def varstmt_declass(self):
            return self.getTypedRuleContext(CSlangParser.Varstmt_declassContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def type_att(self):
            return self.getTypedRuleContext(CSlangParser.Type_attContext,0)


        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_varstmt_declass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarstmt_declass" ):
                return visitor.visitVarstmt_declass(self)
            else:
                return visitor.visitChildren(self)




    def varstmt_declass(self):

        localctx = CSlangParser.Varstmt_declassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_varstmt_declass)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(CSlangParser.ID)
                self.state = 322
                self.match(CSlangParser.COMMA)
                self.state = 323
                self.varstmt_declass()
                self.state = 324
                self.match(CSlangParser.COMMA)
                self.state = 325
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(CSlangParser.ID)
                self.state = 328
                self.match(CSlangParser.COLON)
                self.state = 329
                self.type_att()
                self.state = 330
                self.match(CSlangParser.EQ)
                self.state = 331
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(CSlangParser.Assign_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assignment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = CSlangParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.assign_lhs()
            self.state = 336
            self.match(CSlangParser.ASSIGN)
            self.state = 337
            self.expr()
            self.state = 338
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def name_class_access(self):
            return self.getTypedRuleContext(CSlangParser.Name_class_accessContext,0)


        def STATIC_ID(self):
            return self.getToken(CSlangParser.STATIC_ID, 0)

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def index_operator(self):
            return self.getTypedRuleContext(CSlangParser.Index_operatorContext,0)


        def index_exp_for_scalar_variable(self):
            return self.getTypedRuleContext(CSlangParser.Index_exp_for_scalar_variableContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = CSlangParser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assign_lhs)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.name_class_access()
                self.state = 342
                self.match(CSlangParser.STATIC_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 344
                self.expr8(0)
                self.state = 345
                self.match(CSlangParser.DOT)
                self.state = 346
                self.match(CSlangParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 348
                self.expr8(0)
                self.state = 349
                self.index_operator()
                self.state = 350
                self.match(CSlangParser.DOT)
                self.state = 351
                self.match(CSlangParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 353
                self.index_exp_for_scalar_variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exp_for_scalar_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_index_exp_for_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_exp_for_scalar_variable" ):
                return visitor.visitIndex_exp_for_scalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def index_exp_for_scalar_variable(self):

        localctx = CSlangParser.Index_exp_for_scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_index_exp_for_scalar_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.expr7(0)
            self.state = 357
            self.match(CSlangParser.LSB)
            self.state = 358
            self.expr()
            self.state = 359
            self.match(CSlangParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def blockstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.BlockstmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.BlockstmtContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = CSlangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(CSlangParser.IF)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LB:
                self.state = 362
                self.blockstmt()


            self.state = 365
            self.expr()
            self.state = 366
            self.blockstmt()
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 367
                self.match(CSlangParser.ELSE)
                self.state = 368
                self.blockstmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(CSlangParser.Assign_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = CSlangParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.assign_lhs()
            self.state = 372
            self.match(CSlangParser.ASSIGN)
            self.state = 373
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assignstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.AssignstmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.AssignstmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMI)
            else:
                return self.getToken(CSlangParser.SEMI, i)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = CSlangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(CSlangParser.FOR)
            self.state = 376
            self.assignstmt()
            self.state = 377
            self.match(CSlangParser.SEMI)
            self.state = 378
            self.expr()
            self.state = 379
            self.match(CSlangParser.SEMI)
            self.state = 380
            self.assignstmt()
            self.state = 381
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = CSlangParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(CSlangParser.BREAK)
            self.state = 384
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = CSlangParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(CSlangParser.CONTINUE)
            self.state = 387
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = CSlangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(CSlangParser.RETURN)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.INTARR) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.STATIC_ID))) != 0):
                self.state = 390
                self.expr()


            self.state = 393
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invocation(self):
            return self.getTypedRuleContext(CSlangParser.Method_invocationContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = CSlangParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.method_invocation()
            self.state = 396
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_method_invocation(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_invocationContext,0)


        def instance_method_invocation(self):
            return self.getTypedRuleContext(CSlangParser.Instance_method_invocationContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation" ):
                return visitor.visitMethod_invocation(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation(self):

        localctx = CSlangParser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_method_invocation)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.static_method_invocation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.instance_method_invocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_class_access(self):
            return self.getTypedRuleContext(CSlangParser.Name_class_accessContext,0)


        def STATIC_ID(self):
            return self.getToken(CSlangParser.STATIC_ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_static_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invocation" ):
                return visitor.visitStatic_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invocation(self):

        localctx = CSlangParser.Static_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_static_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.name_class_access()
            self.state = 403
            self.match(CSlangParser.STATIC_ID)
            self.state = 404
            self.match(CSlangParser.LP)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.INTARR) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.STATIC_ID))) != 0):
                self.state = 405
                self.exp_list()


            self.state = 408
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_class_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_name_class_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_class_access" ):
                return visitor.visitName_class_access(self)
            else:
                return visitor.visitChildren(self)




    def name_class_access(self):

        localctx = CSlangParser.Name_class_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_name_class_access)
        self._la = 0 # Token type
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SELF, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                _la = self._input.LA(1)
                if not(_la==CSlangParser.SELF or _la==CSlangParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 411
                self.match(CSlangParser.DOT)
                pass
            elif token in [CSlangParser.STATIC_ID]:
                self.enterOuterAlt(localctx, 2)

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


    class Instance_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pre_exp(self):
            return self.getTypedRuleContext(CSlangParser.Pre_expContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_instance_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invocation" ):
                return visitor.visitInstance_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invocation(self):

        localctx = CSlangParser.Instance_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_instance_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.pre_exp(0)
            self.state = 416
            self.match(CSlangParser.DOT)
            self.state = 417
            self.match(CSlangParser.ID)
            self.state = 418
            self.match(CSlangParser.LP)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.INTARR) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.STATIC_ID))) != 0):
                self.state = 419
                self.exp_list()


            self.state = 422
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pre_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def pre_exp(self):
            return self.getTypedRuleContext(CSlangParser.Pre_expContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_pre_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPre_exp" ):
                return visitor.visitPre_exp(self)
            else:
                return visitor.visitChildren(self)



    def pre_exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Pre_expContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_pre_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 440
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 438
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Pre_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pre_exp)
                        self.state = 427
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 428
                        self.match(CSlangParser.DOT)
                        self.state = 429
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Pre_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pre_exp)
                        self.state = 430
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 431
                        self.match(CSlangParser.DOT)
                        self.state = 432
                        self.match(CSlangParser.ID)
                        self.state = 433
                        self.match(CSlangParser.LP)
                        self.state = 435
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.INTARR) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.STATIC_ID))) != 0):
                            self.state = 434
                            self.exp_list()


                        self.state = 437
                        self.match(CSlangParser.RP)
                        pass

             
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr1Context,i)


        def STRING_CONCAT(self):
            return self.getToken(CSlangParser.STRING_CONCAT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CSlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.expr1()
                self.state = 444
                self.match(CSlangParser.STRING_CONCAT)
                self.state = 445
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(CSlangParser.NOT_EQUAL, 0)

        def LESS_THAN_EQUAL(self):
            return self.getToken(CSlangParser.LESS_THAN_EQUAL, 0)

        def GREATER_THAN_EQUAL(self):
            return self.getToken(CSlangParser.GREATER_THAN_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(CSlangParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(CSlangParser.GREATER_THAN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = CSlangParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.expr2(0)
                self.state = 451
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.NOT_EQUAL) | (1 << CSlangParser.LESS_THAN) | (1 << CSlangParser.GREATER_THAN) | (1 << CSlangParser.LESS_THAN_EQUAL) | (1 << CSlangParser.GREATER_THAN_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 452
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 460
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 461
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 462
                    self.expr3(0) 
                self.state = 467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 476
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 471
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 472
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 473
                    self.expr4(0) 
                self.state = 478
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(CSlangParser.MUL, 0)

        def DIV_FLOAT(self):
            return self.getToken(CSlangParser.DIV_FLOAT, 0)

        def DIV_INT(self):
            return self.getToken(CSlangParser.DIV_INT, 0)

        def MOD(self):
            return self.getToken(CSlangParser.MOD, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 487
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 482
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 483
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL) | (1 << CSlangParser.DIV_FLOAT) | (1 << CSlangParser.DIV_INT) | (1 << CSlangParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 484
                    self.expr5() 
                self.state = 489
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = CSlangParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_expr5)
        try:
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.match(CSlangParser.NOT)
                self.state = 491
                self.expr5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB, CSlangParser.LP, CSlangParser.LSB, CSlangParser.INTARR, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.STATIC_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expr6)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(CSlangParser.SUB)
                self.state = 496
                self.expr6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LP, CSlangParser.LSB, CSlangParser.INTARR, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.STATIC_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self.expr7(0)
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(CSlangParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 507
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 503
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 504
                    self.index_operator() 
                self.state = 509
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(CSlangParser.FuncallContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 521
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 513
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 514
                    self.match(CSlangParser.DOT)
                    self.state = 517
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 515
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 516
                        self.funcall()
                        pass

             
                self.state = 523
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_class_access(self):
            return self.getTypedRuleContext(CSlangParser.Name_class_accessContext,0)


        def STATIC_ID(self):
            return self.getToken(CSlangParser.STATIC_ID, 0)

        def static_funcall(self):
            return self.getTypedRuleContext(CSlangParser.Static_funcallContext,0)


        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = CSlangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_expr9)
        try:
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.name_class_access()
                self.state = 527
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 525
                    self.match(CSlangParser.STATIC_ID)
                    pass

                elif la_ == 2:
                    self.state = 526
                    self.static_funcall()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def operands(self):
            return self.getTypedRuleContext(CSlangParser.OperandsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(CSlangParser.NEW)
                self.state = 533
                self.match(CSlangParser.ID)
                self.state = 534
                self.match(CSlangParser.LP)
                self.state = 536
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.INTARR) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.STATIC_ID))) != 0):
                    self.state = 535
                    self.exp_list()


                self.state = 538
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LP, CSlangParser.LSB, CSlangParser.INTARR, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.operands()
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


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = CSlangParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(CSlangParser.ID)
            self.state = 543
            self.match(CSlangParser.LP)
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.INTARR) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.STATIC_ID))) != 0):
                self.state = 544
                self.exp_list()


            self.state = 547
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_funcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_ID(self):
            return self.getToken(CSlangParser.STATIC_ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_static_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_funcall" ):
                return visitor.visitStatic_funcall(self)
            else:
                return visitor.visitChildren(self)




    def static_funcall(self):

        localctx = CSlangParser.Static_funcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_static_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(CSlangParser.STATIC_ID)
            self.state = 550
            self.match(CSlangParser.LP)
            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.LP) | (1 << CSlangParser.LSB) | (1 << CSlangParser.INTARR) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.STATIC_ID))) != 0):
                self.state = 551
                self.exp_list()


            self.state = 554
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def literals(self):
            return self.getTypedRuleContext(CSlangParser.LiteralsContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = CSlangParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_operands)
        try:
            self.state = 564
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
                self.match(CSlangParser.LP)
                self.state = 558
                self.expr()
                self.state = 559
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LSB, CSlangParser.INTARR, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 561
                self.literals()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 562
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 563
                self.match(CSlangParser.NULL)
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


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTARR(self):
            return self.getToken(CSlangParser.INTARR, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(CSlangParser.Boolean_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(CSlangParser.Array_literalContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = CSlangParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_literals)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTARR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.match(CSlangParser.INTARR)
                pass
            elif token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 568
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 569
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 570
                self.boolean_literal()
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 571
                self.array_literal()
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


    class Literal_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTARR(self):
            return self.getToken(CSlangParser.INTARR, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(CSlangParser.Boolean_literalContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literal_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_array" ):
                return visitor.visitLiteral_array(self)
            else:
                return visitor.visitChildren(self)




    def literal_array(self):

        localctx = CSlangParser.Literal_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_literal_array)
        try:
            self.state = 579
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTARR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self.match(CSlangParser.INTARR)
                pass
            elif token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 575
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 576
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 577
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 578
                self.boolean_literal()
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


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = CSlangParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            _la = self._input.LA(1)
            if not(_la==CSlangParser.TRUE or _la==CSlangParser.FALSE):
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def litarray_list(self):
            return self.getTypedRuleContext(CSlangParser.Litarray_listContext,0)


        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = CSlangParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(CSlangParser.LSB)
            self.state = 584
            self.litarray_list()
            self.state = 585
            self.match(CSlangParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Litarray_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_array(self):
            return self.getTypedRuleContext(CSlangParser.Literal_arrayContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def litarray_list(self):
            return self.getTypedRuleContext(CSlangParser.Litarray_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_litarray_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitarray_list" ):
                return visitor.visitLitarray_list(self)
            else:
                return visitor.visitChildren(self)




    def litarray_list(self):

        localctx = CSlangParser.Litarray_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_litarray_list)
        try:
            self.state = 592
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 587
                self.literal_array()
                self.state = 588
                self.match(CSlangParser.COMMA)
                self.state = 589
                self.litarray_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 591
                self.literal_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def exp_list(self):
            return self.getTypedRuleContext(CSlangParser.Exp_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = CSlangParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_exp_list)
        try:
            self.state = 599
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 594
                self.expr()
                self.state = 595
                self.match(CSlangParser.COMMA)
                self.state = 596
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 598
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = CSlangParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.match(CSlangParser.LSB)
            self.state = 602
            self.expr()
            self.state = 603
            self.match(CSlangParser.RSB)
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

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_name" ):
                return visitor.visitAttribute_name(self)
            else:
                return visitor.visitChildren(self)




    def attribute_name(self):

        localctx = CSlangParser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_attribute_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
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


    class Identifier_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def STATIC_ID(self):
            return self.getToken(CSlangParser.STATIC_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_identifier_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_name" ):
                return visitor.visitIdentifier_name(self)
            else:
                return visitor.visitChildren(self)




    def identifier_name(self):

        localctx = CSlangParser.Identifier_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_identifier_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.STATIC_ID):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[48] = self.pre_exp_sempred
        self._predicates[51] = self.expr2_sempred
        self._predicates[52] = self.expr3_sempred
        self._predicates[53] = self.expr4_sempred
        self._predicates[56] = self.expr7_sempred
        self._predicates[57] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def pre_exp_sempred(self, localctx:Pre_expContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         





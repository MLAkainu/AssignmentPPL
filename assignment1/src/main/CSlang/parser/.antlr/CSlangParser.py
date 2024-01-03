# Generated from d://Assignment//assignment1//src//main//CSlang//parser//CSlang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,62,610,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,152,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,4,1,4,1,4,3,4,166,8,4,1,5,1,5,3,5,170,8,5,1,6,1,6,1,6,
        1,6,3,6,176,8,6,1,7,1,7,1,7,3,7,181,8,7,1,8,1,8,3,8,185,8,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,198,8,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,3,12,216,8,12,1,13,1,13,1,13,3,13,221,8,13,1,14,1,14,1,
        15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,3,17,234,8,17,1,18,1,
        18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,3,20,249,
        8,20,1,21,1,21,1,21,1,21,1,21,3,21,256,8,21,1,22,1,22,1,22,1,22,
        1,23,1,23,1,23,1,23,3,23,266,8,23,1,24,1,24,1,24,3,24,271,8,24,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,3,
        27,286,8,27,1,28,1,28,1,28,1,28,3,28,292,8,28,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,3,29,303,8,29,1,30,1,30,1,30,3,30,308,8,
        30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,3,32,320,8,
        32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,
        33,334,8,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,355,8,35,1,36,1,
        36,1,36,1,36,1,36,1,37,1,37,3,37,364,8,37,1,37,1,37,1,37,1,37,3,
        37,370,8,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,
        39,1,39,1,40,1,40,1,40,1,41,1,41,1,41,1,42,1,42,3,42,392,8,42,1,
        42,1,42,1,43,1,43,1,43,1,44,1,44,3,44,401,8,44,1,45,1,45,1,45,1,
        45,3,45,407,8,45,1,45,1,45,1,46,1,46,1,46,3,46,414,8,46,1,47,1,47,
        1,47,1,47,1,47,3,47,421,8,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,
        1,48,1,48,1,48,1,48,1,48,1,48,3,48,436,8,48,1,48,5,48,439,8,48,10,
        48,12,48,442,9,48,1,49,1,49,1,49,1,49,1,49,3,49,449,8,49,1,50,1,
        50,1,50,1,50,1,50,3,50,456,8,50,1,51,1,51,1,51,1,51,1,51,1,51,5,
        51,464,8,51,10,51,12,51,467,9,51,1,52,1,52,1,52,1,52,1,52,1,52,5,
        52,475,8,52,10,52,12,52,478,9,52,1,53,1,53,1,53,1,53,1,53,1,53,5,
        53,486,8,53,10,53,12,53,489,9,53,1,54,1,54,1,54,3,54,494,8,54,1,
        55,1,55,1,55,3,55,499,8,55,1,56,1,56,1,56,1,56,1,56,5,56,506,8,56,
        10,56,12,56,509,9,56,1,57,1,57,1,57,1,57,1,57,1,57,1,57,3,57,518,
        8,57,5,57,520,8,57,10,57,12,57,523,9,57,1,58,1,58,1,58,3,58,528,
        8,58,1,58,3,58,531,8,58,1,59,1,59,1,59,1,59,3,59,537,8,59,1,59,1,
        59,3,59,541,8,59,1,60,1,60,1,60,3,60,546,8,60,1,60,1,60,1,61,1,61,
        1,61,3,61,553,8,61,1,61,1,61,1,62,1,62,1,62,1,62,1,62,1,62,1,62,
        1,62,3,62,565,8,62,1,63,1,63,1,63,1,63,1,63,1,63,3,63,573,8,63,1,
        64,1,64,1,64,1,64,1,64,3,64,580,8,64,1,65,1,65,1,66,1,66,1,66,1,
        66,1,67,1,67,1,67,1,67,1,67,3,67,593,8,67,1,68,1,68,1,68,1,68,1,
        68,3,68,600,8,68,1,69,1,69,1,69,1,69,1,70,1,70,1,71,1,71,1,71,0,
        6,96,102,104,106,112,114,72,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,
        112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,
        0,10,1,0,8,11,2,0,8,11,19,19,2,0,17,17,58,58,2,0,24,24,26,30,1,0,
        22,23,1,0,32,33,2,0,34,36,40,40,1,0,6,7,2,0,16,16,20,20,1,0,58,59,
        612,0,144,1,0,0,0,2,151,1,0,0,0,4,153,1,0,0,0,6,160,1,0,0,0,8,165,
        1,0,0,0,10,169,1,0,0,0,12,175,1,0,0,0,14,180,1,0,0,0,16,184,1,0,
        0,0,18,186,1,0,0,0,20,197,1,0,0,0,22,199,1,0,0,0,24,215,1,0,0,0,
        26,220,1,0,0,0,28,222,1,0,0,0,30,224,1,0,0,0,32,226,1,0,0,0,34,233,
        1,0,0,0,36,235,1,0,0,0,38,237,1,0,0,0,40,248,1,0,0,0,42,255,1,0,
        0,0,44,257,1,0,0,0,46,265,1,0,0,0,48,270,1,0,0,0,50,272,1,0,0,0,
        52,279,1,0,0,0,54,285,1,0,0,0,56,291,1,0,0,0,58,302,1,0,0,0,60,304,
        1,0,0,0,62,311,1,0,0,0,64,319,1,0,0,0,66,333,1,0,0,0,68,335,1,0,
        0,0,70,354,1,0,0,0,72,356,1,0,0,0,74,361,1,0,0,0,76,371,1,0,0,0,
        78,375,1,0,0,0,80,383,1,0,0,0,82,386,1,0,0,0,84,389,1,0,0,0,86,395,
        1,0,0,0,88,400,1,0,0,0,90,402,1,0,0,0,92,413,1,0,0,0,94,415,1,0,
        0,0,96,424,1,0,0,0,98,448,1,0,0,0,100,455,1,0,0,0,102,457,1,0,0,
        0,104,468,1,0,0,0,106,479,1,0,0,0,108,493,1,0,0,0,110,498,1,0,0,
        0,112,500,1,0,0,0,114,510,1,0,0,0,116,530,1,0,0,0,118,540,1,0,0,
        0,120,542,1,0,0,0,122,549,1,0,0,0,124,564,1,0,0,0,126,572,1,0,0,
        0,128,579,1,0,0,0,130,581,1,0,0,0,132,583,1,0,0,0,134,592,1,0,0,
        0,136,599,1,0,0,0,138,601,1,0,0,0,140,605,1,0,0,0,142,607,1,0,0,
        0,144,145,3,2,1,0,145,146,5,0,0,1,146,1,1,0,0,0,147,148,3,4,2,0,
        148,149,3,2,1,0,149,152,1,0,0,0,150,152,3,4,2,0,151,147,1,0,0,0,
        151,150,1,0,0,0,152,3,1,0,0,0,153,154,5,14,0,0,154,155,3,6,3,0,155,
        156,3,8,4,0,156,157,5,49,0,0,157,158,3,10,5,0,158,159,5,50,0,0,159,
        5,1,0,0,0,160,161,5,58,0,0,161,7,1,0,0,0,162,163,5,31,0,0,163,166,
        5,58,0,0,164,166,1,0,0,0,165,162,1,0,0,0,165,164,1,0,0,0,166,9,1,
        0,0,0,167,170,3,12,6,0,168,170,1,0,0,0,169,167,1,0,0,0,169,168,1,
        0,0,0,170,11,1,0,0,0,171,172,3,14,7,0,172,173,3,12,6,0,173,176,1,
        0,0,0,174,176,3,14,7,0,175,171,1,0,0,0,175,174,1,0,0,0,176,13,1,
        0,0,0,177,181,3,16,8,0,178,181,3,38,19,0,179,181,3,50,25,0,180,177,
        1,0,0,0,180,178,1,0,0,0,180,179,1,0,0,0,181,15,1,0,0,0,182,185,3,
        18,9,0,183,185,3,22,11,0,184,182,1,0,0,0,184,183,1,0,0,0,185,17,
        1,0,0,0,186,187,3,140,70,0,187,188,3,20,10,0,188,189,5,43,0,0,189,
        190,3,26,13,0,190,191,5,42,0,0,191,19,1,0,0,0,192,193,3,142,71,0,
        193,194,5,41,0,0,194,195,3,20,10,0,195,198,1,0,0,0,196,198,3,142,
        71,0,197,192,1,0,0,0,197,196,1,0,0,0,198,21,1,0,0,0,199,200,3,140,
        70,0,200,201,3,142,71,0,201,202,3,24,12,0,202,203,3,98,49,0,203,
        204,5,42,0,0,204,23,1,0,0,0,205,206,5,41,0,0,206,207,3,142,71,0,
        207,208,3,24,12,0,208,209,3,98,49,0,209,210,5,41,0,0,210,216,1,0,
        0,0,211,212,5,43,0,0,212,213,3,26,13,0,213,214,5,38,0,0,214,216,
        1,0,0,0,215,205,1,0,0,0,215,211,1,0,0,0,216,25,1,0,0,0,217,221,3,
        28,14,0,218,221,3,32,16,0,219,221,3,36,18,0,220,217,1,0,0,0,220,
        218,1,0,0,0,220,219,1,0,0,0,221,27,1,0,0,0,222,223,7,0,0,0,223,29,
        1,0,0,0,224,225,7,1,0,0,225,31,1,0,0,0,226,227,5,47,0,0,227,228,
        5,54,0,0,228,229,5,48,0,0,229,230,3,34,17,0,230,33,1,0,0,0,231,234,
        3,28,14,0,232,234,3,36,18,0,233,231,1,0,0,0,233,232,1,0,0,0,234,
        35,1,0,0,0,235,236,5,58,0,0,236,37,1,0,0,0,237,238,5,21,0,0,238,
        239,3,142,71,0,239,240,5,45,0,0,240,241,3,40,20,0,241,242,5,46,0,
        0,242,243,5,43,0,0,243,244,3,48,24,0,244,245,3,52,26,0,245,39,1,
        0,0,0,246,249,3,42,21,0,247,249,1,0,0,0,248,246,1,0,0,0,248,247,
        1,0,0,0,249,41,1,0,0,0,250,251,3,44,22,0,251,252,5,41,0,0,252,253,
        3,42,21,0,253,256,1,0,0,0,254,256,3,44,22,0,255,250,1,0,0,0,255,
        254,1,0,0,0,256,43,1,0,0,0,257,258,3,46,23,0,258,259,5,43,0,0,259,
        260,3,26,13,0,260,45,1,0,0,0,261,262,5,58,0,0,262,263,5,41,0,0,263,
        266,3,46,23,0,264,266,5,58,0,0,265,261,1,0,0,0,265,264,1,0,0,0,266,
        47,1,0,0,0,267,271,3,30,15,0,268,271,3,32,16,0,269,271,3,36,18,0,
        270,267,1,0,0,0,270,268,1,0,0,0,270,269,1,0,0,0,271,49,1,0,0,0,272,
        273,5,21,0,0,273,274,5,15,0,0,274,275,5,45,0,0,275,276,3,40,20,0,
        276,277,5,46,0,0,277,278,3,52,26,0,278,51,1,0,0,0,279,280,5,49,0,
        0,280,281,3,54,27,0,281,282,5,50,0,0,282,53,1,0,0,0,283,286,3,56,
        28,0,284,286,1,0,0,0,285,283,1,0,0,0,285,284,1,0,0,0,286,55,1,0,
        0,0,287,288,3,58,29,0,288,289,3,56,28,0,289,292,1,0,0,0,290,292,
        3,58,29,0,291,287,1,0,0,0,291,290,1,0,0,0,292,57,1,0,0,0,293,303,
        3,60,30,0,294,303,3,68,34,0,295,303,3,74,37,0,296,303,3,78,39,0,
        297,303,3,80,40,0,298,303,3,82,41,0,299,303,3,84,42,0,300,303,3,
        86,43,0,301,303,3,52,26,0,302,293,1,0,0,0,302,294,1,0,0,0,302,295,
        1,0,0,0,302,296,1,0,0,0,302,297,1,0,0,0,302,298,1,0,0,0,302,299,
        1,0,0,0,302,300,1,0,0,0,302,301,1,0,0,0,303,59,1,0,0,0,304,307,3,
        140,70,0,305,308,3,62,31,0,306,308,3,66,33,0,307,305,1,0,0,0,307,
        306,1,0,0,0,308,309,1,0,0,0,309,310,5,42,0,0,310,61,1,0,0,0,311,
        312,3,64,32,0,312,313,5,43,0,0,313,314,3,26,13,0,314,63,1,0,0,0,
        315,316,5,58,0,0,316,317,5,41,0,0,317,320,3,64,32,0,318,320,5,58,
        0,0,319,315,1,0,0,0,319,318,1,0,0,0,320,65,1,0,0,0,321,322,5,58,
        0,0,322,323,5,41,0,0,323,324,3,66,33,0,324,325,5,41,0,0,325,326,
        3,98,49,0,326,334,1,0,0,0,327,328,5,58,0,0,328,329,5,43,0,0,329,
        330,3,26,13,0,330,331,5,38,0,0,331,332,3,98,49,0,332,334,1,0,0,0,
        333,321,1,0,0,0,333,327,1,0,0,0,334,67,1,0,0,0,335,336,3,70,35,0,
        336,337,5,25,0,0,337,338,3,98,49,0,338,339,5,42,0,0,339,69,1,0,0,
        0,340,355,5,58,0,0,341,342,3,92,46,0,342,343,5,59,0,0,343,355,1,
        0,0,0,344,345,3,114,57,0,345,346,5,44,0,0,346,347,5,58,0,0,347,355,
        1,0,0,0,348,349,3,114,57,0,349,350,3,138,69,0,350,351,5,44,0,0,351,
        352,5,58,0,0,352,355,1,0,0,0,353,355,3,72,36,0,354,340,1,0,0,0,354,
        341,1,0,0,0,354,344,1,0,0,0,354,348,1,0,0,0,354,353,1,0,0,0,355,
        71,1,0,0,0,356,357,3,112,56,0,357,358,5,47,0,0,358,359,3,98,49,0,
        359,360,5,48,0,0,360,73,1,0,0,0,361,363,5,3,0,0,362,364,3,52,26,
        0,363,362,1,0,0,0,363,364,1,0,0,0,364,365,1,0,0,0,365,366,3,98,49,
        0,366,369,3,52,26,0,367,368,5,4,0,0,368,370,3,52,26,0,369,367,1,
        0,0,0,369,370,1,0,0,0,370,75,1,0,0,0,371,372,3,70,35,0,372,373,5,
        25,0,0,373,374,3,98,49,0,374,77,1,0,0,0,375,376,5,5,0,0,376,377,
        3,76,38,0,377,378,5,42,0,0,378,379,3,98,49,0,379,380,5,42,0,0,380,
        381,3,76,38,0,381,382,3,52,26,0,382,79,1,0,0,0,383,384,5,1,0,0,384,
        385,5,42,0,0,385,81,1,0,0,0,386,387,5,2,0,0,387,388,5,42,0,0,388,
        83,1,0,0,0,389,391,5,12,0,0,390,392,3,98,49,0,391,390,1,0,0,0,391,
        392,1,0,0,0,392,393,1,0,0,0,393,394,5,42,0,0,394,85,1,0,0,0,395,
        396,3,88,44,0,396,397,5,42,0,0,397,87,1,0,0,0,398,401,3,90,45,0,
        399,401,3,94,47,0,400,398,1,0,0,0,400,399,1,0,0,0,401,89,1,0,0,0,
        402,403,3,92,46,0,403,404,5,59,0,0,404,406,5,45,0,0,405,407,3,136,
        68,0,406,405,1,0,0,0,406,407,1,0,0,0,407,408,1,0,0,0,408,409,5,46,
        0,0,409,91,1,0,0,0,410,411,7,2,0,0,411,414,5,44,0,0,412,414,1,0,
        0,0,413,410,1,0,0,0,413,412,1,0,0,0,414,93,1,0,0,0,415,416,3,96,
        48,0,416,417,5,44,0,0,417,418,5,58,0,0,418,420,5,45,0,0,419,421,
        3,136,68,0,420,419,1,0,0,0,420,421,1,0,0,0,421,422,1,0,0,0,422,423,
        5,46,0,0,423,95,1,0,0,0,424,425,6,48,-1,0,425,426,3,116,58,0,426,
        440,1,0,0,0,427,428,10,3,0,0,428,429,5,44,0,0,429,439,5,58,0,0,430,
        431,10,2,0,0,431,432,5,44,0,0,432,433,5,58,0,0,433,435,5,45,0,0,
        434,436,3,136,68,0,435,434,1,0,0,0,435,436,1,0,0,0,436,437,1,0,0,
        0,437,439,5,46,0,0,438,427,1,0,0,0,438,430,1,0,0,0,439,442,1,0,0,
        0,440,438,1,0,0,0,440,441,1,0,0,0,441,97,1,0,0,0,442,440,1,0,0,0,
        443,444,3,100,50,0,444,445,5,39,0,0,445,446,3,100,50,0,446,449,1,
        0,0,0,447,449,3,100,50,0,448,443,1,0,0,0,448,447,1,0,0,0,449,99,
        1,0,0,0,450,451,3,102,51,0,451,452,7,3,0,0,452,453,3,102,51,0,453,
        456,1,0,0,0,454,456,3,102,51,0,455,450,1,0,0,0,455,454,1,0,0,0,456,
        101,1,0,0,0,457,458,6,51,-1,0,458,459,3,104,52,0,459,465,1,0,0,0,
        460,461,10,2,0,0,461,462,7,4,0,0,462,464,3,104,52,0,463,460,1,0,
        0,0,464,467,1,0,0,0,465,463,1,0,0,0,465,466,1,0,0,0,466,103,1,0,
        0,0,467,465,1,0,0,0,468,469,6,52,-1,0,469,470,3,106,53,0,470,476,
        1,0,0,0,471,472,10,2,0,0,472,473,7,5,0,0,473,475,3,106,53,0,474,
        471,1,0,0,0,475,478,1,0,0,0,476,474,1,0,0,0,476,477,1,0,0,0,477,
        105,1,0,0,0,478,476,1,0,0,0,479,480,6,53,-1,0,480,481,3,108,54,0,
        481,487,1,0,0,0,482,483,10,2,0,0,483,484,7,6,0,0,484,486,3,108,54,
        0,485,482,1,0,0,0,486,489,1,0,0,0,487,485,1,0,0,0,487,488,1,0,0,
        0,488,107,1,0,0,0,489,487,1,0,0,0,490,491,5,37,0,0,491,494,3,108,
        54,0,492,494,3,110,55,0,493,490,1,0,0,0,493,492,1,0,0,0,494,109,
        1,0,0,0,495,496,5,33,0,0,496,499,3,110,55,0,497,499,3,112,56,0,498,
        495,1,0,0,0,498,497,1,0,0,0,499,111,1,0,0,0,500,501,6,56,-1,0,501,
        502,3,114,57,0,502,507,1,0,0,0,503,504,10,2,0,0,504,506,3,138,69,
        0,505,503,1,0,0,0,506,509,1,0,0,0,507,505,1,0,0,0,507,508,1,0,0,
        0,508,113,1,0,0,0,509,507,1,0,0,0,510,511,6,57,-1,0,511,512,3,116,
        58,0,512,521,1,0,0,0,513,514,10,2,0,0,514,517,5,44,0,0,515,518,5,
        58,0,0,516,518,3,120,60,0,517,515,1,0,0,0,517,516,1,0,0,0,518,520,
        1,0,0,0,519,513,1,0,0,0,520,523,1,0,0,0,521,519,1,0,0,0,521,522,
        1,0,0,0,522,115,1,0,0,0,523,521,1,0,0,0,524,527,3,92,46,0,525,528,
        5,59,0,0,526,528,3,122,61,0,527,525,1,0,0,0,527,526,1,0,0,0,528,
        531,1,0,0,0,529,531,3,118,59,0,530,524,1,0,0,0,530,529,1,0,0,0,531,
        117,1,0,0,0,532,533,5,18,0,0,533,534,5,58,0,0,534,536,5,45,0,0,535,
        537,3,136,68,0,536,535,1,0,0,0,536,537,1,0,0,0,537,538,1,0,0,0,538,
        541,5,46,0,0,539,541,3,124,62,0,540,532,1,0,0,0,540,539,1,0,0,0,
        541,119,1,0,0,0,542,543,5,58,0,0,543,545,5,45,0,0,544,546,3,136,
        68,0,545,544,1,0,0,0,545,546,1,0,0,0,546,547,1,0,0,0,547,548,5,46,
        0,0,548,121,1,0,0,0,549,550,5,59,0,0,550,552,5,45,0,0,551,553,3,
        136,68,0,552,551,1,0,0,0,552,553,1,0,0,0,553,554,1,0,0,0,554,555,
        5,46,0,0,555,123,1,0,0,0,556,565,5,58,0,0,557,558,5,45,0,0,558,559,
        3,98,49,0,559,560,5,46,0,0,560,565,1,0,0,0,561,565,3,126,63,0,562,
        565,5,17,0,0,563,565,5,13,0,0,564,556,1,0,0,0,564,557,1,0,0,0,564,
        561,1,0,0,0,564,562,1,0,0,0,564,563,1,0,0,0,565,125,1,0,0,0,566,
        573,5,54,0,0,567,573,5,55,0,0,568,573,5,56,0,0,569,573,5,57,0,0,
        570,573,3,130,65,0,571,573,3,132,66,0,572,566,1,0,0,0,572,567,1,
        0,0,0,572,568,1,0,0,0,572,569,1,0,0,0,572,570,1,0,0,0,572,571,1,
        0,0,0,573,127,1,0,0,0,574,580,5,54,0,0,575,580,5,55,0,0,576,580,
        5,56,0,0,577,580,5,57,0,0,578,580,3,130,65,0,579,574,1,0,0,0,579,
        575,1,0,0,0,579,576,1,0,0,0,579,577,1,0,0,0,579,578,1,0,0,0,580,
        129,1,0,0,0,581,582,7,7,0,0,582,131,1,0,0,0,583,584,5,47,0,0,584,
        585,3,134,67,0,585,586,5,48,0,0,586,133,1,0,0,0,587,588,3,128,64,
        0,588,589,5,41,0,0,589,590,3,134,67,0,590,593,1,0,0,0,591,593,3,
        128,64,0,592,587,1,0,0,0,592,591,1,0,0,0,593,135,1,0,0,0,594,595,
        3,98,49,0,595,596,5,41,0,0,596,597,3,136,68,0,597,600,1,0,0,0,598,
        600,3,98,49,0,599,594,1,0,0,0,599,598,1,0,0,0,600,137,1,0,0,0,601,
        602,5,47,0,0,602,603,3,98,49,0,603,604,5,48,0,0,604,139,1,0,0,0,
        605,606,7,8,0,0,606,141,1,0,0,0,607,608,7,9,0,0,608,143,1,0,0,0,
        52,151,165,169,175,180,184,197,215,220,233,248,255,265,270,285,291,
        302,307,319,333,354,363,369,391,400,406,413,420,435,438,440,448,
        455,465,476,487,493,498,507,517,521,527,530,536,540,545,552,564,
        572,579,592,599
    ]

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
        self.checkVersion("4.13.1")
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




    def name_superclass(self):

        localctx = CSlangParser.Name_superclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_name_superclass)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(CSlangParser.SUPERCLASS)
                self.state = 163
                self.match(CSlangParser.ID)
                pass
            elif token in [49]:
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




    def body_class_list(self):

        localctx = CSlangParser.Body_class_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_body_class_list)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 20, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.body_class_prime()
                pass
            elif token in [50]:
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




    def varlist(self):

        localctx = CSlangParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varlist)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
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
            elif token in [43]:
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




    def type_att(self):

        localctx = CSlangParser.Type_attContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type_att)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.primitive_type()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.array_type()
                pass
            elif token in [58]:
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




    def primitive_type(self):

        localctx = CSlangParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
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




    def primitive_type_(self):

        localctx = CSlangParser.Primitive_type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_primitive_type_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528128) != 0)):
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




    def element_type(self):

        localctx = CSlangParser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_element_type)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.primitive_type()
                pass
            elif token in [58]:
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




    def paramlist(self):

        localctx = CSlangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_paramlist)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.paramprime()
                pass
            elif token in [46]:
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




    def type_return(self):

        localctx = CSlangParser.Type_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_type_return)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.primitive_type_()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.array_type()
                pass
            elif token in [58]:
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




    def stmtlist(self):

        localctx = CSlangParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmtlist)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 5, 6, 7, 12, 13, 16, 17, 18, 20, 45, 47, 49, 54, 55, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.stmtprime()
                pass
            elif token in [50]:
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
            if _la==49:
                self.state = 362
                self.blockstmt()


            self.state = 365
            self.expr()
            self.state = 366
            self.blockstmt()
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135083173987098816) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135083173987098816) != 0):
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




    def name_class_access(self):

        localctx = CSlangParser.Name_class_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_name_class_access)
        self._la = 0 # Token type
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                _la = self._input.LA(1)
                if not(_la==17 or _la==58):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 411
                self.match(CSlangParser.DOT)
                pass
            elif token in [59]:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135083173987098816) != 0):
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
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135083173987098816) != 0):
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
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2097152000) != 0)):
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
                    if not(_la==22 or _la==23):
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
                    if not(_la==32 or _la==33):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1219770712064) != 0)):
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




    def expr5(self):

        localctx = CSlangParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_expr5)
        try:
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.match(CSlangParser.NOT)
                self.state = 491
                self.expr5()
                pass
            elif token in [6, 7, 13, 17, 18, 33, 45, 47, 54, 55, 56, 57, 58, 59]:
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




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expr6)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(CSlangParser.SUB)
                self.state = 496
                self.expr6()
                pass
            elif token in [6, 7, 13, 17, 18, 45, 47, 54, 55, 56, 57, 58, 59]:
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




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135083173987098816) != 0):
                    self.state = 535
                    self.exp_list()


                self.state = 538
                self.match(CSlangParser.RP)
                pass
            elif token in [6, 7, 13, 17, 45, 47, 54, 55, 56, 57, 58]:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135083173987098816) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135083173987098816) != 0):
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




    def operands(self):

        localctx = CSlangParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_operands)
        try:
            self.state = 564
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.match(CSlangParser.ID)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
                self.match(CSlangParser.LP)
                self.state = 558
                self.expr()
                self.state = 559
                self.match(CSlangParser.RP)
                pass
            elif token in [6, 7, 47, 54, 55, 56, 57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 561
                self.literals()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 562
                self.match(CSlangParser.SELF)
                pass
            elif token in [13]:
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




    def literals(self):

        localctx = CSlangParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_literals)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.match(CSlangParser.INTARR)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 3)
                self.state = 568
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 4)
                self.state = 569
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 570
                self.boolean_literal()
                pass
            elif token in [47]:
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




    def literal_array(self):

        localctx = CSlangParser.Literal_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_literal_array)
        try:
            self.state = 579
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self.match(CSlangParser.INTARR)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 575
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 3)
                self.state = 576
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 4)
                self.state = 577
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [6, 7]:
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




    def boolean_literal(self):

        localctx = CSlangParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
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




    def attribute_name(self):

        localctx = CSlangParser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_attribute_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            _la = self._input.LA(1)
            if not(_la==16 or _la==20):
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




    def identifier_name(self):

        localctx = CSlangParser.Identifier_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_identifier_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            _la = self._input.LA(1)
            if not(_la==58 or _la==59):
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
         





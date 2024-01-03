// ID : 2110342
// Name: Nguyen Minh Loc
grammar CSlang;

@lexer::header {
from lexererr import *
 # 2110342 - Nguyen Minh Loc
}

options{
	language=Python3;
}

program: class_declarelist EOF ;


class_declarelist: class_declare class_declarelist | class_declare;
class_declare: CLASS name_class name_superclass LB body_class_list RB;
name_class: ID;
name_superclass: SUPERCLASS ID | ;
body_class_list: body_class_prime | ;
body_class_prime: body_class body_class_prime | body_class;

body_class: attribute_declare| method_declare| constructor_declare;


attribute_declare: attdecl_ | attdecl ;
attdecl_: attribute_name indenlist COLON type_att SEMI;
indenlist: identifier_name COMMA indenlist | identifier_name;

attdecl: attribute_name identifier_name varlist expr SEMI;
varlist: COMMA identifier_name varlist expr COMMA
	| COLON type_att EQ ;

type_att: primitive_type | array_type | class_type;
primitive_type: INT | FLOAT | BOOL | STRING ;
primitive_type_ : INT | FLOAT | BOOL | STRING | VOID;
array_type: LSB INTARR RSB element_type;

element_type: primitive_type | class_type;
class_type: ID;

method_declare: FUNC identifier_name LP paramlist RP COLON type_return blockstmt;

paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: idlist COLON type_att;
idlist: ID COMMA idlist | ID;

type_return: primitive_type_ | array_type | class_type;	

constructor_declare: FUNC CONSTRUCTOR LP paramlist RP blockstmt;


blockstmt: LB stmtlist RB;

stmtlist: stmtprime | ;
stmtprime: stmt stmtprime | stmt;

stmt: var_and_const_declstmt
	| assignment_stmt
	| if_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| method_invocation_stmt
	| blockstmt ;

var_and_const_declstmt: attribute_name  (varstmt_decl | varstmt_declass)  SEMI;
varstmt_decl: variable_namelist COLON type_att ;
variable_namelist:  ID COMMA  variable_namelist | ID;


varstmt_declass: ID COMMA varstmt_declass COMMA expr
				| ID COLON type_att EQ expr ;


assignment_stmt:  assign_lhs ASSIGN expr SEMI;
assign_lhs: ID //bien thuong
			|  name_class_access STATIC_ID 		// bien static	
			| expr8 DOT ID
			| expr8 index_operator DOT ID
			| index_exp_for_scalar_variable ;

index_exp_for_scalar_variable:  expr7 LSB expr RSB;


if_stmt: IF blockstmt? expr blockstmt (ELSE blockstmt)?;

assignstmt: assign_lhs ASSIGN expr ;


for_stmt: FOR assignstmt SEMI expr SEMI assignstmt blockstmt;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN expr? SEMI;

method_invocation_stmt: method_invocation SEMI ;

method_invocation: static_method_invocation
					| instance_method_invocation;

static_method_invocation: name_class_access STATIC_ID LP exp_list? RP;

name_class_access: (SELF | ID) DOT | ;

instance_method_invocation: pre_exp DOT ID LP exp_list? RP;

pre_exp: pre_exp DOT ID
		| pre_exp DOT ID LP exp_list? RP
		|expr9 ;

expr: expr1 STRING_CONCAT expr1 | expr1;
expr1: expr2 (EQUAL | NOT_EQUAL | LESS_THAN_EQUAL |  GREATER_THAN_EQUAL | LESS_THAN | GREATER_THAN) expr2 | expr2;
expr2: expr2 (AND | OR ) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;	
expr4: expr4 (MUL | DIV_FLOAT | DIV_INT | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: expr7 index_operator | expr8;
expr8: expr8  DOT (ID | funcall)
	  | expr9;

expr9:  name_class_access (STATIC_ID | static_funcall)  
		| expr10;

expr10: NEW ID LP exp_list? RP
		| operands ;

funcall: ID LP exp_list? RP;
static_funcall: STATIC_ID LP exp_list? RP;

operands: ID | LP expr RP | literals | SELF | NULL ;
literals: INTARR | INTLIT | FLOATLIT | STRINGLIT | boolean_literal | array_literal;

literal_array: INTARR | INTLIT | FLOATLIT | STRINGLIT | boolean_literal ;


boolean_literal: TRUE | FALSE;
array_literal: LSB litarray_list RSB;

litarray_list: literal_array COMMA litarray_list | literal_array;

exp_list: expr COMMA exp_list | expr;

index_operator:  LSB expr RSB ; 

attribute_name: VAR | CONST;
identifier_name: ID | STATIC_ID;

// 3.4 KEYWORDS
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
FOR: 'for';
TRUE: 'true';
FALSE: 'false';
INT: 'int';
FLOAT: 'float';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
NULL: 'null';
CLASS: 'class';	
CONSTRUCTOR: 'constructor';
VAR: 'var';
SELF: 'self';
NEW: 'new';
VOID: 'void';
CONST: 'const';
FUNC: 'func';

// 3.5 OPERATORS
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: ':=';
NOT_EQUAL: '!=';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_EQUAL: '<=';
GREATER_THAN_EQUAL: '>=';
SUPERCLASS: '<-';

ADD: '+';
SUB: '-';
MUL: '*';
DIV_FLOAT: '/';
DIV_INT: '\\';
NOT: '!';
EQ: '=';
STRING_CONCAT: '^';
MOD: '%';


// 3.6 SEPARATORS
COMMA: ',';
SEMI: ';';
COLON: ':';
DOT: '.';
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
LB : '{';
RB : '}';

// 3.2 COMMENTS

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


// 3.7 LITERALS
INTARR:  [1-9][0-9]*;
INTLIT: INTPART;

FLOATLIT: INTPART DECPART  EXPPART? | INTPART DECPART? EXPPART ;
STRINGLIT: '"' CHAR* '"'
{
	self.text = self.text[1:-1]
};

fragment INTPART: '0' | [1-9][0-9]*;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: ('e' | 'E') ('+' | '-')? [0-9]+;

fragment CHAR: ~["\\\r\n] | ESCAPE;
fragment ESCAPE: '\\' [btnfr"\\];


// 3.3 IDENTIFIERS

ID: (LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT)*;
STATIC_ID: AT [a-zA-Z0-9_]+;

fragment UPPER: [A-Z];
fragment LOWER: [a-z];
fragment DIGIT: [0-9];
fragment UNDERSCORE: '_';
fragment LETTER: UPPER | LOWER;
fragment AT : '@';

ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' CHAR* EOF? 
{
	y = str(self.text)
	raise UncloseString(y[1:])
};

ILLEGAL_ESCAPE: '"' CHAR* ( '\\' ~[bnfrt"\\] )  
{
	raise IllegalEscape(self.text[1:])
};



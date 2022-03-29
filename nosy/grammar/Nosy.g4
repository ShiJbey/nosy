grammar Nosy;

// For now, let the entry be the same as a single query we may change this in the future
prog: query;

query: '[' find_spec where_clauses? ']';

find_spec: ':find' find_rel;

find_rel: find_elem+;

find_elem: variable;

aggregate: '[' aggregate_fn_name fn_arg+ ']';

aggregate_fn_name: SYMBOL ('_' SYMBOL)*;

fn_arg: variable | constant;

variable: '?' SYMBOL;

where_clauses: ':where' clause+;

and_clause: '[' 'and' clause+ ']';

not_clause: '[' 'not' clause+ ']';

not_join_clause: '[' 'not-join' '[' variable+ ']' clause+ ']';

or_clause: '[' 'or' clause+ ']';

or_join_clause:
	'[' 'or-join' '[' variable+ ']' (clause | and_clause)+ ']';

expression_clause: data_pattern | pred_expr | fn_expr;

clause:
	not_clause
	| not_join_clause
	| or_clause
	| or_join_clause
	| expression_clause;

data_pattern:
	'[' (variable | constant | '_') attribute_name (
		variable
		| constant
		| '_'
	) ']';

attribute_name:
	':' (SYMBOL ('_' SYMBOL)*) ('/' SYMBOL ('_' SYMBOL)*)*;

constant: BOOLEAN | NUMBER | STRING;

pred_expr: '[' '(' pred fn_arg+ ')' ']';

pred: (SYMBOL ('_' SYMBOL)*) | range_predicate;

range_predicate: '=' | '!=' | '<=' | '<' | '>' | '>=';

fn_expr: '[' '(' fn fn_arg+ ')' binding ']';

fn: SYMBOL ('_' SYMBOL)*;

binding: bind_scalar | bind_tuple;

bind_scalar: variable;

bind_tuple: '[' (variable | '_')+ ']';

NUMBER: INT | INT '.' [0-9]* [1-9];

INT: '0' | '-'? [1-9][0-9]*;

BOOLEAN: 'True' | 'False';

STRING: '"' ([ -~])* '"';

SYMBOL: [a-zA-Z]+;

WS: [ \t\r\n]+ -> skip;

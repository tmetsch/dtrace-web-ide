editAreaLoader.load_syntax["dtrace"] = {
	'DISPLAY_NAME' : 'DTrace'
	,'COMMENT_MULTI' : {'/*' : '*/'}
	,'QUOTEMARKS' : {1: "'", 2: '"'}
	,'KEYWORD_CASE_SENSITIVE' : true
	,'KEYWORDS' : {
		'vars' : [
			'self', 'this'
		]
		,'functions' : [
			'trace', 'printf', 'copyinstr'
		]
		,'aggfunctions' : [
			'count', 'sum', 'min', 'max', 'lquantize', 'quantize'
		]
 		,'buildinvars' : [
			'args', 'pid', 'arg0', 'arg1', 'arg2', 'execname'
		]
		,'probes' : [
		    'syscall'
		]
	}
	,'OPERATORS' :[
		'+', '-', '/', '*', '=', '<', '>', '%', '!', '?', ':', '&'
	]
	,'DELIMITERS' :[
		'(', ')', '[', ']', '{', '}'
	]
	,'REGEXPS' : {
		'precompiler' : {
			'search' : '()(#[^\r\n]*)()'
			,'class' : 'precompiler'
			,'modifiers' : 'g'
			,'execute' : 'before'
		}
	}
	,'STYLES' : {
		'COMMENTS': 'color: #7bc04a;'
		,'QUOTESMARKS': 'color: #6381F8;'
		,'KEYWORDS' : {
			'vars' : 'color: #e00b00;'
			,'functions' : 'color: #ffb400;'
			,'aggfunctions' : 'color: #ffb400; font-weight: bold;'
			,'buildinvars' : 'color: #48BDDF;'
			,'probes' : 'color: #d00;'
		}
		,'OPERATORS' : 'color: #FF00FF;'
		,'DELIMITERS' : 'color: #0038E1;'
		,'REGEXPS' : {
			'precompiler' : 'color: #009900;'
			,'precompilerstring' : 'color: #994400;'
		}
	}
};

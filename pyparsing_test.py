from pyparsing import *

import sys

cmdline = ' '.join(sys.argv[1:])

print cmdline


allchars=srange("[a-zA-Z0-9_$.]")

METHOD = Literal('method')
SIGNAL = Literal('signal')

LPAREN =Suppress(Literal('('))
RPAREN =Suppress(Literal(')'))

text = Word(allchars)

arg = text.setResultsName("arg_type") + text.setResultsName("arg_name") 

argslist = ZeroOrMore( arg + Suppress( ZeroOrMore( ',' ))
                       ).setResultsName("args")

line_expr = (
    (METHOD ^ SIGNAL).setResultsName('item_type') +
    text.setResultsName("return_type") +
    text.setResultsName("method_name")  +
    LPAREN + argslist + RPAREN
    )

print repr(METHOD or SIGNAL)
try:
    result = line_expr.parseString(cmdline)
    print result.asDict()
    print result.dump()
    print result 
except ParseException, e:
    print str(e)
    print cmdline
    print ' ' * e.loc + '^'
    


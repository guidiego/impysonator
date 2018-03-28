from re import compile, DOTALL

IMPERSONAL_EXPRESSIONS = [
    compile('(N|(\.|\s)n)ós', DOTALL),
    compile('(N|(\.|\s)n)oss(a|o)', DOTALL),
    compile('\w*(e|a)mos(,|\.|\s|$)', DOTALL)
]
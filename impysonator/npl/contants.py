from re import compile

IMPERSONAL_EXPRESSIONS = [
    compile('^(\.*)nós[\s|\.|$]'),
    compile('Nos| nos[\s|$]|-nos[\s|$]'),
    compile('[N|(\.|\s)n]oss[a|o]'),
    compile('\w*[e|a]mos[,|\.|\s|$]')
]
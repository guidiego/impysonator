from re import compile

IMPERSONAL_EXPRESSIONS = [
    compile('[N|(\.|\s)n]ós'),
    compile('[N|(\.|\s)n]os\s'),
    compile('[N|(\.|\s)n]oss[a|o]'),
    compile('\w*[e|a]mos[,|\.|\s|$]')
]
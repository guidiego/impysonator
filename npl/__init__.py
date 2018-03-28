from .impersonal import Impersonal

def found_impersonal(body):
    results = []

    for index, line in enumerate(body):
        i = Impersonal(line, index)

        if i.has_matches():
            results = sum([results, i.matches], [])

    return results
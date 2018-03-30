from impysonator.npl import found_impersonal


def assert_imp(imp, word, index):
    assert imp.get('word') == word
    assert imp.get('line') == index


def test_should_found_impersonal():
    fake_phrases = ["Nosso sonho", "resposta nossa", "esta em trenós"]
    imps = found_impersonal(fake_phrases)

    assert len(imps) == 2
    assert_imp(imps[0], "Nosso", 0)
    assert_imp(imps[1], "nossa", 1)

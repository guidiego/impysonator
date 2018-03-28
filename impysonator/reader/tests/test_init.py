from impysonator.reader import read

def assert_file(file, phrase):
    assert phrase in file.get_body()[0]

def test_read_folder():
    files = read('__mocks__')

    assert len(files) == 2
    assert_file(files[0], 'Nossa senhora nosso')
    assert_file(files[1], 'mais algum texto')

def test_read_file():
    files = read('__mocks__/file.txt')

    assert len(files) == 1
    assert_file(files[0], 'Nossa senhora nosso')
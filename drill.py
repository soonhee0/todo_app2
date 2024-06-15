def hoge_fixture():
    yield "hoge"


def test_hoge1(hoge_fixture):
    print(f"test_hoge1: {hoge_fixture}")


def test_hoge2(hoge_fixture):
    print(f"test_hoge2: {hoge_fixture}")

# ジェネレータ関数
g = hoge_fixture()
# ジェネレータ関数と__next__()で値を呼び出す
value = g.__next__()

test_hoge1(value)
test_hoge2(value)

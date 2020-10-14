class Monad():

    # モナドにはいろいろ種類があるので、継承したクラスで実装する。
    def __init__(self, a):
        raise NotImplementedError

    def _bind(self, func):
        raise NotImplementedError

    # 「|」を用いて関数をパイプできるようにする。
    def __or__ (self, func):
        return self._bind(func)

    # この関数でmaybeクラスのインスタンスをつくる
    @staticmethod
    def call_maybe(a=None):
        if a is not None:
            return Just(a)        
        else:
            return Nothing()

class Maybe(Monad):
    # このクラスを継承したJust・Nothingクラスでそれぞれ実装する
    def __init__(self, a):
        raise NotImplementedError

    def _bind(self, func):
        try:
            # 保持している値がNoneでない場合は受け取った関数をバインドし、返却値にJustを適用する。
            # None あるいは関数の処理で例外が発生した場合にはNothingを適用する。
            return Just(func(self.value)) if self.value is not None else Nothing()
        except Exception as e :
            print(e)
            return Nothing()

class Just(Maybe):
    def __init__(self, a=None):
        if a is not None:
            self.value = a
        else:
            raise ValueError
    def __repr__(self):
        return 'Just %r' % self.value

class Nothing(Maybe):
    def __init__(self, a=None):
        self.value = None

    def __repr__(self):
        return 'Nothing'
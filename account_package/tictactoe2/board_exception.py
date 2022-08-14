class BoardException(Exception):
    def _init_(self, message: str)-> None:
        super()._init_(message)
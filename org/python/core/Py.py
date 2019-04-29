class JavaError(RuntimeError):

    def __init__(self, cause):
        super(RuntimeError, self).__init__(cause)

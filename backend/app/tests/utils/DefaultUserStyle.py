class DefaultUserStyle:
    def __init__(self, minimum: float = 0, maximum: float = 255):
        self.colorRamp = "spectral"
        self.minMax = "minMax"
        self.meanStdDev = 2
        self.max = maximum
        self.min = minimum
        self.userMax = maximum
        self.userMin = minimum
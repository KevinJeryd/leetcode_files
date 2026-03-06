class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currentIdx = 0

    def visit(self, url: str) -> None:
        self.currentIdx = self.currentIdx + 1
        while len(self.history) - 1 >= self.currentIdx:
            self.history.pop()
        self.history.append(url)


    def back(self, steps: int) -> str:
        self.currentIdx = max(0, self.currentIdx - steps)
        return self.history[self.currentIdx]

    def forward(self, steps: int) -> str:
        self.currentIdx = min(len(self.history) - 1, self.currentIdx + steps)
        return self.history[self.currentIdx]

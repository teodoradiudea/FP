class RepoFile:
    def __init__(self):
        self.data = []
        self._file_loaded = False

    def _load(self):
        if self._file_loaded:
            return
        self._file_loaded = True
        try:
            with open("labirinth.txt", "rt") as fin:
                self.data = [[int(ch) for ch in line.strip()] for line in fin]
        except FileNotFoundError:
            print("The file labirinth.txt was not found.")

    def get_table(self):
        self._load()
        board = self.data
        return board
class Process:
    def __init__(self, process_id: int, time: int):
        self.process_id = process_id
        self.time = time

    def __str__(self):
        return f'{self.process_id} - {self.time} segundos.'

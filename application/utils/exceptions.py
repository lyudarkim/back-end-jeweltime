class AccountNotFoundException(Exception):
    def __init__(self, message="Account not found"):
        self.message = message
        super().__init__(self.message)


class ProjectNotFoundException(Exception):
    def __init__(self, message="Project not found"):
        self.message = message
        super().__init__(self.message)

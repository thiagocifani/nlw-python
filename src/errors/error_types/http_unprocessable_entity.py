class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str, status_code: int = 422) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Unprocessable Entity"
        self.status_code = status_code
        
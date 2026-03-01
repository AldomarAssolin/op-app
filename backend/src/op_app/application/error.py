class AppError(Exception):
    """Erro base da aplicação: carrega code/status/message/details."""
    code = "APP_ERROR"
    status_code = 500

    def __init__(self, message: str, *, details: dict | None = None, code: str | None = None, status_code: int | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}
        if code is not None:
            self.code = code
        if status_code is not None:
            self.status_code = status_code


class ValidationError(AppError):
    code = "VALIDATION_ERROR"
    status_code = 400


class NotFoundError(AppError):
    code = "NOT_FOUND"
    status_code = 404


class ConflictError(AppError):
    code = "CONFLICT"
    status_code = 409
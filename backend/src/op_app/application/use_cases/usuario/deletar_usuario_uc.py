class DeletarUsuarioUC:
    def execute(self, uow, usuario_id: int) -> bool:
        return uow.usuarios.delete_by_id(usuario_id)
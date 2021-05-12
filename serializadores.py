def diretores_from_web(**kwargs):
    return {
        "id": kwargs["id"] if kwargs["id"] else "",
        "nome completo": kwargs["nome completo"] if kwargs["nome completo"] else "",
    }

def diretores_from_db(*args):
    return {
        "id": kwargs["id"],
        "nome completo": kwargs[nome_completo],
    }

def nome_diretores_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else""

# usuario

def usuario_from_web(**kwargs):
    return {
        "nome completo": kwargs["nome completo"] if kwargs["nome completo"] else "",
        "cpf": kwargs["cpf"] if kwargs["cpf"] else ""
    }


def usuario_from_db(usuario):
    return {
        "nome completo": usuario["nome completo"],
        "cpf":usuario["cpf"],
    }
def nome_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else""

# filmes

def filmes_from_web(**filmes):
    return {

        "id": kwargs["filmes"] if kwargs["id"] else "",
        "titulo": kwargs["titulo"] if kwargs["titulo"] else "",
        "ano": kwargs["ano"] if kwargs["ano"] else ""
        "classificacao": kwargs["classificacao"] if kwargs["classificacao"] else "",
        "preco": kwargs["preco"] if kwargs[preco] else "",
        "diretores_id": kwargs["diretores_id"] if kwargs[diretores_id] else "",
        "generos_id": kwargs[generos_id] if kwargs[generos_id] else ""

    }

def filmes_from_db(*filmes):
    return {
           "id": kwargs["id"],
            "titulo": kwargs["titulo"],
            "ano": kwargs["ano"],
            "classificacao": kwargs["classificação"],
            "preco": kwargs["preco"],
            "diretores_id": kwargs["diretores_id"],
            "generos_id": kwargs["generos_id"],
        }


def nome_filmes_from_web(**kwargs):
        return kwargs["titulo"] if "titulo" in kwargs else ""


# generos


def generos_from_web(**generos):
        return {
            "id": kwargs["id"] if kwargs["id"] else "",
            "nome": kwargs["nome"] if kwargs["nome"] else "",
        }

def generos_from_db(*generos):
        return {
            "id": genero["id"],
            "nome": genero["nome"]
        }


def nome_generos_from_web(**kwargs):
    return kwargs["nome"] if "nome_" in kwargs else""


def locacoes_from_db(**locacoes):
        return {
            "id": kwargs["id"] if kwargs["id"] else "",
            "data_inicio": kwargs["data_inicio"] if kwargs["data_inicio"] else "",
            "data_fim": kwargs["data_fim"] if kwargs["data_fim"] else "",
            "filmes_id": kwargs["filmes_id"] if kwargs["filmes_id"] else "",
            "usuarios_id": kwargs["usuarios_id"] if kwargs["usuarios_id"] else "",

        }


def locacoes_from_web(locacoes):
        return {
            "id": kwargs[id],
            "data_inicio": kwargs["data_inicio"],
            "data_fim": kwargs["data_fim"],
            "filmes_id": kwargs["filmes_id"],
            "usuarios_id": kwargs["usuario_id"],
        }

def nome_locacoes_from_web(**kwargs):
        return kwargs["data_inicio"] if "data_inicio" in kwargs else ""


def pagamento_from_db(**kwargs):
        return {
            "id": kwargs["id"] if kwargs["id"] else "",
            "tipo": kwargs["tipo"] if kwargs["tipo"] else "",
            "status": kwargs["status"] if kwargs["status"] else "",
            "cod_pagamento": kwargs["cod_pagamento"] if kwargs["cod_pagamento"] else "",
            "valor": kwargs["valor"] if kwargs["valor"] else "",
            "data": kwargs["data"] if kwargs["data"] else "",
            "locacoes_id": kwargs["locacoes_id"] if kwargs["locacoes_id"] else "",
        }

    def pagamento_from_web(pagamento):
        return {
            "id": kwargs["id"]
            "titulo": kwargs["titulo"]
            "status": kwargs["status"]
            "codigo_pagamento": kwargs["codigo_pagamento"]
            "valor": kwargs["valor"]
            "data": kwargs["data"]
            "locacoes_id": kwargs["locacoes_id"]

        }

    def nome_pagamento_from_web(**kwargs):
        return kwargs["data_inicio"] if "data_inicio" in kwargs else ""

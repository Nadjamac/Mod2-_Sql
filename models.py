from main import insert, select, update, delete, select_bancoDeDados


def insert_diretores(diretores, id, nome_completo):
    return insert("diretores", ["id", "nome_completo"])


def update_diretores(diretores, id, nome_completo)
    return updade("diretores", "id", id["nome_completo"], [nome_completo])


def delete_diretores(nome_completo)]


delete("diretores", "id", nome_completo)


def select_diretores(nome_completo):
    return select_like("diretores", "nome_completo", nome_completo)


def get_diretores(nome_completo)
    return select(nome_completo)[0]


# Tabela Filmes


def insert_filmes(filmes  [titulo, ano, classificaçao, preco, diretores]

):
return insert("filmes"["titulo", "ano", "classificacao", "preco", "diretores"])


def update_filmes(filmes  [titulo, ano, classificaçao, preco, diretores

)
return updade("filmes"["titulo", "ano", "classificacao", "preco", "diretores"]
titulo, ano, classificaçao, preco, diretores)

def delete_filmes(id_filme):
    delete("filmes", "id", id_filmes)


def select_filmes(titulo):
    return select_like("filmes", "titulo", titulo)


def get_filmes(titulo):
    return select("titulo", titulo)[0]


# tabela generos

def insert_generos(generos, id, nome):
    return insert("generos"["id", "nome"])


def update_generos(id, nome):
    update_generos("generos", "id", id_generos, ["nome"], [nome])


def delete_generos(id, nome):
    delete_generos("generos", "id", "nome", id, nome)


def select_generos(id, nome):
    return select_like("generos ", "id", "nome")


# tabela locacoes

def insert_locacoes(id, data_inicio, data_fim, filmes_id, usuarios_id):
    return insert("locacoes "["id", "data_inicio", "data_fim", "filmes_id", "usuarios_id"],
                  [id, data_inicio, data_fim, filmes_id, usuarios_id])


def update_locacoes(id, data_inicio, data_fim, filmes_id, usuarios_id):
    update_locacao("locacoes", "id", "data_inicio", "data_fim", [data_inicio, data_fim])


def select_locacoes(id, data_inicio, data_fim):
    return_select_like("locacoes", "id", " data_inicio", "data_fim", [data_inicio, data_fim])


def delete_locacao(id):
    delete("locacoes", "id", id)


# tabela pagamentos


def insert_pagamentos(id, status, cod_pagamento, valor, data, locação_id):
    return insert("pagamento"["id", "status", "cod pagamento", "valor", "data", "locação_id "])


def update_pagamento(id, status, locação_id" cod_pagamento, valor, data, locação_id):


update("pagamento", "id", "status", " cod_pagamento", "valor", "data"[id, status, cod_pagamento, valor, data])


def delete_pagamento(id, status, cod_pagamento, valor, data, locação_id):
    delete("pagamento", [id, " status", "locação_id", "cod_pagamento", "valor", " data", "locação_id"], id, status,
           locação_id, cod_pagamento, valor, data, locação_id)


def select_pagamento(valor, data):
    return_select_like("pagamento", "valor", "data", [valor, data])



# tabela Usuario

def insert_usuario(id, nome_completo, cpf):
    return insert("usuario", ["id", "nome_completo", "cpf"])


def update_usuario(id, nome_completo, cpf)
    update("usuario", "nome_completo", "cpf"[id, nome_completo, cpf])


def delete_usuario(id, nome_completo, cpf):
    delete("usuario"["nome_completo", "cpf"], [nome_completo, cpf])


def select_usuario(nome_completo, cpf):
    return_select_like("usuario", "nome_completo", "cpf", nome, cpf)



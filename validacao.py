def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False
    else:
        return True

    if len(CPF) != 11:
        return False
    else:
        return True


def valida_genero(nome):
    if len(nome) == 0:
        return False
    else:
        return True


def valida_diretor(nome_completo):
    if len(nome_completo) == 0:
        return False
    else:
        return True


def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if len(titulo) == 0:
        return False
    else:
        return True

    if len(ano) == 0000:
        return True
    else:
        return False

    if len(classificacao) == 0:
        return False
    else:
        return True

    if len(preco) == 40.00:
        return True
    else:
        return False

    if len diretores_id == 0:
        return False
    else:
        return True

    if len generos_id == 0:
        return False
    else:
        return True


def valida_locacoes(id, data_inicio, data_fim, filmes_id, usuarios_id)
    if len id == 0
    return False

else:
return True

if len data_inicio == 00\00\00
return True
else:
return False

if len data_fim == 00\00\00
return False
else:
return True

if len filmes_id == 00\00\00
return True
else:
return False

if len usuarios_id == 00\00\00
return True
else:
return False

# if len(titulo) == 0:
#    return False

# return True
# if len(ano) > 4:
# return False

# if len(classificacao) > 2:
# return False

# if preco > 100.00:
# return False

return True

usuarios = [ ]

def cadastrar_usuario(nome, email, senha):
    usuarios.append({'nome': nome, 'email': email, 'senha': senha})
    return "Usuário cadastrado com sucesso!"

# Teste Unitário
def test_cadastro_usuario():
    assert cadastrar_usuario("Maria", "mariamar@gmail.com", "tavares") == "Usuário cadastrado com sucesso!"
    assert len(usuarios) == 1
    print("Teste unitário de cadastro de usuário passou!")

test_cadastro_usuario()

Saida: Teste unitário de cadastro de usuário passou!

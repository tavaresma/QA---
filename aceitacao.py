def test_aceitacao_fluxo_completo():
    assert cadastrar_usuario("Maria", "marimar@gmail.com, "tavares26") == "Usuário cadastrado com sucesso!"
    assert login_usuario("marimar@gmail.com, "tavares26"") == "Login bem-sucedido"
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("CadeiraGamer")
    assert carrinho.finalizar_compra() == "Compra finalizada com sucesso!"
    print("Teste de aceitação do fluxo completo passou!")

test_aceitacao_fluxo_completo()

Saida: Teste de aceitação do fluxo completo passou

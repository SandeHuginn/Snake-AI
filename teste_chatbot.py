from chatbot import enviar_mensagem

print("=== Teste do Chatbot Snake AI ===")

while True:
    mensagem = input("\nVocê: ")

    if mensagem.lower() in ["sair", "exit"]:
        print("Encerrando conversa...")
        break

    resposta = enviar_mensagem(mensagem)

    print(f"Snake AI: {resposta}")

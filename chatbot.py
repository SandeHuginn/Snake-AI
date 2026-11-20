import uuid
from google.cloud import dialogflow_v2 as dialogflow


# Identificação do projeto criado no Google Cloud.
PROJECT_ID = "snakeai-assistente-ytup"

# Identificador da sessão de conversa.
SESSION_ID = str(uuid.uuid4())


def enviar_mensagem(mensagem):
    """
    Envia uma mensagem ao Dialogflow e retorna a resposta do chatbot.
    """

    try:
        cliente = dialogflow.SessionsClient()

        sessao = cliente.session_path(PROJECT_ID, SESSION_ID)

        entrada_texto = dialogflow.TextInput(
            text=mensagem,
            language_code="pt-BR"
        )

        entrada_consulta = dialogflow.QueryInput(
            text=entrada_texto
        )

        resposta = cliente.detect_intent(
            request={
                "session": sessao,
                "query_input": entrada_consulta
            }
        )

        return resposta.query_result.fulfillment_text

    except Exception as erro:
        print(f"Erro ao comunicar com o Dialogflow: {erro}")
        return "Não foi possível conectar ao assistente no momento."

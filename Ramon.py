"""
Humanoide de Interação Rowts - "Taman"
Arquivo: rowts_humanoid.py

Descrição:
IA interativa que conversa com o usuário, integra os módulos da Rowts
e se adapta ao contexto para oferecer respostas e comandos dinâmicos.
"""

from fastapi import FastAPI, Form
from typing import Optional
from datetime import datetime
import random

app = FastAPI(title="Rowts Humanoid - Taman")

# Memória de contexto (simples, em produção pode usar banco de dados)
conversation_history = []

# Respostas de exemplo (poderão ser trocadas por chamadas a um LLM como GPT)
base_responses = [
    "Eu entendo… me conte mais.",
    "Interessante, mas o que você quer dizer com isso?",
    "Posso ajudar com algo do mundo Rowts agora?",
    "Sinto uma energia diferente na sua fala… quer explorar isso?",
    "Posso traduzir, criar arte ou guiar você pela UOPS, é só pedir."
]

@app.post("/talk")
def talk_with_taman(
    message: str = Form(...),
    user_name: Optional[str] = Form("Visitante"),
    emotion: Optional[str] = Form("neutro")
):
    """
    Conversa com o humanoide Taman.
    """
    global conversation_history

    # Registrar histórico
    conversation_history.append({
        "timestamp": datetime.now().isoformat(),
        "user": user_name,
        "message": message,
        "emotion": emotion
    })

    # Simular personalização de resposta
    if "traduza" in message.lower():
        reply = "Claro, me diga o texto e o idioma de destino."
    elif "uops" in message.lower():
        reply = "Conectando você à entrada da UOPS… respire fundo."
    elif "ocus" in message.lower():
        reply = "Ativando a explosão sensorial OCUS."
    elif "arte" in message.lower():
        reply = "Pronto para gerar uma arte transcendental para você."
    else:
        reply = random.choice(base_responses)

    return {
        "status": "ok",
        "user": user_name,
        "user_message": message,
        "taman_reply": reply,
        "context_length": len(conversation_history)
    }

@app.get("/history")
def get_conversation_history():
    """
    Retorna o histórico de conversa com o Taman.
    """
    return {"history": conversation_history}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("rowts_humanoid:app", host="0.0.0.0", port=8002, reload=True)

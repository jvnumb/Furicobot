from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Simulação de dados
next_games = [
    "FURIA vs NAVI - 25/04 às 18h (ESL Pro League)",
    "FURIA vs Vitality - 27/04 às 20h (Blast Premier)"
]

next_games_va = [
    "FURIA vs Team Liquid - 26/04 às 16h (Valorant Champions Tour)",
    "FURIA vs Sentinels - 28/04 às 18h (Valorant Champions Tour)"
]

lineup_cs = [
    " MOLODOY - Rifler ",
    " YEKINDAR - Rifler ",
    " FalleN - AWPer ",
    " KSCERATO - AWPer ",
    " yuurih - Rifler "
]

lineup_va = [
    " havoc - Duelista ",
    " Khalil - Initiator ",
    " raafa - Sentinel ",
    " heat - Duelista ",
    " mwzera (Reserva) ",
]

# Banco de dados de recado
recados_armazenados = []

quiz = [
    {
        "q": "Qual foi a melhor colocação da FURIA em um Major de CS?",
        "a": "Top 4 (Rio Major 2022)"
    },
    {
        "q": "Quem é o IGL da FURIA atualmente no CS?",
        "a": "FalleN"
    },
    {
        "q": "Qual a maior vitória da FURIA em torneios internacionais?",
        "a": "Vencedores do Blast Premier Global Final 2020"
    },
    {
        "q": "Qual foi a primeira conquista internacional da FURIA?",
        "a": "ESL Pro League Season 10"
    },
    {
        "q": "Em que ano a FURIA entrou para o cenário competitivo de CS?",
        "a": "2017"
    },
    {
        "q": "Quem é o AWPer da FURIA no CS?",
        "a": "FalleN"
    },
    {
        "q": "Quantos jogadores possuem no line-up da FURIA no CS?",
        "a": "5"
    },
    {
        "q": "Quem foi o MVP do Rio Major 2022?",
        "a": "KSCERATO"
    },
    {
        "q": "Qual time foi a maior rivalidade da FURIA no CS?",
        "a": "MIBR"
    },
    {
        "q": "Qual foi a maior virada de FURIA em uma grande competição?",
        "a": "Vira a série contra Vitality no Blast Premier"
    },
    {
        "q": "Quem foi o MVP do torneio Blast Premier Global Final 2020?",
        "a": "yuurih"
    },
    {
        "q": "Quantos jogadores da FURIA jogaram o Major de 2022?",
        "a": "5"
    },
    {
        "q": "Qual jogador da FURIA é conhecido por ser um dos melhores riflers?",
        "a": "yuurih"
    },
    {
        "q": "Quem é o principal mentor do time da FURIA?",
        "a": "Guerri (técnico)"
    },
    {
        "q": "Qual é o papel de Khalil na FURIA do Valorant?",
        "a": "Initiator"
    },
    {
        "q": "Qual jogador da FURIA do Valorant é o principal duelista?",
        "a": "havoc"
    },
    {
        "q": "Em que ano a FURIA entrou no competitivo de Valorant?",
        "a": "2020"
    },
    {
        "q": "Quem é o coach da FURIA Valorant?",
        "a": "peu"
    },
    {
        "q": "Qual time é o maior rival da FURIA no Valorant?",
        "a": "LOUD"
    }
]

# Comandos
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🖤 Salve, furioso ! Seja bem-vindo ao QG da FURIA no Telegram 🖤\n\n"
        "Aqui você:\n"
        "📢 Fica por dentro de tudo da Furia\n"
        "💬 Pode interagir, deixar sua opinião e trocar ideia\n"
        "🎮 E ainda desafia seus amigos com um quiz maneiro!\n\n"
        "*Comandos disponíveis:*\n"
        "➡️ /jogoscs – Próximo jogo de CS2\n"
        "➡️ /jogosval – Próximo jogo de Valorant\n"
        "➡️ /lineupcs – Escalação atual do CS2\n"
        "➡️ /lineupval – Escalação do time de Valorant\n"
        "➡️ /recado – Mande um recado ou conselho pra org\n"
        "➡️ /quiz – Desafie seus amigos no quiz da FURIA\n\n"
        "A selva é nossa. Pra cima com tudo! 🖤",
    )

async def jogoscs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Próximos jogos de CS:\n" + "\n".join(next_games))

async def nextgame_va(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Próximos jogos de Valorant:\n" + "\n".join(next_games_va))

async def show_lineup_cs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Lineup atual da FURIA (CS):\n" + "\n".join(lineup_cs))

async def show_lineup_va(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Lineup atual da FURIA (Valorant):\n" + "\n".join(lineup_va))

async def show_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = random.choice(quiz)
    await update.message.reply_text(f"❓ {q['q']}\n\n✅ Resposta: {q['a']}")

async def recado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = " ".join(context.args)
    if mensagem:
        recados_armazenados.append(mensagem)
        await update.message.reply_text(
            f"✅ Obrigado pelo seu recado!\n"
            "Nós estamos sempre de olho no que a torcida tem a dizer! 👀🖤\n\n",
        )
    else:
        await update.message.reply_text(
            "⚠️ Escreva seu recado junto com o comando, tipo:\n`/recado Vamos dominar esse split com o Fallen de AWP!`\n",
        )

# Setup do bot
def main():
    app = ApplicationBuilder().token("7881602506:AAG7_cz8RKOfZQoT5YMBJS_MPCYQDw_gI5E").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogoscs", jogoscs))
    app.add_handler(CommandHandler("jogosval", nextgame_va))
    app.add_handler(CommandHandler("lineupcs", show_lineup_cs))
    app.add_handler(CommandHandler("lineupval", show_lineup_va))
    app.add_handler(CommandHandler("quiz", show_quiz))
    app.add_handler(CommandHandler("recado", recado))

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
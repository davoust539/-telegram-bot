import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("8857579656:AAFbVSeUSIiO03njqQqkJunPOCmMF9wX2j4")


def accueil():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📋 Menu", callback_data="menu")],
        [InlineKeyboardButton("💳 Rechargement", callback_data="rechargement")],
        [InlineKeyboardButton("👤 Profil", callback_data="profil")],
        [InlineKeyboardButton("⚙️ Paramètres", callback_data="parametres")]
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bienvenue dans notre boutique !\n\nChoisissez une option :",
        reply_markup=accueil()
    )


async def boutons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "menu":
        await query.edit_message_text("📋 Menu (étape suivante)")

    elif query.data == "rechargement":
        await query.edit_message_text("💳 Rechargement (étape suivante)")

    elif query.data == "profil":
        await query.edit_message_text("👤 Solde : 0 €")

    elif query.data == "parametres":
        await query.edit_message_text("⚙️ Contact : @TON_TELEGRAM")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(boutons))

print("Bot démarré...")

app.run_polling()

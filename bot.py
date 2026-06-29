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

TOKEN = os.getenv("BOT_TOKEN")


# ==========================
# MENU PRINCIPAL
# ==========================

def accueil_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📋 Menu", callback_data="menu")],
        [InlineKeyboardButton("💳 Rechargement", callback_data="rechargement")],
        [InlineKeyboardButton("👤 Profil", callback_data="profil")],
        [InlineKeyboardButton("⚙️ Paramètres", callback_data="parametres")]
    ])


# ==========================
# MENU PRODUITS
# ==========================

def menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🍫 Coca", callback_data="coca")],
        [InlineKeyboardButton("🍫 Cali", callback_data="cali")],
        [InlineKeyboardButton("🍫 Amené", callback_data="amene")],
        [InlineKeyboardButton("🍫 3M", callback_data="3m")],
        [InlineKeyboardButton("🍫 Coco", callback_data="coco")],
        [InlineKeyboardButton("⬅️ Retour", callback_data="accueil")]
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bienvenue dans notre boutique.\n\nChoisissez une option :",
        reply_markup=accueil_keyboard()
    )


async def boutons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "accueil":
        await query.edit_message_text(
            "👋 Bienvenue dans notre boutique.\n\nChoisissez une option :",
            reply_markup=accueil_keyboard()
        )

    elif query.data == "menu":
        await query.edit_message_text(
            "🍫 Choisissez une gamme :",
            reply_markup=menu_keyboard()
        )

    elif query.data == "rechargement":
        await query.edit_message_text(
            "💳 Rechargement\n\nCette partie sera créée à l'étape suivante."
        )

    elif query.data == "profil":
        await query.edit_message_text(
            "👤 Profil\n\n💰 Solde : 0 €"
        )

    elif query.data == "parametres":
        await query.edit_message_text(
            "⚙️ Paramètres\n\nSupport : @TON_TELEGRAM"
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(boutons))

app.run_polling()

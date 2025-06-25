from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "7692094977:AAGDIMxSIIdZA4uYhZH9xHUt7XY3K_C8XP8"

# دالة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("📩 استقبلنا /start")  # ← للتأكد إن /start اشتغلت
    keyboard = [
        [InlineKeyboardButton("💄 Cosmetics", callback_data="cosmetics")],
        [InlineKeyboardButton("💊 Pharma", callback_data="pharma")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "أهلاً وسهلاً بك في TravAsist 🌍\nاختار القسم اللي محتاجه من القايمة 👇",
        reply_markup=reply_markup
    )

# دالة التعامل مع الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    choice = query.data

    # قائمة Cosmetics
    if choice == "cosmetics":
        keyboard = [
            [InlineKeyboardButton("🧴 Bioderma", callback_data="bioderma")],
            [InlineKeyboardButton("🧴 LaRoche", callback_data="laroche")],
            [InlineKeyboardButton("🧴 Vichy", callback_data="vichy")],
            [InlineKeyboardButton("🧴 CeraVe", callback_data="cerave")],
            [InlineKeyboardButton("🧴 Ducray", callback_data="ducray")],
            [InlineKeyboardButton("🧴 Isis Pharma", callback_data="isis")],
            [InlineKeyboardButton("🧴 Pharmaceris", callback_data="pharmaceris")],
            [InlineKeyboardButton("🧴 Avene", callback_data="avene")],
            [InlineKeyboardButton("🧴 Uriage", callback_data="uriage")],
            [InlineKeyboardButton("🧴 Body Care", callback_data="body")],
            [InlineKeyboardButton("🧴 Hair Care", callback_data="hair")],
            [InlineKeyboardButton("🧴 Dark Circles", callback_data="dark")],
            [InlineKeyboardButton("🧴 Egyptian Product", callback_data="egyptian")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("💄 اختر من قسم Cosmetics:", reply_markup=reply_markup)

    # قائمة Pharma
    elif choice == "pharma":
        keyboard = [
            [InlineKeyboardButton("💪 Vitamins", callback_data="vitamins")],
            [InlineKeyboardButton("🤧 Allergy Relief", callback_data="allergy")],
            [InlineKeyboardButton("🩺 CVS", callback_data="cvs")],
            [InlineKeyboardButton("🍽️ GIT", callback_data="git")],
            [InlineKeyboardButton("🧪 Another", callback_data="another")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("💊 اختر من قسم Pharma:", reply_markup=reply_markup)

    # الردود على عناصر Cosmetics
    elif choice == "bioderma":
        await query.edit_message_text("🧴 Bioderma: منتجات متخصصة للبشرة الحساسة.")
    elif choice == "laroche":
        await query.edit_message_text("🧴 La Roche-Posay: تركيبة فعالة ومناسبة للبشرة الدهنية.")
    elif choice == "vichy":
        await query.edit_message_text("🧴 Vichy: تجديد وترطيب من مصدر فرنسي.")
    elif choice == "cerave":
        await query.edit_message_text("🧴 CeraVe: ترطيب عميق وحماية للبشرة.")
    elif choice == "ducray":
        await query.edit_message_text("🧴 Ducray: منتجات علاجية لفروة الرأس والبشرة.")
    elif choice == "isis":
        await query.edit_message_text("🧴 Isis Pharma: عناية فائقة بالبشرة الحساسة.")
    elif choice == "pharmaceris":
        await query.edit_message_text("🧴 Pharmaceris: تركيبات طبية لبشرة صحية.")
    elif choice == "avene":
        await query.edit_message_text("🧴 Avene: مياه حرارية وعناية لطيفة بالبشرة.")
    elif choice == "uriage":
        await query.edit_message_text("🧴 Uriage: توازن طبيعي ورطوبة مثالية.")
    elif choice == "body":
        await query.edit_message_text("🧴 Body Care: منتجات مخصصة للعناية بالجسم بالكامل.")
    elif choice == "hair":
        await query.edit_message_text("🧴 Hair Care: شامبو، بلسم وعلاجات لفروة الرأس.")
    elif choice == "dark":
        await query.edit_message_text("🧴 Dark Circles: كريمات فعالة لتفتيح الهالات.")
    elif choice == "egyptian":
        await query.edit_message_text("🧴 Egyptian Product: منتجات مصرية بجودة ممتازة.")

    # الردود على عناصر Pharma
    elif choice == "vitamins":
        await query.edit_message_text("💪 Vitamins: تعزيز المناعة والطاقة.")
    elif choice == "allergy":
        await query.edit_message_text("🤧 Allergy Relief: أدوية فعالة للحساسية.")
    elif choice == "cvs":
        await query.edit_message_text("🩺 CVS: القلب والدورة الدموية.")
    elif choice == "git":
        await query.edit_message_text("🍽️ GIT: المعدة والجهاز الهضمي.")
    elif choice == "another":
        await query.edit_message_text("🧪 Other Pharma Products: منتجات طبية أخرى.")

    # الرجوع للرئيسية
    elif choice == "main":
        keyboard = [
            [InlineKeyboardButton("💄 Cosmetics", callback_data="cosmetics")],
            [InlineKeyboardButton("💊 Pharma", callback_data="pharma")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⬅️ رجعتك للقائمة الرئيسية 👇", reply_markup=reply_markup)

# تشغيل البوت
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ البوت شغال بالقوائم الكاملة 💄💊")
    app.run_polling()


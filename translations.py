

translations = {
    '<b>Логин:</b> {message.from_user.full_name}\n<b>Статус:</b> {premiumStatus(user.premium)}\n<b>Зарегистрирован:</b> {user.registr_date}': '<b>Login:</b> {message.from_user.full_name}\n<b>Status:</b> {premiumStatus(user.premium)}\n<b>Registered:</b> {user.registr_date}'

}

def _(text, lang='ru'):
    if lang == 'ru':
        return text
    else:
        global translations
        try:
            return translations[lang][text]
        except:
            return text
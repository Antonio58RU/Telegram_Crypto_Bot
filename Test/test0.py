class StatsFullSt(StatesGroup):
    nameCrypto = State()  
    
@router.callback_query(F.data == 'getStatsFull')
async def get_statsFull(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(StatsFullSt.nameCrypto)
    lang = await rq.get_localization(callback.from_user.id)
    await callback.message.answer(_('Введите название криптовалюты.', lang), parse_mode='html')
    
@router.message(StatsFullSt.nameCrypto)
async def StatsFull_stats(message: Message, state: FSMContext):
    await state.update_data(nameCrypto = message.text)
    data = await state.get_data()
    crypto_name = data['nameCrypto']
    await get_messageStatsFull(crypto_name, message)
    
    await state.clear()
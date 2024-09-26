from aiogram.dispatcher.filters.state import State, StatesGroup
API_KEY = '7516662169:AAEPRfniZ8JhRxV42xFKMB9aKPagfknenIw'

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()

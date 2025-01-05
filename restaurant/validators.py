from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    if not re.match(r'^\+?[0-9]*$', value):
        raise ValidationError('Telefon raqami raqamli bolishi va + bilan boshlanishi mumkin.')

def validate_username(value):
    if not re.match(r'^[\w.@+-]+$', value):
        raise ValidationError('Foydalanuvchi nomi faqat harflar, raqamlar va . @ + - belgilaridan iborat bo\'lishi mumkin.')
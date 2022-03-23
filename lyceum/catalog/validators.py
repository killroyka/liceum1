from django.core.exceptions import ValidationError


def validate_brilliant(value):
    must_word = {'превосходно', 'роскошно'}
    value = value.lower()
    if not (set(value.split()) - must_word) or len(value.split()) < 2:
        raise ValidationError(f'Обязательно используйте слова {" ".join(must_word)}!')


def validate_eng(value):
    value = value.lower()
    must_be = 'qwertyuiopasdfghjklzxcvbnm-_'
    for x in value:
        if x not in must_be:
            raise ValidationError("Допустимы только буквы латиницы и символы - и _")


def validate_max_number(value):
    if value > 32767 or value < 0:
        raise ValidationError("число должно быть меньше 32767 и больше 0")

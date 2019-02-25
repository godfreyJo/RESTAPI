from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXER = [item for item in get_all_lexers()if item[1]]
LANGUAGE_CHOICE = sorted([(item [1][0], item[0])for item in LEXER])
STYLE_CHOICES = sorted((item,item)for item in get_all_styles())
# coding: utf8

from __future__ import unicode_literals, print_function
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS

from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS
from .tag_map import TAG_MAP

from ...attrs import LANG
from ...language import Language

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...util import update_exc
from ...lookups import Lookups


class ArmenianDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters[LANG] = lambda text: "hy"
    lex_attr_getters.update(LEX_ATTRS)

    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS
    tag_map = TAG_MAP


class Armenian(Language):
    lang = "hy"
    Defaults = ArmenianDefaults


__all__ = ["Armenian"]

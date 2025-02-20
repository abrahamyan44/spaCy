# coding: utf8
from __future__ import unicode_literals

import pytest


# TODO add test cases with valid punctuation signs.

hy_tokenize_text_test = [
    (
        "Մետաղագիտությունը պայմանականորեն բաժանվում է տեսականի և կիրառականի (տեխնիկական)",
        [
            "Մետաղագիտությունը",
            "պայմանականորեն",
            "բաժանվում",
            "է",
            "տեսականի",
            "և",
            "կիրառականի",
            "(",
            "տեխնիկական",
            ")",
        ],
    ),
    (
        "Գետաբերանը գտնվում է Օմոլոնա գետի ձախ ափից 726 կմ հեռավորության վրա",
        [
            "Գետաբերանը",
            "գտնվում",
            "է",
            "Օմոլոնա",
            "գետի",
            "ձախ",
            "ափից",
            "726",
            "կմ",
            "հեռավորության",
            "վրա",
        ],
    ),
    ( "Կինոարվեստի և գիտության ակադեմիան (անգլ.՝ Academy of Motion Picture Arts and Sciences",
    [
        "Կինոարվեստի",
        "և",
        "գիտության",
        "ակադեմիան",
        "(",
        "անգլ.",
        "՝",
        "Academy",
        "of",
        "Motion",
        "Picture",
        "Arts",
        "and",
        "Sciences",
    ],
      ),
   ("վերջինս Պարույր նահապետի որդին էր և Ասորեստանի Նաբուգոդոնոսոր Բ (Ք.ա. 605–562 թթ.) թագավորի ժամանակակիցը.",
       [
           "վերջինս",
           "Պարույր",
           "նահապետի",
           "որդին",
           "էր",
           "և",
           "Ասորեստանի",
           "Նաբուգոդոնոսոր",
           "Բ",
           "()",
           "Ք.ա.",
           "605",
           "–",
           "562",
           "թթ.",
           ")",
           "թագավորի",
           "ժամանակակիցը.",
       ],
    ),

]


@pytest.mark.parametrize("text,expected_tokens", hy_tokenize_text_test)
def test_ga_tokenizer_handles_exception_cases(hy_tokenizer, text, expected_tokens):
    tokens = hy_tokenizer(text)
    token_list = [token.text for token in tokens if not token.is_space]
    assert expected_tokens == token_list

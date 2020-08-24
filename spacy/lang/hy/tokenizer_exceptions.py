# encoding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, NORM


_exc = {}

_abbrev_exc = [
    # Weekdays abbreviations
    {ORTH: "երկ", LEMMA: "երկուշաբթի", NORM: "երկուշաբթի"},
    {ORTH: "երք", LEMMA: "երեքշաբթի", NORM: "երեքշաբթի"},
    {ORTH: "չրք", LEMMA: "չորեքշաբթի", NORM: "չորեքշաբթի"},
    {ORTH: "հնգ", LEMMA: "հինգշաբթի", NORM: "հինգշաբթի"},
    {ORTH: "ուրբ", LEMMA: "ուրբաթ", NORM: "ուրբաթ"},
    {ORTH: "շբթ", LEMMA: "շաբաթ", NORM: "շաբաթ"},
    {ORTH: "կիր", LEMMA: "կիրակի", NORM: "կիրակի"},
    # Months abbreviations
    {ORTH: "հնվ", LEMMA: "հունվար", NORM: "հունվար"},
    {ORTH: "փետ", LEMMA: "փետրվար", NORM: "փետրվար"},
    {ORTH: "մրտ", LEMMA: "մարտ", NORM: "մարտ"},
    {ORTH: "ապր", LEMMA: "ապրիլ", NORM: "ապրիլ"},
    {ORTH: "մայ", LEMMA: "մայիս", NORM: "մայիս"},
    {ORTH: "հուն", LEMMA: "հունիս", NORM: "հունիս"},
    {ORTH: "հուլ", LEMMA: "հուլիս", NORM: "հուլիս"},
    {ORTH: "օգս", LEMMA: "օգոստոս", NORM: "օգոստոս"},
    {ORTH: "սեպ", LEMMA: "սեպտեմբեր", NORM: "սեպտեմբեր"},
    {ORTH: "հոկ", LEMMA: "հոկտեմբեր", NORM: "հոկտեմբեր"},
    {ORTH: "նոյ", LEMMA: "նոյեմբեր", NORM: "նոյեմբեր"},
    {ORTH: "դեկ", LEMMA: "դեկտեմբեր", NORM: "դեկտեմբեր"},
    # Length abbreviations
    {ORTH: "մմ", LEMMA: "միլիմետր", NORM: "միլիմետր"},
    {ORTH: "սմ", LEMMA: "սանտիմետր", NORM: "սանտիմետր"},
    {ORTH: "մ", LEMMA: "մետր", NORM: "մետր"},
    {ORTH: "կմ", LEMMA: "կիլոմետր", NORM: "կիլոմետր"},
]


for abbrev_desc in _abbrev_exc:
    abbrev = abbrev_desc[ORTH]
    for orth in (abbrev, abbrev.capitalize(), abbrev.upper()):
        _exc[orth] = [{ORTH: orth, LEMMA: abbrev_desc[LEMMA], NORM: abbrev_desc[NORM]}]
        _exc[orth + "."] = [
            {ORTH: orth + ".", LEMMA: abbrev_desc[LEMMA], NORM: abbrev_desc[NORM]}
        ]




TOKENIZER_EXCEPTIONS = _exc

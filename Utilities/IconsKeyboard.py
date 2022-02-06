"""Defines simple icon keyboard."""
#Made by: @[Just] Freak#4999 / Freaku

# • Icon Keyboard •
# Make your chats look even more cooler!
# Make sure "Always Use Internal Keyboard" is ON
# Double tap the space to change between keyboards...




# ba_meta require api 6

from __future__ import annotations

from typing import TYPE_CHECKING

import ba
from _ba import charstr as uwu
from ba._enums import SpecialChar

if TYPE_CHECKING:
    from typing import Any, Optional, Dict, List, Tuple,Type, Iterable

__version__ ='1' #done

# I spent quite some time, figuring out new icons and typing this ....
# Change credits = Instant DEATH!









# ba_meta export keyboard
class IconKeyboard_byFreaku(ba.Keyboard):
    """Keyboard go brrrrrrr"""
    name = 'Icons by \ue048Freaku'
    chars = [(uwu(SpecialChar.TICKET),
            uwu(SpecialChar.CROWN),
            uwu(SpecialChar.DRAGON),
            uwu(SpecialChar.SKULL),
            uwu(SpecialChar.HEART),
            uwu(SpecialChar.FEDORA),
            uwu(SpecialChar.HAL),
            uwu(SpecialChar.YIN_YANG),
            uwu(SpecialChar.EYE_BALL),
            uwu(SpecialChar.HELMET),
            uwu(SpecialChar.OUYA_BUTTON_U)),
            (uwu(SpecialChar.MUSHROOM),
            uwu(SpecialChar.NINJA_STAR),
            uwu(SpecialChar.VIKING_HELMET),
            uwu(SpecialChar.MOON),
            uwu(SpecialChar.SPIDER),
            uwu(SpecialChar.FIREBALL),
            uwu(SpecialChar.MIKIROG),
            uwu(SpecialChar.OUYA_BUTTON_O),
            uwu(SpecialChar.LOCAL_ACCOUNT),
            uwu(SpecialChar.LOGO)),
            (uwu(SpecialChar.TICKET),
            uwu(SpecialChar.FLAG_INDIA),
            uwu(SpecialChar.OCULUS_LOGO),
            uwu(SpecialChar.STEAM_LOGO),
            uwu(SpecialChar.NVIDIA_LOGO),
            uwu(SpecialChar.GAME_CENTER_LOGO),
            uwu(SpecialChar.GOOGLE_PLAY_GAMES_LOGO),
            uwu(SpecialChar.OUYA_BUTTON_A))]
    nums = []
    pages: Dict[str, Tuple[str, ...]] = {}

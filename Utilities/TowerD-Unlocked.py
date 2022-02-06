#Made by @[Just] Freak#4999 / Freaku

# ba_meta require api 6

from __future__ import annotations

from typing import TYPE_CHECKING

import ba
import _ba
from bastd.maps import TowerD

if TYPE_CHECKING:
    from typing import List, Tuple, Any, Optional

@classmethod
def new_play_types(cls) -> List[str]:
    """return valid play types for this map."""
    return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

# ba_meta export plugin
class byFreaku(ba.Plugin):
    def on_app_launch(self):
        TowerD.get_play_types = new_play_types

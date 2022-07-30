#Frozen One ported
#By your friend: @[Just] Freak#4999


import ba
from bastd.game.chosenone import Player, ChosenOneGame


# ba_meta require api 7
# ba_meta export game
class FrozenOneGame(ChosenOneGame):
    name = 'Frozen One'

    def _set_chosen_one_player(self, player: Player) -> None:
        super()._set_chosen_one_player(player)
        if hasattr(player, 'actor'):
            player.actor.frozen = True
            player.actor.node.frozen = 1

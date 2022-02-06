from __future__ import annotations


## Map Credits: byANG3L ##
## Modpack Credits: BSWorld (https://youtu.be/1TN56NLlShE) ##
## Plugin by: Jinx (https://github.com/JinxBs/BombSquad-Community-Plugin-Manager/blob/main/plugins/allMapsInOne.py) ##


# was modified for "Freaku Maps" server by me ##



# ba_meta require api 6

import os, ssl, threading, urllib.request
from hashlib import md5
from typing import TYPE_CHECKING

import _ba, ba
from ba import _map
from bastd.gameutils import SharedObjects

ssl._create_default_https_context = ssl._create_unverified_context

if TYPE_CHECKING:
    from typing import Any


file_naam = __name__ + '.py'
file_location = _ba.env()['python_directory_user'] + '/' + file_naam
my_version = 5
ur_version = 5


package_name = "Maps for \ue048Freaku's server"

package_files = {
    # arena mini gore map
    "arenaminigoreMapCob.cob": {
        "md5": "fde6e6c61ffe5201dc814eeb97a84418",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/arenaminigoreMap/arenaminigoreMapCob.cob",
        "target": "ba_data/models/arenaminigoreMapCob.cob"
    },
    "arenaminigoreMapColor.dds": {
        "md5": "5380f35794ade00de4cc68de0d6e29ad",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/arenaminigoreMap/arenaminigoreMapColor.dds",
        "target": "ba_data/textures/arenaminigoreMapColor.dds"
    },
    "arenaminigoreMapColor.ktx": {
        "md5": "8588a0ae308f6e04f000eea6ffbdc00c",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/arenaminigoreMap/arenaminigoreMapColor.ktx",
        "target": "ba_data/textures/arenaminigoreMapColor.ktx"
    },
    "arenaminigoreMap.bob": {
        "md5": "42be9c3b8bf3f595d53b8b0223723194",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/arenaminigoreMap/arenaminigoreMap.bob",
        "target": "ba_data/models/arenaminigoreMap.bob"
    },
    "arenaMinigorePreview.dds": {
        "md5": "9eed3b7c488d0ef3738d63445b5ae7e3",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/arenaminigoreMap/arenaMinigorePreview.dds",
        "target": "ba_data/textures/arenaMinigorePreview.dds"
    },
    "arenaMinigorePreview.ktx": {
        "md5": "ad72dd59ac437f0dd3cd89ad073dd185",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/arenaminigoreMap/arenaMinigorePreview.ktx",
        "target": "ba_data/textures/arenaMinigorePreview.ktx"
    },

    # bikini bottom map
    "bikiniBottomMapBG.bob": {
        "md5": "05313e78a62302fe2791ad8fd3ef24bc",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/bikiniBottomMapBG.bob",
        "target": "ba_data/models/bikiniBottomMapBG.bob"
    },
    "bikiniBottomMapBGColor.ktx": {
        "md5": "6c06dfc088b8edd54fab7a745b60061c",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/bikiniBottomMapBGColor.ktx",
        "target": "ba_data/textures/bikiniBottomMapBGColor.ktx"
    },
    "cangremovilColor.ktx": {
        "md5": "43301ff824cd1d485509674e6e49ed62",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/cangremovilColor.ktx",
        "target": "ba_data/textures/cangremovilColor.ktx"
    },
    "bikiniBottomMapColor.ktx": {
        "md5": "91f764531b63faa1c15753c4cfb9f299",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/bikiniBottomMapColor.ktx",
        "target": "ba_data/textures/bikiniBottomMapColor.ktx"
    },
    "bikiniBottomMapColor.dds": {
        "md5": "e499bfec39d793b0bf40424b99057e09",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/bikiniBottomMapColor.dds",
        "target": "ba_data/textures/bikiniBottomMapColor.dds"
    },
    "bikiniBottomMapCob.cob": {
        "md5": "1c5662b93973e69c63e449ee17fd523f",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/bikiniBottomMapCob.cob",
        "target": "ba_data/models/bikiniBottomMapCob.cob"
    },
    "cangremovilColor.dds": {
        "md5": "948f7a83275db17451c6b6ed862a5cd0",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/cangremovilColor.dds",
        "target": "ba_data/textures/cangremovilColor.dds"
    },
    "bikiniBottomMapBGColor.dds": {
        "md5": "33c0f36dad26b4ac904b3e2b8b53b913",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/bikiniBottomMapBGColor.dds",
        "target": "ba_data/textures/bikiniBottomMapBGColor.dds"
    },
    "bikiniBottomPreview.dds": {
        "md5": "93b19b85f00ebee9932da09f22bb4b15",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/bikiniBottomPreview.dds",
        "target": "ba_data/textures/bikiniBottomPreview.dds"
    },
    "bikiniBottomPreview.ktx": {
        "md5": "d9275a66db9dff147a50b0b769e21aea",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/bikiniBottomPreview.ktx",
        "target": "ba_data/textures/bikiniBottomPreview.ktx"
    },
    "cangremovilModel.bob": {
        "md5": "986d4699e7bfe3bf55db008634a503bf",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/cangremovilModel.bob",
        "target": "ba_data/models/cangremovilModel.bob"
    },
    "bikiniBottomMap.bob": {
        "md5": "bb10c4aedaa7fa0f82ac6a9b25d3dd53",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bikiniBottomMap/bikiniBottomMap.bob",
        "target": "ba_data/models/bikiniBottomMap.bob"
    },

    # bomberman map
    "bombermanMapColor.dds": {
        "md5": "ed7911ea9b23cea1c2044b27bc8a413c",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bombermanMap/bombermanMapColor.dds",
        "target": "ba_data/textures/bombermanMapColor.dds"
    },
    "bombermanMapPreview.ktx": {
        "md5": "0d8579bcf5169588f23ff18b6d0c2338",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bombermanMap/bombermanMapPreview.ktx",
        "target": "ba_data/textures/bombermanMapPreview.ktx"
    },
    "bombermanMapPreview.dds": {
        "md5": "297df338402bea9c49c4b7ff5ba0c593",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bombermanMap/bombermanMapPreview.dds",
        "target": "ba_data/textures/bombermanMapPreview.dds"
    },
    "bombermanMapCob.cob": {
        "md5": "7a0ce7caf64821e04fbebdd32075ebc0",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bombermanMap/bombermanMapCob.cob",
        "target": "ba_data/models/bombermanMapCob.cob"
    },
    "bombermanMapColor.ktx": {
        "md5": "9475047324957a7270143a173f71d2a9",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bombermanMap/bombermanMapColor.ktx",
        "target": "ba_data/textures/bombermanMapColor.ktx"
    },
    "bombermanMap.bob": {
        "md5": "b1e809656e200056a1f5df9fbcac1c6f",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/bombermanMap/bombermanMap.bob",
        "target": "ba_data/models/bombermanMap.bob"
    },

    # courage map
    "courageBGColor.ktx": {
        "md5": "f8b40a6652e3c4676c9a5a993e3da888",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/courageMap/courageBGColor.ktx",
        "target": "ba_data/textures/courageBGColor.ktx"
    },
    "courageMapColor.ktx": {
        "md5": "55d4cb427671307b3f079c6f17970e7f",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/courageMap/courageMapColor.ktx",
        "target": "ba_data/textures/courageMapColor.ktx"
    },
    "courageMap.bob": {
        "md5": "d4e13d0902a6bc94a5ec4582e685f432",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/courageMap/courageMap.bob",
        "target": "ba_data/models/courageMap.bob"
    },
    "courageMapPreview.dds": {
        "md5": "302a82c26f15d76d41a021b503cfbed4",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/courageMap/courageMapPreview.dds",
        "target": "ba_data/textures/courageMapPreview.dds"
    },
    "courageMapPreview.ktx": {
        "md5": "82ce6089d43c51bc49b70c1a2ec0410b",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/courageMap/courageMapPreview.ktx",
        "target": "ba_data/textures/courageMapPreview.ktx"
    },
    "courageBGColor.dds": {
        "md5": "7a1f36e515db763dbbc4dd964862c85b",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/courageMap/courageBGColor.dds",
        "target": "ba_data/textures/courageBGColor.dds"
    },
    "courageMapColor.dds": {
        "md5": "bab38b7ec1008e18e4725f80eec55010",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/courageMap/courageMapColor.dds",
        "target": "ba_data/textures/courageMapColor.dds"
    },
    "courageMapCob.cob": {
        "md5": "855b2aed970c961d11614e2445ad49b9",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/courageMap/courageMapCob.cob",
        "target": "ba_data/models/courageMapCob.cob"
    },

    # cragcatle map
    "cragCastleBigPreview.ktx": {
        "md5": "85235ee6e75074c3b8dfd77fc8c84fe3",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/cragcastleMap/cragCastleBigPreview.ktx",
        "target": "ba_data/textures/cragCastleBigPreview.ktx"
    },
    "cragCastleLevelBig.bob": {
        "md5": "10975567481e02de6c13f01dd94942c3",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/cragcastleMap/cragCastleLevelBig.bob",
        "target": "ba_data/models/cragCastleLevelBig.bob"
    },
    "cragCastleLevelBottomBig.bob": {
        "md5": "39d5313854efb10054cf26bc9be09919",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/cragcastleMap/cragCastleLevelBottomBig.bob",
        "target": "ba_data/models/cragCastleLevelBottomBig.bob"
    },
    "cragCastleLevelBumperBig.cob": {
        "md5": "37427fc882b0c842f0457a17fb1c2bba",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/cragcastleMap/cragCastleLevelBumperBig.cob",
        "target": "ba_data/models/cragCastleLevelBumperBig.cob"
    },
    "cragCastleBigPreview.dds": {
        "md5": "682fcde82d682f2dabfdad36eca455e2",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/cragcastleMap/cragCastleBigPreview.dds",
        "target": "ba_data/textures/cragCastleBigPreview.dds"
    },
    "cragCastleLevelCollideBig.cob": {
        "md5": "5981bafc0a936e779c0e668af6739327",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/cragcastleMap/cragCastleLevelCollideBig.cob",
        "target": "ba_data/models/cragCastleLevelCollideBig.cob"
    },

    # dreamland map
    "dreamlandMapColor.dds": {
        "md5": "bda203e2cfe909878652727ab2f210b1",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMapColor.dds",
        "target": "ba_data/textures/dreamlandMapColor.dds"
    },
    "dreamlandMapNPreview.ktx": {
        "md5": "a3b4332a4746b38cc537d67260cebc27",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMapNPreview.ktx",
        "target": "ba_data/textures/dreamlandMapNPreview.ktx"
    },
    "dreamlandMapBottomCob.cob": {
        "md5": "34fbf6c50e8ca999abb16d424d89fde8",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMapBottomCob.cob",
        "target": "ba_data/models/dreamlandMapBottomCob.cob"
    },
    "dreamlandMapPreview.ktx": {
        "md5": "994a4fd3f9225876e8b7136150e34bab",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMapPreview.ktx",
        "target": "ba_data/textures/dreamlandMapPreview.ktx"
    },
    "dreamlandMapPreview.dds": {
        "md5": "f58dbc7c8ccc68e7f157d8728192584f",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMapPreview.dds",
        "target": "ba_data/textures/dreamlandMapPreview.dds"
    },
    "dreamlandMapCob.cob": {
        "md5": "2c08f895e2792185092842f6099b80b9",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMapCob.cob",
        "target": "ba_data/models/dreamlandMapCob.cob"
    },
    "dreamlandMapColor.ktx": {
        "md5": "05314980d146b6fcebb46d57a6b7719c",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMapColor.ktx",
        "target": "ba_data/textures/dreamlandMapColor.ktx"
    },
    "dreamlandMapNPreview.dds": {
        "md5": "373683cae6db67f8652dc3ef7ccab59d",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMapNPreview.dds",
        "target": "ba_data/textures/dreamlandMapNPreview.dds"
    },
    "uknucklesBGColor.ktx": {
        "md5": "6556f72533b6e9c8ee0836a0c0c1a0fc",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/uknucklesBGColor.ktx",
        "target": "ba_data/textures/uknucklesBGColor.ktx"
    },
    "dreamlandMapBottom.bob": {
        "md5": "58a31fe6c07a42e25cb77d4c182dbf68",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMapBottom.bob",
        "target": "ba_data/models/dreamlandMapBottom.bob"
    },
    "uknucklesBGColor.dds": {
        "md5": "6850d4a1cf9018a9ca43a2ca07fb8bec",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/uknucklesBGColor.dds",
        "target": "ba_data/textures/uknucklesBGColor.dds"
    },
    "dreamlandMap.bob": {
        "md5": "0884957ab480c97f36652d082d280f96",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/dreamlandMap/dreamlandMap.bob",
        "target": "ba_data/models/dreamlandMap.bob"
    },

    # elimination chamber raw
    "ecMapColor.dds": {
        "md5": "0d7345db0bda49b6d2ab80d5e1b71f0b",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecMapColor.dds",
        "target": "ba_data/textures/ecMapColor.dds"
    },
    "ecBGMap.bob": {
        "md5": "a5bd0d85133a86c06bf74a6bbfdc1c34",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecBGMap.bob",
        "target": "ba_data/models/ecBGMap.bob"
    },
    "ecGlassMapCob.cob": {
        "md5": "755b6838f3d4bbfe0447659878b437d5",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecGlassMapCob.cob",
        "target": "ba_data/models/ecGlassMapCob.cob"
    },
    "ecRawMapPreview.dds": {
        "md5": "160cdf0558238e15de168a3ec178da89",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecRawMapPreview.dds",
        "target": "ba_data/textures/ecRawMapPreview.dds"
    },
    "ecRawNLMap.bob": {
        "md5": "1616ad9e25600473cdb75954aaa3037a",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecRawNLMap.bob",
        "target": "ba_data/models/ecRawNLMap.bob"
    },
    "ecRawMapPreview.ktx": {
        "md5": "2096ea7ccc79b5634b210b67fa4f254d",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecRawMapPreview.ktx",
        "target": "ba_data/textures/ecRawMapPreview.ktx"
    },
    "ecRawInvMap.bob": {
        "md5": "54a556e9e62c185c03c65acb41e4b31d",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecRawInvMap.bob",
        "target": "ba_data/models/ecRawInvMap.bob"
    },
    "ecMapColor.ktx": {
        "md5": "01e33af58c380fef2b840ed9ce23073b",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecMapColor.ktx",
        "target": "ba_data/textures/ecMapColor.ktx"
    },
    "ecMapCob.cob": {
        "md5": "86d05e5a6a2c7ee168372a5779961051",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecMapCob.cob",
        "target": "ba_data/models/ecMapCob.cob"
    },
    "ecRawMap.bob": {
        "md5": "8fc840ea238849d53f761a0a2ddd7d20",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecRawMap.bob",
        "target": "ba_data/models/ecRawMap.bob"
    },
    "ecExtMap.bob": {
        "md5": "224b883703dc352fd550a8139e650c51",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecExtMap.bob",
        "target": "ba_data/models/ecExtMap.bob"
    },
    "ecRawGlassMap.bob": {
        "md5": "3f943556b4f9691c5ca182ee394735cc",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecRawGlassMap.bob",
        "target": "ba_data/models/ecRawGlassMap.bob"
    },
    "ecExtMapCob.cob": {
        "md5": "389a191ae68cabcc63886f05cec4c2d0",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberRaw/ecExtMapCob.cob",
        "target": "ba_data/models/ecExtMapCob.cob"
    },

    # elimination chamber sd
    "ecSDMap.bob": {
        "md5": "0a1cafe8222ceb919243d6bd2e328dc9",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecSDMap.bob",
        "target": "ba_data/models/ecSDMap.bob"
    },
    "ecSDMapPreview.ktx": {
        "md5": "5591a97277653d35effdf86c5b948dda",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecSDMapPreview.ktx",
        "target": "ba_data/textures/ecSDMapPreview.ktx"
    },
    "ecMapColor.dds": {
        "md5": "0d7345db0bda49b6d2ab80d5e1b71f0b",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecMapColor.dds",
        "target": "ba_data/textures/ecMapColor.dds"
    },
    "ecBGMap.bob": {
        "md5": "a5bd0d85133a86c06bf74a6bbfdc1c34",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecBGMap.bob",
        "target": "ba_data/models/ecBGMap.bob"
    },
    "ecGlassMapCob.cob": {
        "md5": "755b6838f3d4bbfe0447659878b437d5",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecGlassMapCob.cob",
        "target": "ba_data/models/ecGlassMapCob.cob"
    },
    "ecMapColor.ktx": {
        "md5": "01e33af58c380fef2b840ed9ce23073b",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecMapColor.ktx",
        "target": "ba_data/textures/ecMapColor.ktx"
    },
    "ecMapCob.cob": {
        "md5": "86d05e5a6a2c7ee168372a5779961051",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecMapCob.cob",
        "target": "ba_data/models/ecMapCob.cob"
    },
    "ecSDMapPreview.dds": {
        "md5": "09669b93fefbeca963cea00bf84ac95d",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecSDMapPreview.dds",
        "target": "ba_data/textures/ecSDMapPreview.dds"
    },
    "ecSDNLMap.bob": {
        "md5": "6e68e754cfc213b492c7e26fb673d9bd",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecSDNLMap.bob",
        "target": "ba_data/models/ecSDNLMap.bob"
    },
    "ecExtMap.bob": {
        "md5": "224b883703dc352fd550a8139e650c51",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecExtMap.bob",
        "target": "ba_data/models/ecExtMap.bob"
    },
    "ecSDInvMap.bob": {
        "md5": "a7842a820221353f9bedddbd335cc696",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecSDInvMap.bob",
        "target": "ba_data/models/ecSDInvMap.bob"
    },
    "ecSDGlassMap.bob": {
        "md5": "a9b01db08d5a5df894b51614c7399710",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecSDGlassMap.bob",
        "target": "ba_data/models/ecSDGlassMap.bob"
    },
    "ecExtMapCob.cob": {
        "md5": "389a191ae68cabcc63886f05cec4c2d0",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/eliminationChamberSD/ecExtMapCob.cob",
        "target": "ba_data/models/ecExtMapCob.cob"
    },

    # gotcha map
    "gotchaMapColor.dds": {
        "md5": "9dbc9cf5f2e8ea488102ba75253b4c8a",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gotchaMap/gotchaMapColor.dds",
        "target": "ba_data/textures/gotchaMapColor.dds"
    },
    "gotchaMap.bob": {
        "md5": "3415e902a77ffa579fd825da877c51f2",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gotchaMap/gotchaMap.bob",
        "target": "ba_data/models/gotchaMap.bob"
    },
    "gotchaMapColor.ktx": {
        "md5": "f8ff1a19e1f994572ec7fe0b53098d74",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gotchaMap/gotchaMapColor.ktx",
        "target": "ba_data/textures/gotchaMapColor.ktx"
    },
    "gotchaMapRailing.cob": {
        "md5": "4e99322da9ffb84a95acfdc451f67750",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gotchaMap/gotchaMapRailing.cob",
        "target": "ba_data/models/gotchaMapRailing.cob"
    },
    "gotchaMapBG.bob": {
        "md5": "1903f42c0edc8403c9d1fbfb10a9cf7d",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gotchaMap/gotchaMapBG.bob",
        "target": "ba_data/models/gotchaMapBG.bob"
    },
    "gotchaMapCob.cob": {
        "md5": "4196e66d85f35ae5ec3fe4004a2ef3f9",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gotchaMap/gotchaMapCob.cob",
        "target": "ba_data/models/gotchaMapCob.cob"
    },
    "gotchaMapPreview.ktx": {
        "md5": "f17bc3d3eb68c43eec28e4ea20097810",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gotchaMap/gotchaMapPreview.ktx",
        "target": "ba_data/textures/gotchaMapPreview.ktx"
    },
    "gotchaMapPreview.dds": {
        "md5": "20cf9237d3f49fa65f8790e832cd5342",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gotchaMap/gotchaMapPreview.dds",
        "target": "ba_data/textures/gotchaMapPreview.dds"
    },

    # gravity falls map
    "gravityFallsMap.bob": {
        "md5": "8835ac3225f7f79fd239d55968f52dc1",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gravityFallsMap/gravityFallsMap.bob",
        "target": "ba_data/models/gravityFallsMap.bob"
    },
    "gravityFallsMapCob.cob": {
        "md5": "eab0568aff3978e0c79bcc0b4e5d4462",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gravityFallsMap/gravityFallsMapCob.cob",
        "target": "ba_data/models/gravityFallsMapCob.cob"
    },
    "gravityFallsMapD.bob": {
        "md5": "d280b120b35af472e163a4d7a054c2aa",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gravityFallsMap/gravityFallsMapD.bob",
        "target": "ba_data/models/gravityFallsMapD.bob"
    },
    "gravityFallsMapColor.ktx": {
        "md5": "0cfddb31c4c4834d982b56e33e6b6e1b",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gravityFallsMap/gravityFallsMapColor.ktx",
        "target": "ba_data/textures/gravityFallsMapColor.ktx"
    },
    "gravityFallsMapPreview.dds": {
        "md5": "8d1be1942ef3f01b90ee2932ac757151",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gravityFallsMap/gravityFallsMapPreview.dds",
        "target": "ba_data/textures/gravityFallsMapPreview.dds"
    },
    "gravityFallsMapColor.dds": {
        "md5": "adfc0b76353a860bc8352d709c4f116a",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gravityFallsMap/gravityFallsMapColor.dds",
        "target": "ba_data/textures/gravityFallsMapColor.dds"
    },
    "gravityFallsMapPreview.ktx": {
        "md5": "b225a5dac315a2c9e68b444659f0bc64",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/gravityFallsMap/gravityFallsMapPreview.ktx",
        "target": "ba_data/textures/gravityFallsMapPreview.ktx"
    },

    # guardian map
    "skyGlassBG.ktx": {
        "md5": "d0e0dcbcdc1a1a0ac2ee135a3deabd44",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/guardianMap/skyGlassBG.ktx",
        "target": "ba_data/textures/skyGlassBG.ktx"
    },
    "guardianMapCob.cob": {
        "md5": "648a46324ddb883ab66ee9e1f5578fb1",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/guardianMap/guardianMapCob.cob",
        "target": "ba_data/models/guardianMapCob.cob"
    },
    "guardianMapPreview.dds": {
        "md5": "6c93e078f2267f1fad9b893c5c27a9c0",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/guardianMap/guardianMapPreview.dds",
        "target": "ba_data/textures/guardianMapPreview.dds"
    },
    "guardianMap.bob": {
        "md5": "862cb7c9c1aa9bc02e343e82a2f32887",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/guardianMap/guardianMap.bob",
        "target": "ba_data/models/guardianMap.bob"
    },
    "guardianMapColor.ktx": {
        "md5": "ba9cf86e182e621e06e6b70b304b6eb2",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/guardianMap/guardianMapColor.ktx",
        "target": "ba_data/textures/guardianMapColor.ktx"
    },
    "guardianMapColor.dds": {
        "md5": "7f0b6ca414ae3b28aabc33994acf9f27",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/guardianMap/guardianMapColor.dds",
        "target": "ba_data/textures/guardianMapColor.dds"
    },
    "skyGlassBG.dds": {
        "md5": "3ec0945c5c188ec7d4989020fc414eb6",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/guardianMap/skyGlassBG.dds",
        "target": "ba_data/textures/skyGlassBG.dds"
    },
    "guardianMapPreview.ktx": {
        "md5": "7ac123c93e088f5df3f5f7738d9af421",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/guardianMap/guardianMapPreview.ktx",
        "target": "ba_data/textures/guardianMapPreview.ktx"
    },

    # halloween map
    "hwMap.bob": {
        "md5": "bcd81762eaae80061dfe8655b3e779be",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/hwMap/hwMap.bob",
        "target": "ba_data/models/hwMap.bob"
    },
    "hwMapColor.ktx": {
        "md5": "f51257bf0ceb9a86fd604475a99ff197",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/hwMap/hwMapColor.ktx",
        "target": "ba_data/textures/hwMapColor.ktx"
    },
    "hwMapCob.cob": {
        "md5": "85c3a8957a74b4ec01686ce763a62787",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/hwMap/hwMapCob.cob",
        "target": "ba_data/models/hwMapCob.cob"
    },
    "hwMapPreview.dds": {
        "md5": "42fdcfb32000277ab05ab59ae26c6ffc",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/hwMap/hwMapPreview.dds",
        "target": "ba_data/textures/hwMapPreview.dds"
    },
    "hwMapColor.dds": {
        "md5": "c54b4d09c9e3b9fab95f8ce1fc0ee62d",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/hwMap/hwMapColor.dds",
        "target": "ba_data/textures/hwMapColor.dds"
    },
    "hwMapPreview.ktx": {
        "md5": "d2b1daeb416f96907c65c5cd0518fdb9",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/hwMap/hwMapPreview.ktx",
        "target": "ba_data/textures/hwMapPreview.ktx"
    },

    # ice map
    "iceMapColor.dds": {
        "md5": "61dadb6e68eab0e69abcb891500aa0d5",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapColor.dds",
        "target": "ba_data/textures/iceMapColor.dds"
    },
    "iceMapTopCob.cob": {
        "md5": "420edc2422d4a75253d1d372718eaa92",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapTopCob.cob",
        "target": "ba_data/models/iceMapTopCob.cob"
    },
    "iceMapTop.bob": {
        "md5": "1c2afc3f7b17d1e788150945fb19af7c",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapTop.bob",
        "target": "ba_data/models/iceMapTop.bob"
    },
    "iceMapPreview.ktx": {
        "md5": "39146f2246341c7036d044bb54fdb788",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapPreview.ktx",
        "target": "ba_data/textures/iceMapPreview.ktx"
    },
    "iceMapIce.bob": {
        "md5": "b89807481e96f854b97b37f38709831d",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapIce.bob",
        "target": "ba_data/models/iceMapIce.bob"
    },
    "natureBackgroundNColor.dds": {
        "md5": "2a0e93248cd284ec5875c2fd005ca8e3",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/natureBackgroundNColor.dds",
        "target": "ba_data/textures/natureBackgroundNColor.dds"
    },
    "iceMapPreview.dds": {
        "md5": "d874e09943d502b689e92a3c32bfe3cc",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapPreview.dds",
        "target": "ba_data/textures/iceMapPreview.dds"
    },
    "iceMapBottom.bob": {
        "md5": "c61b7d717399565a6320a3278da9b827",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapBottom.bob",
        "target": "ba_data/models/iceMapBottom.bob"
    },
    "iceMapIceCob.cob": {
        "md5": "6b1ab014d59932666e59923132b658ca",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapIceCob.cob",
        "target": "ba_data/models/iceMapIceCob.cob"
    },
    "iceMapColor.ktx": {
        "md5": "29cca7526a8c928505913e89d8e6136b",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapColor.ktx",
        "target": "ba_data/textures/iceMapColor.ktx"
    },
    "iceMapBottomCob.cob": {
        "md5": "76185914f2f3a86771d4781116ec4933",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/iceMapBottomCob.cob",
        "target": "ba_data/models/iceMapBottomCob.cob"
    },
    "natureBackgroundNColor.ktx": {
        "md5": "e00ec03bee7ad98e704cc361ed11882f",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/iceMap/natureBackgroundNColor.ktx",
        "target": "ba_data/textures/natureBackgroundNColor.ktx"
    },

    # krusty krab map
    "krustyKrabBGMapColor.ktx": {
        "md5": "33715489d4cc5754d2e91521df0be6f4",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/krustyKrabMap/krustyKrabBGMapColor.ktx",
        "target": "ba_data/textures/krustyKrabBGMapColor.ktx"
    },
    "krustyKrabMap.bob": {
        "md5": "4c46a9d561c5dced7aed232c72dfcc05",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/krustyKrabMap/krustyKrabMap.bob",
        "target": "ba_data/models/krustyKrabMap.bob"
    },
    "krustyKrabBGMapColor.dds": {
        "md5": "2b461c1f4156c489220fad1100cd909b",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/krustyKrabMap/krustyKrabBGMapColor.dds",
        "target": "ba_data/textures/krustyKrabBGMapColor.dds"
    },
    "krustyKrabMapColor.ktx": {
        "md5": "4574504d09c683871c7ad36b55a80f7e",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/krustyKrabMap/krustyKrabMapColor.ktx",
        "target": "ba_data/textures/krustyKrabMapColor.ktx"
    },
    "krustyKrabBGMap.bob": {
        "md5": "85f20afe5b8d6b8dd6c1b668d26ab3b3",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/krustyKrabMap/krustyKrabBGMap.bob",
        "target": "ba_data/models/krustyKrabBGMap.bob"
    },
    "krustyKrabMapPreview.ktx": {
        "md5": "fdb37b5db63f2018c55fd72a9e98009e",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/krustyKrabMap/krustyKrabMapPreview.ktx",
        "target": "ba_data/textures/krustyKrabMapPreview.ktx"
    },
    "krustyKrabMapPreview.dds": {
        "md5": "171854a77bf1ae688cc6d3f5d01d4114",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/krustyKrabMap/krustyKrabMapPreview.dds",
        "target": "ba_data/textures/krustyKrabMapPreview.dds"
    },
    "krustyKrabMapColor.dds": {
        "md5": "ce0a8641a8ecd248ffd6b03f1e606638",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/krustyKrabMap/krustyKrabMapColor.dds",
        "target": "ba_data/textures/krustyKrabMapColor.dds"
    },
    "krustyKrabMapCob.cob": {
        "md5": "d5087aa84f1aff77302d9da64d59a049",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/krustyKrabMap/krustyKrabMapCob.cob",
        "target": "ba_data/models/krustyKrabMapCob.cob"
    },

    # picnic map
    "mapPicnicPreview.ktx": {
        "md5": "77b8b0ac74f0cdd05f81bb7024f120dc",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mapPicnic/mapPicnicPreview.ktx",
        "target": "ba_data/textures/mapPicnicPreview.ktx"
    },
    "mapPicnic.bob": {
        "md5": "7d5f423039ff8158ee66c8238b4d5ef8",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mapPicnic/mapPicnic.bob",
        "target": "ba_data/models/mapPicnic.bob"
    },
    "mapPicnicCob.cob": {
        "md5": "0f6de05dbfeb0ed5b32ec14fbdbc8c4a",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mapPicnic/mapPicnicCob.cob",
        "target": "ba_data/models/mapPicnicCob.cob"
    },
    "mapPicnicDeathCob.cob": {
        "md5": "4ca617e5900561452e2a1451e61f596a",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mapPicnic/mapPicnicDeathCob.cob",
        "target": "ba_data/models/mapPicnicDeathCob.cob"
    },
    "mapPicnicTransparent.bob": {
        "md5": "8590631c1a0e40a549c955541ece7375",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mapPicnic/mapPicnicTransparent.bob",
        "target": "ba_data/models/mapPicnicTransparent.bob"
    },
    "mapPicnicColor.ktx": {
        "md5": "8d680a695c4b3c646a1d868e448e5f08",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mapPicnic/mapPicnicColor.ktx",
        "target": "ba_data/textures/mapPicnicColor.ktx"
    },
    "mapPicnicTransparentCob.cob": {
        "md5": "fce6f383c3e1c123577f584edb1395cd",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mapPicnic/mapPicnicTransparentCob.cob",
        "target": "ba_data/models/mapPicnicTransparentCob.cob"
    },
    "mapPicnicColor.dds": {
        "md5": "5819ab98ba94437477162044ee2a7b8f",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mapPicnic/mapPicnicColor.dds",
        "target": "ba_data/textures/mapPicnicColor.dds"
    },
    "mapPicnicPreview.dds": {
        "md5": "2c843812693868eaaa3b675650cf4f9c",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mapPicnic/mapPicnicPreview.dds",
        "target": "ba_data/textures/mapPicnicPreview.dds"
    },

    # mario world map
    "mbwMapPreview.dds": {
        "md5": "6c6d7062799de2b898a2c674e3ffb314",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mbwMap/mbwMapPreview.dds",
        "target": "ba_data/textures/mbwMapPreview.dds"
    },
    "mbw.bob": {
        "md5": "9e691e5f440fda84ca62337d39e55fba",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mbwMap/mbw.bob",
        "target": "ba_data/models/mbw.bob"
    },
    "mbwColor.ktx": {
        "md5": "5278e9c816df915c26ade9e8385689ed",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mbwMap/mbwColor.ktx",
        "target": "ba_data/textures/mbwColor.ktx"
    },
    "mbwMapPreview.ktx": {
        "md5": "77b9229478fce80db42a095eb8006b41",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mbwMap/mbwMapPreview.ktx",
        "target": "ba_data/textures/mbwMapPreview.ktx"
    },
    "mbwCob.cob": {
        "md5": "2d043b3b0f79d8702db2a4e2c4207895",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mbwMap/mbwCob.cob",
        "target": "ba_data/models/mbwCob.cob"
    },
    "mbwColor.dds": {
        "md5": "cf23e23848984494b2bf66e72687a5ff",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/mbwMap/mbwColor.dds",
        "target": "ba_data/textures/mbwColor.dds"
    },

    # pacman map
    "pacmanMapPreview.dds": {
        "md5": "b5b99904392f574f7f799e8d64c3b7c6",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/pacmanMap/pacmanMapPreview.dds",
        "target": "ba_data/textures/pacmanMapPreview.dds"
    },
    "pacmanMap.bob": {
        "md5": "c3123b22e06547968b6ec5d6c6986a0f",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/pacmanMap/pacmanMap.bob",
        "target": "ba_data/models/pacmanMap.bob"
    },
    "pacmanMapColor.ktx": {
        "md5": "4c622b279250158afcfe9137a8d8b11a",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/pacmanMap/pacmanMapColor.ktx",
        "target": "ba_data/textures/pacmanMapColor.ktx"
    },
    "pacmanMapColor.dds": {
        "md5": "4c797309320a6d8e6426ae5534e7a140",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/pacmanMap/pacmanMapColor.dds",
        "target": "ba_data/textures/pacmanMapColor.dds"
    },
    "pacmanMapPreview.ktx": {
        "md5": "1c2bf698b76cd05157b75d14cd84d6ac",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/pacmanMap/pacmanMapPreview.ktx",
        "target": "ba_data/textures/pacmanMapPreview.ktx"
    },
    "pacmanMapCob.cob": {
        "md5": "47843aac9f607568e9cb087302984088",
        "url": "https://raw.githubusercontent.com/JinxBs/BombSquad-Community-Plugin-Manager/main/Maps/pacmanMap/pacmanMapCob.cob",
        "target": "ba_data/models/pacmanMapCob.cob"
    },

    # geom map
    "geomArcoMap.bob": {
        "md5": "37dbfb68c13bbeeba708e4b6039f8f12",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomArcoMap.bob?raw=true",
        "target": "ba_data/models/geomArcoMap.bob"
    },
    "geomExtraMap.bob": {
        "md5": "29ec1b79df4c66bb79c61b42305e1be5",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomExtraMap.bob?raw=true",
        "target": "ba_data/models/geomExtraMap.bob"
    },
    "geomMap.bob": {
        "md5": "1229805f9511ce739badd87da1b7dae9",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMap.bob?raw=true",
        "target": "ba_data/models/geomMap.bob"
    },
    "geomMapBG.bob": {
        "md5": "84a5bcd0405b1c8f03634af6f5ee2bb6",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMapBG.bob?raw=true",
        "target": "ba_data/models/geomMapBG.bob"
    },
    "geomMapBGColor.dds": {
        "md5": "9f5cfdb9ade877c3557308d467d6fa74",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMapBGColor.dds?raw=true",
        "target": "ba_data/textures/geomMapBGColor.dds"
    },
    "geomMapBGColor.ktx": {
        "md5": "2de2a3390e3ddea36178f8197ffefabb",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMapBGColor.ktx?raw=true",
        "target": "ba_data/textures/geomMapBGColor.ktx"
    },
    "geomMapColor.dds": {
        "md5": "3b64295efd44a3ee5dc6ec0606aa43dc",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMapColor.dds?raw=true",
        "target": "ba_data/textures/geomMapColor.dds"
    },
    "geomMapColor.ktx": {
        "md5": "09c37e28d613112977b9de01d548354c",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMapColor.ktx?raw=true",
        "target": "ba_data/textures/geomMapColor.ktx"
    },
    "geomMapDeathCob.cob": {
        "md5": "f6cfb43bccc522c461dd700cfd41ee57",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMapDeathCob.cob?raw=true",
        "target": "ba_data/models/geomMapDeathCob.cob"
    },
    "geomMapPreview.dds": {
        "md5": "7f6feb2c7c413cc572c987e37d2b3147",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMapPreview.dds?raw=true",
        "target": "ba_data/textures/geomMapPreview.dds"
    },
    "geomMapPreview.ktx": {
        "md5": "bdf84c5f279e9fce5b6beac924bc09bf",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMapPreview.ktx?raw=true",
        "target": "ba_data/textures/geomMapPreview.ktx"
    },
    "geomMapCob.cob": {
        "md5": "ac62d729bb62bb98081c816814e390d3",
        "url": "https://github.com/Freaku17/BombSquad-Mods-byFreaku/blob/main/Maps/Geometry2D/geomMapCob.cob?raw=true",
        "target": "ba_data/models/geomMapCob.cob"
    },

    # lava map
    "washMap.bob": {
        "md5": "f6d1537b7a4a6c4ae2ed258d44ba51a0",
        "url": "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/LavaMap/washMap.bob",
        "target": "ba_data/models/washMap.bob"
    },
    "washMapBG.bob": {
        "md5": "7943b3d5133742aad663d96404e8b6ff",
        "url": "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/LavaMap/washMapBG.bob",
        "target": "ba_data/models/washMapBG.bob"
    },
    "washMapCob.cob": {
        "md5": "e7b32899e5a2517dc8e4616ea38a48ea",
        "url": "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/LavaMap/washMapCob.cob",
        "target": "ba_data/models/washMapCob.cob"
    },
    "washMapColor.dds": {
        "md5": "ba2ff0a35404e591e4bada4eada7fb80",
        "url": "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/LavaMap/washMapColor.dds",
        "target": "ba_data/textures/washMapColor.dds"
    },
    "washMapColor.ktx": {
        "md5": "1340f62ffcd0385045894d2513d67969",
        "url": "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/LavaMap/washMapColor.ktx",
        "target": "ba_data/textures/washMapColor.ktx"
    },
    "washMapDeath.bob": {
        "md5": "6731144ddfc55b08c03c3c48462e7df0",
        "url": "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/LavaMap/washMapDeath.bob",
        "target": "ba_data/models/washMapDeath.bob"
    },
    "washMapDeathCob.cob": {
        "md5": "70daadd2374198bd5d71dadc1828c96b",
        "url": "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/LavaMap/washMapDeathCob.cob",
        "target": "ba_data/models/washMapDeathCob.cob"
    },
    "washMapPreview.ktx": {
        "md5": "35090e1fad9b5344ca152312d51bb65d",
        "url": "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/LavaMap/washMapPreview.ktx",
        "target": "ba_data/textures/washMapPreview.ktx"
    },
    "washMapPreview.dds": {
        "md5": "91bc3dccd1cbf95c6ddf75702024a991",
        "url": "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/LavaMap/washMapPreview.dds",
        "target": "ba_data/textures/washMapPreview.dds"
    }
}


def Install_msg():
    ba.screenmessage(f"Installing: {package_name}", color=(1, 1, 0))

def Update_msg():
    ba.screenmessage(f"Updating: {package_name}", color=(1,1,0))

def Update_success():
    ba.screenmessage(f"Update Success, please restart game :)", color=(1,1,0))

class PackInstaller:
    def __init__(self, name, package_files):
        self.name = name
        self.package_files = package_files
        self.give_update_popup = False
        self.give_update_success = False
        if self._installed():
            threading.Thread(target=self.check_update).start()
            ba.timer(3, self.get_update_clue)
            ba.timer(5, self.update_success_clue)
            return
        try:
            ba.timer(1, Install_msg)
            download = threading.Thread(target=self.download)
            download.start()
        except:
            ba.print_exception()

    def check_update(self):
        check_url = "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/allMapsInOne/url_version.txt"
        try:
            response = urllib.request.urlopen(check_url)
            if response.getcode() == 200:
                ur_version = response.read().decode()
        except Exception as e:
            print(e)
            ur_version = my_version
        if int(ur_version) > my_version:
            self.give_update_popup = True
            self.updateit()
        else: return

    def updateit(self):
        update_url = "https://raw.githubusercontent.com/Freaku17/BombSquad-Mods-byFreaku/main/Maps/allMapsInOne/allMapsInOne.py"
        updated_file = ""
        try:
            response = urllib.request.urlopen(update_url)
            if response.getcode() == 200:
                updated_file = response.read().decode()
            with open(file_location, 'w+') as f:
                f.write(updated_file)
                f.close()
            self.give_update_success = True
        except Exception as e:
            print(e)

    def get_update_clue(self):
        if self.give_update_popup: Update_msg()

    def update_success_clue(self):
        if self.give_update_success: Update_success()

    def _get_md5(self, file):
        with open(file, 'rb') as f:
            data = f.read()
            return md5(data).hexdigest()

    def _installed(self):
        for info in self.package_files.values():
            if not os.path.exists(info['target']):
                return False
            if check_md5:
                if self._get_md5(info['target']) != info['md5']:
                    return False
        return True

    def download(self):
        for info in self.package_files.values():

            # download only if file isnt present
            if os.path.exists(info['target']) and self._get_md5(info['target']) == info['md5']:
                continue
            request = info['url']
            try:
                response = urllib.request.urlopen(request)
                if response.getcode() == 200:
                    data = response.read()
                    with open(info['target'], 'wb') as f:
                        f.write(data)
            except:
                ba.print_exception()

class geomMapDefs:
# This file was automatically generated from "alwaysLandLevel.ma"
    points= {}
    boxes = {}
    points['ffa_spawn1'] = (-12.0422, 14.94395, -5.44451) + (1.55584, 0.05, 0.11656)
    points['ffa_spawn2'] = (8.44448, 14.94068, -5.61448) + (1.55386, 0.05, 0.0442)
    points['ffa_spawn3'] = (-7.23133, 12.23867, -5.61448) + (1.33793, 0.05, 0.0442)
    points['ffa_spawn4'] = (3.96227, 12.25704, -5.61448) + (1.33793, 0.05, 0.0442)
    points['ffa_spawn5'] = (-12.97798, 7.37773, -5.61448) + (0.90462, 0.05, 0.0442)
    points['ffa_spawn6'] = (5.83325, 7.69005, -5.52167) + (0.97071, 0.05, 0.00758)
    points['flag1'] = (-13.02317, 7.59685, -5.52)
    points['flag2'] = (10.71013, 6.72526, -5.52)
    points['flag3'] = (-12.12348, 15.19512, -5.52)
    points['flag4'] = (8.56178, 15.09921, -5.52)
    points['flag_default'] = (-1.91162, 10.61648, -5.52)
    points['powerup_spawn1'] = (-13.62341, 15.21751, -5.46911)
    points['powerup_spawn2'] = (10.21625, 15.23359, -5.50572)
    points['powerup_spawn3'] = (-7.79082, 6.81023, -5.57623)
    points['powerup_spawn4'] = (0.64672, 6.66186, -5.57623)
    points['spawn1'] = (-12.96446, 7.35024, -5.44451) + (0.92773, 0.05, 0.11656)
    points['spawn2'] = (10.77293, 6.6801, -5.61448) + (0.81303, 0.05, 0.0442)
    points['spawn_by_flag1'] = (-13.01779, 7.34912, -5.44451) + (0.80423, 0.05, 0.11656)
    points['spawn_by_flag2'] = (10.76989, 6.67741, -5.61448) + (0.70346, 0.05, 0.0442)
    points['spawn_by_flag3'] = (-12.23744, 14.93243, -5.53528) + (0.95164, 0.05, 0.08607)
    points['spawn_by_flag4'] = (8.6825, 14.95201, -5.59898) + (0.69982, 0.05, 0.01941)
    boxes['area_of_interest_bounds'] = (-1.04586, 12.67723, -5.40154) + (0, 0, 0) + (34.46157, 20.94045, 0.69316)
    boxes['map_bounds'] = (-0.87483, 9.21294, -5.72954) + (0, 0, 0) + (36.09666, 26.1995, 7.89541)

class GeomMap(ba.Map):
    defs = geomMapDefs()
    name = 'Geometrical Dominator'

    @classmethod
    def get_play_types(cls) -> List[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'conquest', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'geomMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: Dict[str, Any] = {
            'model': ba.getmodel('geomMap'),
            'model_arco': ba.getmodel('geomArcoMap'),
            'model_extra': ba.getmodel('geomExtraMap'),
            'collide_model': ba.getcollidemodel('geomMapCob'),
            'collide_death': ba.getcollidemodel('geomMapDeathCob'),
            'tex': ba.gettexture('geomMapColor'),
            'bg_tex': ba.gettexture('geomMapBGColor'),
            'bg_model': ba.getmodel('alwaysLandBG'),
            'bg_model2': ba.getmodel('geomMapBG'),
            'bg_material': ba.Material()
        }
        data['bg_material'].add_actions(actions=('modify_part_collision',
                                                 'friction', 10.0))
        return data

    @classmethod
    def get_music_type(cls) -> ba.MusicType:
        return ba.MusicType.FLYING

    def __init__(self) -> None:
        super().__init__(vr_overlay_offset=(0, -3.7, 2.5))
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.nodeArco = ba.newnode('terrain', delegate=self, attrs={
                                     'model': self.preloaddata['model_arco'],
                                     'lighting': False,
                                     'color_texture': self.preloaddata['tex']
                                 })
        self.nodeExtra = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'model': self.preloaddata['model_extra'],
                'lighting': False,
                'color_texture': self.preloaddata['tex']
            })
        self.death = ba.newnode('terrain', delegate=self, attrs={
            'collide_model':self.preloaddata['collide_death'],
            'materials':[shared.footing_material, shared.death_material]})
        self.foo = ba.newnode('terrain', attrs={
            'model':self.preloaddata['bg_model'],
            'lighting':False,
            'background':True,
            'color_texture':self.preloaddata['bg_tex']})
        self.bg = ba.newnode('terrain', attrs={
            'model':self.preloaddata['bg_model2'],
            'lighting':False,
            'background':True,
            'color_texture':self.preloaddata['bg_tex']})
        gnode = ba.getactivity().globalsnode
        gnode.happy_thoughts_mode = True
        gnode.shadow_offset = (0.0, 8.0, 5.0)
        gnode.tint = (1.3, 1.23, 1.0)
        gnode.ambient_color = (1.3, 1.23, 1.0)
        gnode.vignette_outer = (0.64, 0.59, 0.69)
        gnode.vignette_inner = (0.95, 0.95, 0.93)
        gnode.vr_near_clip = 1.0
        self.is_flying = True

        # throw out some tips on flying
        txt = ba.newnode('text',
                         attrs={
                             'text': ba.Lstr(resource='pressJumpToFlyText'),
                             'scale': 1.2,
                             'maxwidth': 800,
                             'position': (0, 200),
                             'shadow': 0.5,
                             'flatness': 0.5,
                             'h_align': 'center',
                             'v_attach': 'bottom'
                         })
        cmb = ba.newnode('combine',
                         owner=txt,
                         attrs={
                             'size': 4,
                             'input0': 0.3,
                             'input1': 0.9,
                             'input2': 0.0
                         })
        ba.animate(cmb, 'input3', {3.0: 0, 4.0: 1, 9.0: 1, 10.0: 0})
        cmb.connectattr('output', txt, 'color')
        ba.timer(10.0, txt.delete)


class washMapDefs:
# pylint: disable=all
    points = {}
# noinspection PyDictCreation
    boxes = {}
    points['ffa_spawn1'] = (-0.04757, 1.09686, -3.89173) + (3.8064, 0.05, 0.44435)
    points['ffa_spawn2'] = (-0.04757, 1.08571, 3.37578) + (3.8064, 0.05, 0.44435)
    points['flag_default'] = (-0.10014, 1.44659, -0.47588)
    points['powerup_spawn1'] = (-0.30229, 1.50386, -7.7884)
    points['powerup_spawn2'] = (-7.553, 1.50386, -0.3482)
    points['powerup_spawn3'] = (-0.3006, 1.50386, 7.01017)
    points['powerup_spawn4'] = (7.23978, 1.50386, -0.35983)
    points['spawn1'] = (-3.48876, 1.09929, -0.24436) + (0.5, 0.05, 4.0)
    points['spawn2'] = (3.40264, 1.1049, -0.27694) + (0.5, 0.05, 4.0)
    boxes['area_of_interest_bounds'] = (0.0, 1.18575,0.43262) + (0.0, 0.0, 0.0) + (29.81803, 17.99181, 18.89134)
    boxes['edge_box'] = (-0.10387, 0.41333, 0.42947) + (0.0, 0.0, 0.0) + (22.48296, 1.29024, 8.99025)
    boxes['map_bounds'] = (0.0, 1.18575, 0.43262) + (0.0, 0.0, 0.0) + (42.09507, 35.46551, 29.76723)

class WashMap(ba.Map):
    defs = washMapDefs()
    name = 'Wash Map'

    @classmethod
    def get_play_types(cls) -> List[str]:
        """Return valid play types for this map."""
        return ['melee', 'king_of_the_hill', 'keep_away']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'washMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: Dict[str, Any] = {
            'model': ba.getmodel('washMap'),
            'collide_model': ba.getcollidemodel('washMapCob'),
            'model_death': ba.getmodel('washMapDeath'),
            'collide_death': ba.getcollidemodel('washMapDeathCob'),
            'tex': ba.gettexture('washMapColor'),
            'model_bg': ba.getmodel('washMapBG'),
            'bg_material': ba.Material()
        }
        data['bg_material'].add_actions(actions=('modify_part_collision',
                                                 'friction', 10.0))
        return data

    def __init__(self):
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.death = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_death'],
                'model': self.preloaddata['model_death'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material,
                              shared.death_material]
            })
        self.background = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'model': self.preloaddata['model_bg'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['tex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.1, 1.0)
        gnode.ambient_color = (1.1, 1.1, 1.0)
        gnode.vignette_outer = (0.7, 0.65, 0.75)
        gnode.vignette_inner = (0.95, 0.95, 0.93)

class ArenaminigoremapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-4.42149, 3.1618, -7.59045) + (3.13882, 0.05, 2.58941)
    points['ffa_spawn2'] = (4.89134, 3.18797, -7.59754) + (3.13385, 0.05, 2.56661)
    points['ffa_spawn3'] = (4.87849, 3.16192, 1.10463) + (3.11134, 0.05, 2.49891)
    points['ffa_spawn4'] = (-4.42791, 3.16192, 1.10463) + (3.12373, 0.05, 2.57577)
    points['flag1'] = (-8.85376, 3.08991, -3.21865)
    points['flag2'] = (9.53636, 3.14715, -3.35611)
    points['flag_default'] = (0.30888, 3.16322, -3.28703)
    points['powerup_spawn1'] = (-4.16659, 3.42372, -6.42749)
    points['powerup_spawn2'] = (4.42687, 3.48435, -6.32974)
    points['powerup_spawn3'] = (-4.20169, 3.26527, 0.44007)
    points['powerup_spawn4'] = (4.75892, 3.26527, 0.34941)
    points['spawn1'] = (-8.35908, 3.1618, -3.16719) + (0.42967, 0.05, 2.68171)
    points['spawn2'] = (8.96465, 3.18797, -3.18894) + (0.42967, 0.05, 2.68171)
    points['tnt1'] = (-7.91677, 3.55083, -10.26691)
    points['tnt2'] = (8.8223, 3.55083, -10.26691)
    points['tnt3'] = (-7.91677, 3.55083, 3.94815)
    points['tnt4'] = (8.8223, 3.55083, 3.94815)
    boxes['area_of_interest_bounds'] = (0.35634, 4.49356, -2.2642) + (0, 0, 0) + (17.33594, 12.05851, 18.50299)
    boxes['map_bounds'] = (0.25894, 4.89966, -3.79786) + (0, 0, 0) + (30.44458, 21.24073, 29.92689)


class ArenaMinigore(ba.Map):
    defs = ArenaminigoremapDefs()
    name = 'Hardland Arena'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'arenaMinigorePreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('arenaminigoreMap'),
            'collide_model': ba.getcollidemodel('arenaminigoreMapCob'),
            'tex': ba.gettexture('arenaminigoreMapColor')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.1, 1.0)
        gnode.ambient_color = (1.1, 1.1, 1.0)
        gnode.vignette_outer = (0.7, 0.65, 0.75)
        gnode.vignette_inner = (0.95, 0.95, 0.93)


class BikiniBottomDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-12.941, 0.49259, 0.40543) + (0.4868, 0.05, 1.25935)
    points['ffa_spawn2'] = (10.01692, 0.53469, -5.54644) + (2.14841, 0.05, 0.69308)
    points['ffa_spawn3'] = (12.65346, 0.5398, 0.32502) + (0.41375, 0.05, 1.32322)
    points['ffa_spawn4'] = (-9.92497, 0.54031, -5.55539) + (2.1591, 0.05, 0.65578)
    points['flag1'] = (-10.10481, 0.81866, 5.65734)
    points['flag2'] = (9.64363, 0.7631, 5.65322)
    points['flag_default'] = (0.20325, 3.43438, -4.75406)
    points['powerup_spawn1'] = (-7.33996, 0.7924, 1.15642)
    points['powerup_spawn2'] = (-2.61051, 0.7562, 1.13188)
    points['powerup_spawn3'] = (2.95595, 0.75344, 1.11008)
    points['powerup_spawn4'] = (7.01624, 0.77552, 1.14522)
    points['spawn1'] = (-9.92708, 0.52016, -5.56546) + (2.30817, 0.05, 0.69569)
    points['spawn2'] = (10.03658, 0.50706, -5.54186) + (2.35914, 0.05, 0.71615)
    points['tnt1'] = (0.0365, 0.87095, 5.72216)
    boxes['area_of_interest_bounds'] = (-0.01839, 1.30799, 0.46229) + (0, 0, 0) + (38.48324, 21.2151, 14.40626)
    boxes['map_bounds'] = (0.47584, 4.09931, 0.09103) + (0, 0, 0) + (59.82487, 27.42716, 23.30082)


class Cangremovil(ba.Actor):
    def __init__(self,
                 position: Sequence[float] = (0.0, 1.0, 0.0),
                 position2: Sequence[float] = (0.0, 1.0, 0.0),
                 time: float = 5.0):
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'prop',
            delegate=self,
            attrs={
                'position': position,
                'model': ba.getmodel('cangremovilModel'),
                'body': 'crate',
                'body_scale': 3.0,
                'density': 999999999999999999999,
                'damping': 999999999999999999999,
                'gravity_scale': 0.0,
                'reflection': 'powerup',
                'reflection_scale': [0.3],
                'color_texture': ba.gettexture('cangremovilColor'),
                'materials': [shared.footing_material]
            }
        )
        ba.animate_array(self.node,
                         'position',
                         3,
                         {0.0: position, time: position2}, loop=True)


class BikiniBottomMap(ba.Map):
    defs = BikiniBottomDefs()
    name = 'Bikini Bottom'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'bikiniBottomPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('bikiniBottomMap'),
            'collide_model': ba.getcollidemodel('bikiniBottomMapCob'),
            'tex': ba.gettexture('bikiniBottomMapColor'),
            'bgtex': ba.gettexture('bikiniBottomMapBGColor'),
            'bgmodel': ba.getmodel('bikiniBottomMapBG')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        Cangremovil(position=(-30.10481, 0.81866, 3.05734),
                    position2=(30.10481, 0.81866, 3.05734),
                    time=3.0).autoretain()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'materials': [shared.footing_material],
                'color_texture': self.preloaddata['bgtex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.1, 1.0)
        gnode.ambient_color = (1.1, 1.1, 1.0)
        gnode.vignette_outer = (0.7, 0.65, 0.75)
        gnode.vignette_inner = (0.95, 0.95, 0.93)


class BombermanDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-6.67542, 3.68439, -5.53375) + (0.36007, 0.02575, 0.9315)
    points['ffa_spawn2'] = (-7.2624, 3.71553, -0.03071) + (0.51265, 0.02934, 1.58911)
    points['ffa_spawn3'] = (7.19605, 3.71931, -5.43993) + (0.30604, 0.05, 0.97874)
    points['ffa_spawn4'] = (7.7071, 3.71969, -0.02085) + (0.48506, 0.05, 1.59702)
    points['flag1'] = (-5.53975, 4.90844, -1.29316)
    points['flag2'] = (6.03798, 4.86734, -1.2541)
    points['flag_default'] = (0.25697, 4.91175, -1.23932)
    points['powerup_spawn1'] = (-4.26423, 4.15187, -2.68368)
    points['powerup_spawn2'] = (4.7916, 4.12509, -2.73491)
    points['powerup_spawn3'] = (-4.29883, 4.12305, 0.08537)
    points['powerup_spawn4'] = (4.8075, 4.13938, 0.12609)
    points['spawn1'] = (-7.28662, 3.70478, -1.38929) + (0.51458, 0.05, 1.70728)
    points['spawn2'] = (7.72787, 3.75089, -0.76991) + (0.52971, 0.05, 2.20823)
    points['tnt1'] = (0.32876, 3.96425, -6.16745)
    boxes['area_of_interest_bounds'] = (0.64605, 8.43146, 1.88631) + (0, 0, 0) + (12.56183, 9.47264, 10.65585)
    boxes['map_bounds'] = (0.56149, 10.49611, -2.47924) + (0, 0, 0) + (22.0605, 16.68579, 17.23487)


class BombermanMap(ba.Map):
    defs = BombermanDefs()
    name = 'BombermanMap'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'bombermanMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('bombermanMap'),
            'collide_model': ba.getcollidemodel('bombermanMapCob'),
            'tex': ba.gettexture('bombermanMapColor')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.1, 1.0)
        gnode.ambient_color = (1.1, 1.1, 1.0)
        gnode.vignette_outer = (0.7, 0.65, 0.75)
        gnode.vignette_inner = (0.95, 0.95, 0.93)


class CouragemapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-6.5205, 1.13883, 4.19109) + (0.4868, 0.05, 1.25935)
    points['ffa_spawn2'] = (8.78868, 1.18093, -2.49017) + (0.69308, 0.05, 2.14841)
    points['ffa_spawn3'] = (8.22231, 1.18604, 4.1369) + (0.41375, 0.05, 1.32322)
    points['ffa_spawn4'] = (-6.39927, 1.18655, -2.2972) + (0.65578, 0.05, 2.1591)
    points['flag1'] = (-6.40246, 1.4649, -0.18825)
    points['flag2'] = (8.6688, 1.40934, -0.34307)
    points['flag_default'] = (1.10226, 1.46938, 3.37262)
    points['powerup_spawn1'] = (-2.72635, 1.43864, -2.69105)
    points['powerup_spawn2'] = (4.57531, 1.40244, -2.55269)
    points['powerup_spawn3'] = (-2.5655, 1.39968, 5.91099)
    points['powerup_spawn4'] = (4.63833, 1.42176, 5.88299)
    points['spawn1'] = (-6.43877, 1.1664, -2.26988) + (0.69569, 0.05, 2.30817)
    points['spawn2'] = (8.71112, 1.1533, -2.47063) + (0.71615, 0.05, 2.35914)
    points['tnt1'] = (-7.47936, 1.51719, 1.60992)
    points['tnt2'] = (9.08903, 1.52706, 1.56156)
    boxes['area_of_interest_bounds'] = (0.59016, 0.74947, 3.06926) + (0, 0, 0) + (16.98306, 12.80661, 14.40626)
    boxes['edge_box'] = (1.01079, 3.81195, -0.03497) + (0, 0, 0) + (9.46205, 7.07351, 5.54318)
    boxes['map_bounds'] = (0.47584, 3.54079, -2.83278) + (0, 0, 0) + (29.82487, 22.55849, 23.30082)


class CourageMap(ba.Map):
    defs = CouragemapDefs()
    name = 'Courage'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'courageMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('courageMap'),
            'collide_model': ba.getcollidemodel('courageMapCob'),
            'tex': ba.gettexture('courageMapColor'),
            'bgtex': ba.gettexture('courageBGColor'),
            'bgmodel': ba.getmodel('thePadBG')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['bgtex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (0.8, 0.9, 1.3)
        gnode.ambient_color = (0.8, 0.9, 1.3)
        gnode.vignette_outer = (0.79, 0.79, 0.69)
        gnode.vignette_inner = (0.97, 0.97, 0.99)

    def is_point_near_edge(self,
                           point: ba.Vec3,
                           running: bool = False) -> bool:
        # count anything off our ground level as safe (for our platforms)
        # see if we're within edge_box
        box_position = self.defs.boxes['edge_box'][0:3]
        box_scale = self.defs.boxes['edge_box'][6:9]
        xpos = (point.x - box_position[0]) / box_scale[0]
        zpos = (point.z - box_position[2]) / box_scale[2]
        return xpos < -0.5 or xpos > 0.5 or zpos < -0.5 or zpos > 0.5


class CragcastlemapDefs:
    # This file generated from "cragCastleBig.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-2.22659, 14.63751, 11.52419) + (1.55044, 0.03137, 0.1124)
    points['ffa_spawn2'] = (3.71513, 14.66076, 11.55282) + (1.51546, 0.03137, 0.11228)
    points['ffa_spawn3'] = (3.35989, 15.7454, 9.97398) + (1.01492, 0.03137, 0.11228)
    points['ffa_spawn4'] = (-1.9671, 15.7454, 9.97398) + (1.01492, 0.03137, 0.11228)
    points['ffa_spawn5'] = (-1.20575, 13.62445, 13.76571) + (1.01492, 0.03137, 0.11228)
    points['ffa_spawn6'] = (2.51764, 13.62445, 13.76571) + (1.01492, 0.03137, 0.11228)
    points['flag1'] = (-0.88318, 15.77746, 9.70605)
    points['flag2'] = (2.34138, 15.74996, 9.73634)
    points['flag3'] = (-4.00945, 14.59352, 13.8783)
    points['flag4'] = (5.4491, 14.59501, 13.84305)
    points['flag_default'] = (0.70381, 13.80694, 13.71932)
    points['powerup_spawn1'] = (5.27504, 14.8211, 9.98847)
    points['powerup_spawn2'] = (-0.12894, 14.84951, 9.9409)
    points['powerup_spawn3'] = (1.47447, 14.8553, 9.93446)
    points['powerup_spawn4'] = (-3.87666, 14.91756, 9.90655)
    points['spawn1'] = (-2.93425, 14.63751, 11.52419) + (0.66332, 0.03137, 0.1124)
    points['spawn2'] = (4.20019, 14.66076, 11.55282) + (0.63351, 0.03137, 0.11228)
    points['spawn_by_flag1'] = (-1.49292, 15.77746, 9.95693)
    points['spawn_by_flag2'] = (3.01471, 15.77746, 9.95693)
    points['spawn_by_flag3'] = (-3.85287, 14.61411, 13.37536)
    points['spawn_by_flag4'] = (5.2451, 14.61411, 13.37536)
    points['tnt1'] = (-2.85167, 16.18561, 9.88324)
    points['tnt2'] = (4.20036, 16.18561, 9.88324)
    boxes['area_of_interest_bounds'] = (0.75009, 14.01822, 11.76844) + (0, 0, 0) + (10.49919, 9.37717, 7.27735)
    boxes['map_bounds'] = (0.44951, 15.90257, 11.61652) + (0, 0, 0) + (14.40166, 6.21587, 8.89543)


class CragCastleBigMap(ba.Map):
    defs = CragcastlemapDefs()
    name = 'Crag Castle Big'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'conquest']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'cragCastleBigPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('cragCastleLevelBig'),
            'bottom_model': ba.getmodel('cragCastleLevelBottomBig'),
            'collide_model': ba.getcollidemodel('cragCastleLevelCollideBig'),
            'tex': ba.gettexture('cragCastleLevelColor'),
            'bgtex': ba.gettexture('menuBG'),
            'bgmodel': ba.getmodel('thePadBG'),
            'railing_collide_model':
                (ba.getcollidemodel('cragCastleLevelBumperBig')),
            'vr_fill_mound_model': ba.getmodel('cragCastleVRFillMound'),
            'vr_fill_mound_tex': ba.gettexture('vrFillMound')
        }
        # fixme should chop this into vr/non-vr sections
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.bottom = ba.newnode('terrain',
                                 attrs={
                                     'model': self.preloaddata['bottom_model'],
                                     'lighting': False,
                                     'color_texture': self.preloaddata['tex']
                                 })
        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['bgtex']
            })
        self.railing = ba.newnode(
            'terrain',
            attrs={
                'collide_model': self.preloaddata['railing_collide_model'],
                'materials': [shared.railing_material],
                'bumper': True
            })
        ba.newnode('terrain',
                   attrs={
                       'model': self.preloaddata['vr_fill_mound_model'],
                       'lighting': False,
                       'vr_only': True,
                       'color': (0.2, 0.25, 0.2),
                       'background': True,
                       'color_texture': self.preloaddata['vr_fill_mound_tex']
                   })
        gnode = ba.getactivity().globalsnode
        gnode.shadow_ortho = True
        gnode.shadow_offset = (0, 0, -5.0)
        gnode.tint = (1.15, 1.05, 0.75)
        gnode.ambient_color = (1.15, 1.05, 0.75)
        gnode.vignette_outer = (0.6, 0.65, 0.6)
        gnode.vignette_inner = (0.95, 0.95, 0.95)
        gnode.vr_near_clip = 1.0


class DreamlandmapDefs:
    # This file generated from "torneo.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-6.69624, 2.85039, -4.10288) + (0.77236, 0.05, 0.87378)
    points['ffa_spawn2'] = (-10.40827, 2.85039, -1.56054) + (0.77236, 0.05, 0.87378)
    points['ffa_spawn3'] = (-8.65731, 2.85039, 2.62386) + (0.77236, 0.05, 0.87378)
    points['ffa_spawn4'] = (-2.02022, 2.85039, 4.61688) + (0.77236, 0.05, 0.87378)
    points['ffa_spawn5'] = (1.86972, 2.85039, 4.72121) + (0.77236, 0.05, 0.87378)
    points['ffa_spawn6'] = (8.4577, 2.85039, 2.62079) + (0.77236, 0.05, 0.87378)
    points['ffa_spawn7'] = (10.39531, 2.85039, -1.52552) + (0.77236, 0.05, 0.87378)
    points['ffa_spawn8'] = (6.67172, 2.85039, -4.13483) + (0.77236, 0.05, 0.87378)
    points['flag1'] = (-11.02499, 3.17053, 0.88749)
    points['flag2'] = (11.10934, 3.17053, 0.88885)
    points['flag3'] = (-8.37111, 3.25837, -4.26217)
    points['flag4'] = (8.32579, 3.3096, -4.23468)
    points['flag5'] = (-2.36192, 3.21392, 4.21456)
    points['flag6'] = (2.24404, 3.21392, 4.31202)
    points['flag_default'] = (-0.16211, 3.663, -0.46622)
    points['powerup_spawn1'] = (-8.08751, 3.11164, -6.17346)
    points['powerup_spawn2'] = (-6.24881, 3.0105, -0.35762)
    points['powerup_spawn3'] = (-2.07277, 3.11164, 6.74271)
    points['powerup_spawn4'] = (1.84842, 3.11164, 6.75979)
    points['powerup_spawn5'] = (6.08678, 3.0105, -0.38878)
    points['powerup_spawn6'] = (8.08131, 3.11164, -6.15938)
    points['spawn1'] = (-9.46633, 2.84651, 0.25554) + (0.87378, 0.05, 1.6634)
    points['spawn2'] = (9.38817, 2.84651, 0.21746) + (0.87378, 0.05, 1.6634)
    points['spawn_by_flag1'] = (-10.01502, 2.85596, 1.81426) + (0.84416, 0.05, 0.84945)
    points['spawn_by_flag2'] = (10.15712, 3.12542, 1.82582) + (0.85053, 0.05, 0.83403)
    points['spawn_by_flag3'] = (-7.454, 2.95629, -3.34154) + (0.8398, 0.05, 0.83771)
    points['spawn_by_flag4'] = (7.38268, 2.89333, -3.31041) + (0.84957, 0.05, 0.83771)
    points['spawn_by_flag5'] = (-2.22089, 3.01925, 5.55799) + (0.8398, 0.05, 0.83771)
    points['spawn_by_flag6'] = (1.84214, 3.05073, 5.55764) + (0.83672, 0.05, 0.83771)
    points['tnt1'] = (0.0091, 3.11164, -3.65076)
    points['tnt2'] = (0.0091, 3.11164, 2.39515)
    boxes['area_of_interest_bounds'] = (0.35441, 4.49356, -2.40045) + (0, 0, 0) + (29.91755, 23.28733, 24.08552)
    boxes['map_bounds'] = (0.26088, 5.81105, -3.66161) + (0, 0, 0) + (54.98705, 41.72606, 26.50049)


class DreamlandMap(ba.Map):
    defs = DreamlandmapDefs()
    name = 'Dream Land'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill', 'conquest']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'dreamlandMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('dreamlandMap'),
            'collide_model': ba.getcollidemodel('dreamlandMapCob'),
            'modelb': ba.getmodel('dreamlandMapBottom'),
            'collide_modelb': ba.getcollidemodel('dreamlandMapBottomCob'),
            'tex': ba.gettexture('dreamlandMapColor'),
            'bgtex': ba.gettexture('uknucklesBGColor'),
            'bgmodel': ba.getmodel('thePadBG')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.nodeb = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_modelb'],
                'model': self.preloaddata['modelb'],
                'color_texture': self.preloaddata['tex'],
                'lighting': False,
                'materials': [shared.footing_material]
            })
        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['bgtex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (0.9, 0.9, 1.3)
        gnode.ambient_color = (0.8, 0.9, 1.3)
        gnode.vignette_outer = (0.79, 0.79, 0.69)
        gnode.vignette_inner = (0.97, 0.97, 0.99)


class EliminationChamberDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-5.73834, 2.80152, -8.8294) + (0.16326, 0.05, 1.17729)
    points['ffa_spawn2'] = (6.29593, 2.82769, -8.84425) + (1.17571, 0.05, 0.19976)
    points['ffa_spawn3'] = (-5.73994, 2.80164, 3.14882) + (0.1102, 0.05, 1.11355)
    points['ffa_spawn4'] = (6.28908, 2.80164, 3.1914) + (1.10532, 0.05, 0.1034)
    points['flag1'] = (-6.75103, 3.00062, -2.80413)
    points['flag2'] = (7.09391, 3.02284, -2.94835)
    points['flag_default'] = (0.27249, 4.38208, -2.93376)
    points['powerup_spawn1'] = (-6.64437, 3.08947, -6.27667)
    points['powerup_spawn2'] = (-3.48047, 3.15009, -9.86327)
    points['powerup_spawn3'] = (4.13658, 2.93102, -9.85887)
    points['powerup_spawn4'] = (7.40907, 2.93102, -6.63147)
    points['powerup_spawn5'] = (7.40355, 3.19542, 0.85875)
    points['powerup_spawn6'] = (4.10369, 3.08724, 4.3101)
    points['powerup_spawn7'] = (-3.61995, 3.09165, 4.27063)
    points['powerup_spawn8'] = (-6.81122, 3.13612, 0.9741)
    points['spawn1'] = (-5.47127, 2.70749, -0.86437) + (1.29739, 0.05, 0.87378)
    points['spawn2'] = (6.18423, 2.73365, -4.87303) + (1.3172, 0.05, 0.87378)
    boxes['area_of_interest_bounds'] = (0.35441, 2.49356, -2.51839) + (0, 0, 0) + (16.64755, 8.06139, 22.50299)
    boxes['map_bounds'] = (0.26088, 4.89966, -3.54367) + (0, 0, 0) + (29.23565, 14.19991, 29.92689)


class EliminationRawMap(ba.Map):
    defs = EliminationChamberDefs()
    name = 'Elimination Chamber - Raw'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill', 'wwe']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'ecRawMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('ecRawMap'),
            'collide_model': ba.getcollidemodel('ecMapCob'),
            'modeli': ba.getmodel('ecRawInvMap'),
            'modelnl': ba.getmodel('ecRawNLMap'),
            'modelg': ba.getmodel('ecRawGlassMap'),
            'collide_modelg': ba.getcollidemodel('ecGlassMapCob'),
            'modele': ba.getmodel('ecExtMap'),
            'collide_modele': ba.getcollidemodel('ecExtMapCob'),
            'tex': ba.gettexture('ecMapColor'),
            'bgmodel': ba.getmodel('ecBGMap')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.nodenl = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'lighting': False,
                'model': self.preloaddata['modelnl'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.nodei = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'opacity': 0.05,
                'model': self.preloaddata['modeli'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.nodeg = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_modelg'],
                'model': self.preloaddata['modelg'],
                'color_texture': self.preloaddata['tex'],
                'lighting': False,
                'opacity': 0.2,
                'materials': [shared.footing_material]
            })
        self.nodee = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_modele'],
                'model': self.preloaddata['modele'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['tex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.1, 1.0)
        gnode.ambient_color = (1.1, 1.1, 1.0)
        gnode.vignette_outer = (0.7, 0.65, 0.75)
        gnode.vignette_inner = (0.95, 0.95, 0.93)


class EliminationSDMap(ba.Map):
    defs = EliminationChamberDefs()
    name = 'Elimination Chamber - SD'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill', 'wwe']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'ecSDMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('ecSDMap'),
            'collide_model': ba.getcollidemodel('ecMapCob'),
            'modeli': ba.getmodel('ecSDInvMap'),
            'modelnl': ba.getmodel('ecSDNLMap'),
            'modelg': ba.getmodel('ecSDGlassMap'),
            'collide_modelg': ba.getcollidemodel('ecGlassMapCob'),
            'modele': ba.getmodel('ecExtMap'),
            'collide_modele': ba.getcollidemodel('ecExtMapCob'),
            'tex': ba.gettexture('ecMapColor'),
            'bgmodel': ba.getmodel('ecBGMap')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.nodenl = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'lighting': False,
                'model': self.preloaddata['modelnl'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.nodei = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'opacity': 0.05,
                'model': self.preloaddata['modeli'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.nodeg = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_modelg'],
                'model': self.preloaddata['modelg'],
                'color_texture': self.preloaddata['tex'],
                'lighting': False,
                'opacity': 0.2,
                'materials': [shared.footing_material]
            })
        self.nodee = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_modele'],
                'model': self.preloaddata['modele'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['tex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.1, 1.0)
        gnode.ambient_color = (1.1, 1.1, 1.0)
        gnode.vignette_outer = (0.7, 0.65, 0.75)
        gnode.vignette_inner = (0.95, 0.95, 0.93)


class GotchamapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-8.5184, 0.56928, -1.49458) + (1.22169, 0.05, 1.26353)
    points['ffa_spawn2'] = (8.59355, 0.59544, -1.43799) + (1.20895, 0.05, 1.25724)
    points['ffa_spawn3'] = (-8.54483, 0.5694, 4.72378) + (1.18984, 0.05, 1.29418)
    points['ffa_spawn4'] = (8.70633, 0.5694, 4.74922) + (1.18907, 0.05, 1.26568)
    points['flag1'] = (-9.9261, 1.26464, 1.5577)
    points['flag2'] = (10.02378, 1.32188, 1.59798)
    points['flag_default'] = (0.02873, 2.60659, 1.51861)
    points['powerup_spawn1'] = (-3.93765, 1.08218, -2.33189)
    points['powerup_spawn2'] = (4.12161, 1.14281, -2.33589)
    points['powerup_spawn3'] = (-3.92186, 0.92373, 5.8076)
    points['powerup_spawn4'] = (4.1484, 0.92373, 5.74238)
    points['spawn1'] = (-8.4059, 0.5624, 1.62179) + (0.4613, 0.05, 2.22033)
    points['spawn2'] = (8.46397, 0.58856, 1.70095) + (0.4613, 0.05, 2.22033)
    points['tnt1'] = (0.0275, 0.87995, 1.51592)
    boxes['area_of_interest_bounds'] = (0.36325, 1.10086, 2.99368) + (0, 0, 0) + (28.94068, 14.07879, 14.7444)
    boxes['map_bounds'] = (0.25204, 1.42446, 3.3493) + (0, 0, 0) + (34.76113, 24.79939, 23.84771)


class GotchaMap(ba.Map):
    defs = GotchamapDefs()
    name = 'Gotcha'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'gotchaMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('gotchaMap'),
            'collide_model': ba.getcollidemodel('gotchaMapCob'),
            'tex': ba.gettexture('gotchaMapColor'),
            'bgmodel': ba.getmodel('gotchaMapBG'),
            'railing_collide_model': ba.getcollidemodel('gotchaMapRailing')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.railing = ba.newnode(
            'terrain',
            attrs={
                'collide_model': self.preloaddata['railing_collide_model'],
                'materials': [shared.railing_material],
                'bumper': True
            })
        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['tex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (0.8, 0.9, 1.3)
        gnode.ambient_color = (0.8, 0.9, 1.3)
        gnode.vignette_outer = (0.79, 0.79, 0.69)
        gnode.vignette_inner = (0.97, 0.97, 0.99)


class GravityfallsmapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-6.97783, 2.05753, -4.75154) + (1.4663, 0.05, 0.87378)
    points['ffa_spawn2'] = (7.28045, 2.0837, -5.7546) + (1.67437, 0.05, 0.87378)
    points['ffa_spawn3'] = (12.50401, 2.04888, -1.16587) + (0.48506, 0.05, 1.59702)
    points['ffa_spawn4'] = (-10.66812, 2.04888, 1.1377) + (0.48506, 0.05, 1.59702)
    points['flag1'] = (-12.62698, 3.02028, -2.23155)
    points['flag2'] = (11.71206, 2.51231, -4.23504)
    points['flag_default'] = (0.16225, 2.56307, -1.87058)
    points['powerup_spawn1'] = (-8.4451, 2.39672, -2.23429)
    points['powerup_spawn2'] = (5.24553, 2.45735, 2.6822)
    points['powerup_spawn3'] = (-13.7492, 2.43847, 2.63631)
    points['powerup_spawn4'] = (11.17395, 2.43847, -6.65691)
    points['spawn1'] = (-12.93303, 2.01032, 0.78771) + (1.6634, 0.05, 0.87378)
    points['spawn2'] = (13.39258, 2.03649, -1.57687) + (1.6634, 0.05, 0.87378)
    points['tnt1'] = (-4.29628, 2.48705, -10.83656)
    boxes['area_of_interest_bounds'] = (-1.0776, 2.93491, -2.53375) + (0, 0, 0) + (46.36258, 11.84662, 21.07336)
    boxes['map_bounds'] = (-1.22571, 3.39742, -4.04047) + (0, 0, 0) + (46.29672, 20.86748, 34.08423)


class PortalGF(ba.Actor):
    def __init__(self,
                 position: Sequence[float] = (0.0, 1.0, 0.0),
                 position2: Sequence[float] = (0.0, 1.0, 0.0),
                 color: Sequence[float] = (1.0, 1.0, 1.0)):
        super().__init__()
        shared = SharedObjects.get()

        self.radius = 1.1
        self.position = position
        self.position2 = position2
        self.cooldown = False

        self.portalmaterial = ba.Material()
        self.portalmaterial.add_actions(
            conditions=(
                ('they_have_material', shared.player_material)
            ),
            actions=(('modify_part_collision', 'collide', True),
                     ('modify_part_collision', 'physical', False),
                     ('call', 'at_connect', self.portal)),
        )

        self.portalmaterial.add_actions(
            conditions=(
                ('they_have_material', shared.object_material),
                'or',
                ('they_dont_have_material', shared.player_material),
            ),
            actions=(('modify_part_collision', 'collide', True),
                     ('modify_part_collision', 'physical', False),
                     ('call', 'at_connect', self.objportal)),
        )

        self.node = ba.newnode(
            'region',
            attrs={'position': (self.position[0],
                                self.position[1],
                                self.position[2]),
                   'scale': (0.1, 0.1, 0.1),
                   'type': 'sphere',
                   'materials': [self.portalmaterial]}
        )
        ba.animate_array(self.node, 'scale', 3,
                         {0: (0, 0, 0), 0.5: (self.radius * 5,
                                              self.radius * 5,
                                              self.radius * 5)})

        self.portal2material = ba.Material()
        self.portal2material.add_actions(
            conditions=(
                ('they_have_material', shared.player_material)
            ),
            actions=(('modify_part_collision', 'collide', True),
                     ('modify_part_collision', 'physical', False),
                     ('call', 'at_connect', self.portal2)),
        )

        self.portal2material.add_actions(
            conditions=(
                ('they_have_material', shared.object_material),
                'or',
                ('they_dont_have_material', shared.player_material),
            ),
            actions=(('modify_part_collision', 'collide', True),
                     ('modify_part_collision', 'physical', False),
                     ('call', 'at_connect', self.objportal2)),
        )

        self.node2 = ba.newnode(
            'region',
            attrs={'position': (self.position2[0],
                                self.position2[1],
                                self.position2[2]),
                   'scale': (0.1, 0.1, 0.1),
                   'type': 'sphere',
                   'materials': [self.portal2material]}
        )
        ba.animate_array(self.node2, 'scale', 3,
                         {0: (0, 0, 0), 0.5: (self.radius * 5,
                                              self.radius * 5,
                                              self.radius * 5)})

    def cooldown1(self):
        self.cooldown = True

        def off():
            self.cooldown = False

        ba.timer(0.01, off)

    def portal(self):
        sound = ba.getsound('powerup01')
        ba.playsound(sound)
        node = ba.getcollision().opposingnode
        node.handlemessage(ba.StandMessage(self.node2.position))

    def portal2(self):
        return

    def objportal(self):
        node = ba.getcollision().opposingnode
        if node.getnodetype() == 'spaz':
            return
        v = node.velocity
        if not self.cooldown:
            node.position = self.position2
            self.cooldown1()

        def vel():
            node.velocity = v

        ba.timer(0.01, vel)

    def objportal2(self):
        return


class GravityFallsMap(ba.Map):
    defs = GravityfallsmapDefs()
    name = 'Gravity Falls'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'gravityFallsMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('gravityFallsMap'),
            'collide_model': ba.getcollidemodel('gravityFallsMapCob'),
            'modeld': ba.getmodel('gravityFallsMapD'),
            'tex': ba.gettexture('gravityFallsMapColor')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        self.noded = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['modeld'],
                'materials': [shared.footing_material,
                              shared.death_material]
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (0.8, 0.9, 1.3)
        gnode.ambient_color = (0.8, 0.9, 1.3)
        gnode.vignette_outer = (0.79, 0.79, 0.69)
        gnode.vignette_inner = (0.97, 0.97, 0.99)

        PortalGF(position=(7.5929, -10.1028, -1.68649),
                 position2=(5.2929, 11.1028, -2.78649),
                 color=(3, 0, 9))


class GuardianmapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-2.07349, 3.88767, -6.65336) + (0.19747, 0.03, 0.51546)
    points['ffa_spawn2'] = (-4.70652, 3.91384, -3.78073) + (0.2047, 0.0271, 0.46127)
    points['ffa_spawn3'] = (-4.75011, 3.88779, 0.05944) + (0.46197, 0.0271, 0.20634)
    points['ffa_spawn4'] = (-1.96338, 3.88779, 2.74233) + (0.46098, 0.02698, 0.21011)
    points['ffa_spawn5'] = (2.1002, 3.88767, 2.65299) + (0.17194, 0.0271, 0.46628)
    points['ffa_spawn6'] = (4.74843, 3.91384, -0.14317) + (0.21347, 0.0271, 0.45728)
    points['ffa_spawn7'] = (4.71459, 3.88779, -4.09687) + (0.47092, 0.0271, 0.1773)
    points['ffa_spawn8'] = (1.80796, 3.88779, -6.9272) + (0.44113, 0.0271, 0.24531)
    points['flag1'] = (-12.55316, 4.98557, -14.28474)
    points['flag2'] = (12.34078, 5.04281, -14.94647)
    points['flag_default'] = (0.01441, 4.69604, -2.06973)
    points['powerup_spawn1'] = (-0.06763, 4.25657, -6.24298)
    points['powerup_spawn2'] = (-3.04409, 4.4172, -5.05894)
    points['powerup_spawn3'] = (-4.14865, 4.19812, -1.90987)
    points['powerup_spawn4'] = (-2.89817, 4.19812, 1.01643)
    points['powerup_spawn5'] = (0.06065, 4.35657, 2.15929)
    points['powerup_spawn6'] = (3.00639, 4.4172, 0.88465)
    points['powerup_spawn7'] = (4.18947, 4.19812, -2.12366)
    points['powerup_spawn8'] = (2.91713, 4.19812, -5.14095)
    points['spawn1'] = (-10.34384, 4.73805, -11.94499) + (0.09711, 0.04517, 3.35739)
    points['spawn2'] = (10.23575, 4.86421, -12.60951) + (3.34782, 0.04517, 0.2713)
    points['tnt1'] = (-5.48852, 4.87128, 3.64587)
    points['tnt2'] = (5.63454, 4.87128, 3.55774)
    boxes['area_of_interest_bounds'] = (-0.24115, 4.79046, -3.77876) + (0, 0, 0) + (17.63465, 15.05966, 16.71558)
    boxes['map_bounds'] = (-0.33468, 5.19656, -4.80404) + (0, 0, 0) + (30.96915, 26.52718, 27.03592)


class GuardianMap(ba.Map):
    defs = GuardianmapDefs()
    name = 'Guardian'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'guardianMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('guardianMap'),
            'collide_model': ba.getcollidemodel('guardianMapCob'),
            'tex': ba.gettexture('guardianMapColor'),
            'bgtex': ba.gettexture('skyGlassBG'),
            'bgmodel': ba.getmodel('thePadBG')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['bgtex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (0.8, 0.9, 1.3)
        gnode.ambient_color = (0.8, 0.9, 1.3)
        gnode.vignette_outer = (0.79, 0.79, 0.69)
        gnode.vignette_inner = (0.97, 0.97, 0.99)


class HalloweenmapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-3.21939, 4.36361, -20.48689) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn10'] = (6.11609, 4.53849, -18.89968) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn11'] = (8.65855, 4.75483, -16.74401) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn12'] = (10.50375, 5.01777, -8.63663) + (0.55372, 0.05, 5.43854)
    points['ffa_spawn13'] = (9.58738, 4.93388, -0.37638) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn14'] = (7.64953, 4.91408, 1.82044) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn15'] = (5.01917, 4.93212, 2.20499) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn16'] = (-0.0325, 3.14097, 2.10002) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn2'] = (-6.24933, 4.53849, -18.89968) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn3'] = (-8.65944, 4.75483, -16.74401) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn4'] = (-10.56597, 5.01777, -8.63663) + (0.55372, 0.05, 5.43854)
    points['ffa_spawn5'] = (-9.80749, 4.93388, -0.37638) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn6'] = (-7.87914, 4.91408, 1.82044) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn7'] = (-5.10961, 4.93212, 2.20499) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn8'] = (-0.0325, 3.14097, 2.10002) + (0.55372, 0.05, 0.52935)
    points['ffa_spawn9'] = (3.20042, 4.36361, -20.48689) + (0.55372, 0.05, 0.52935)
    points['flag1'] = (-8.62451, 4.24695, -7.51276)
    points['flag2'] = (8.59073, 4.17493, -7.4768)
    points['flag_default'] = (-0.04391, 4.97167, -20.18156)
    points['powerup_spawn1'] = (8.45206, 4.24325, -12.30868)
    points['powerup_spawn2'] = (-8.11399, 4.27517, -12.19911)
    points['powerup_spawn3'] = (-8.23795, 4.23112, -3.28173)
    points['powerup_spawn4'] = (8.14943, 4.24283, -2.71368)
    points['spawn1'] = (-10.5791, 4.84945, -7.53411) + (0.50029, 0.05, 3.20865)
    points['spawn2'] = (10.51234, 4.84931, -7.51627) + (0.48792, 0.05, 3.2029)
    points['tnt1'] = (0.44224, 2.83063, -11.26023)
    points['tnt2'] = (-0.66255, 2.81362, -3.3946)
    boxes['area_of_interest_bounds'] = (0.08641, 4.39067, -7.46992) + (0, 0, 0) + (51.08173, 54.97659, 42.52111)
    boxes['map_bounds'] = (-0.10175, 5.00256, -12.05441) + (0, 0, 0) + (58.81755, 63.49395, 45.09238)


class Halloween(ba.Map):
    defs = HalloweenmapDefs()
    name = 'Halloween'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'hwMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('hwMap'),
            'collide_model': ba.getcollidemodel('hwMapCob'),
            'tex': ba.gettexture('hwMapColor')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        gnode = ba.getactivity().globalsnode
        gnode.tint = (0.8, 0.9, 1.3)
        gnode.ambient_color = (0.8, 0.9, 1.3)
        gnode.vignette_outer = (0.79, 0.79, 0.69)
        gnode.vignette_inner = (0.97, 0.97, 0.99)


class IcemapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (8.73357, 5.09934, 2.27606) + (0.78982, 0.05, 1.3628)
    points['ffa_spawn2'] = (8.63628, 5.83788, -7.26134) + (0.78982, 0.05, 1.3628)
    points['ffa_spawn3'] = (-9.03869, 5.09934, 2.27066) + (0.78982, 0.05, 1.3628)
    points['ffa_spawn4'] = (-8.89221, 5.83788, -7.2801) + (0.78982, 0.05, 1.3628)
    points['flag1'] = (8.97686, 5.45802, 4.83282)
    points['flag2'] = (-8.94129, 6.20577, -8.61665)
    points['flag3'] = (-9.36293, 5.45802, 4.79063)
    points['flag4'] = (8.63678, 6.20577, -8.66938)
    points['flag_default'] = (-0.19593, 4.38208, 4.59982)
    points['powerup_spawn1'] = (9.3797, 5.59043, 3.62563)
    points['powerup_spawn2'] = (-9.70205, 5.65105, 3.64135)
    points['powerup_spawn3'] = (-9.92278, 6.17397, -6.07351)
    points['powerup_spawn4'] = (9.52793, 6.07397, -6.12759)
    points['race_mine1'] = (6.62301, 5.38078, 3.805)
    points['race_mine2'] = (4.548, 5.38078, 0.49843)
    points['race_mine3'] = (5.73178, 5.74403, -4.13684)
    points['race_mine4'] = (-6.43899, 5.51047, -4.09674)
    points['race_mine5'] = (-5.05255, 5.36071, 0.52398)
    points['race_mine6'] = (-7.22847, 5.33566, 3.74171)
    points['race_point1'] = (-0.23437, 5.40034, 4.69668) + (0.2825, 3.95051, 1.70289)
    points['race_point2'] = (8.70337, 5.34581, 2.06327) + (1.54214, 3.95051, 0.2825)
    points['race_point3'] = (8.60551, 5.82501, -7.23624) + (1.4634, 3.95051, 0.2575)
    points['race_point4'] = (-9.01558, 5.7132, -7.22704) + (1.4513, 3.95051, 0.26029)
    points['race_point5'] = (-9.16008, 5.53273, 2.04487) + (1.54315, 3.95051, 0.2825)
    points['spawn1'] = (-4.03787, 3.21046, -6.22642) + (0.93466, 0.05, 3.0751)
    points['spawn2'] = (4.45458, 3.23662, -6.22464) + (0.93466, 0.05, 3.0751)
    points['tnt1'] = (-0.21676, 5.59505, -2.38739)
    boxes['area_of_interest_bounds'] = (-0.08966, 2.55672, -3.97028) + (0, 0, 0) + (24.12044, 12.6595, 18.50299)
    boxes['map_bounds'] = (-0.18319, 6.96282, -1.58038) + (0, 0, 0) + (29.23565, 16.29936, 21.43922)


class IceMap(ba.Map):
    defs = IcemapDefs()
    name = 'Ice Map'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return [
            'melee', 'keep_away', 'team_flag', 'king_of_the_hill', 'conquest', 'race']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'iceMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model_top': ba.getmodel('iceMapTop'),
            'collide_model_top': ba.getcollidemodel('iceMapTopCob'),
            'model_bottom': ba.getmodel('iceMapBottom'),
            'collide_model_bottom': ba.getcollidemodel('iceMapBottomCob'),
            'model_ice': ba.getmodel('iceMapIce'),
            'collide_model_ice': ba.getcollidemodel('iceMapIceCob'),
            'tex': ba.gettexture('iceMapColor'),
            'bgtex': ba.gettexture('natureBackgroundNColor'),
            'bgmodel': ba.getmodel('natureBackground')
        }
        mat = ba.Material()
        mat.add_actions(actions=('modify_part_collision', 'friction', 0.01))
        data['ice_material'] = mat
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.top = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model_top'],
                'model': self.preloaddata['model_top'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.bottom = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model_bottom'],
                'model': self.preloaddata['model_bottom'],
                'lighting': False,
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.ice = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model_ice'],
                'model': self.preloaddata['model_ice'],
                'reflection': 'soft',
                'reflection_scale': [0.65],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material,
                              self.preloaddata['ice_material']]
            })
        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['bgtex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (0.8, 0.9, 1.3)
        gnode.ambient_color = (0.8, 0.9, 1.3)
        gnode.vignette_outer = (0.79, 0.79, 0.69)
        gnode.vignette_inner = (0.97, 0.97, 0.99)


class KrustykrabmapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-6.22221, 4.04595, -2.42887) + (1.00304, 0.05, 0.67435)
    points['ffa_spawn2'] = (4.34829, 4.04595, -2.42887) + (1.00304, 0.05, 0.67435)
    points['ffa_spawn3'] = (-6.12272, 4.04595, 5.08241) + (1.00304, 0.05, 0.67435)
    points['ffa_spawn4'] = (5.56701, 4.04595, 4.95805) + (1.00304, 0.05, 0.67435)
    points['flag1'] = (-9.61277, 4.30876, 1.45718)
    points['flag2'] = (9.17461, 4.366, 1.29792)
    points['flag_default'] = (-0.63318, 4.38208, 0.99473)
    points['powerup_spawn1'] = (-6.38018, 4.40338, 0.61122)
    points['powerup_spawn2'] = (4.2279, 4.43021, 0.55974)
    points['powerup_spawn3'] = (-0.37144, 4.36881, 4.96673)
    points['powerup_spawn4'] = (-0.78748, 4.35755, -1.71495)
    points['spawn1'] = (-9.71476, 4.06156, 2.26422) + (0.46069, 0.05, 1.22664)
    points['spawn2'] = (9.51737, 4.08772, 2.20081) + (0.46069, 0.05, 1.22664)
    points['tnt1'] = (-1.32497, 4.77605, -4.34548)
    boxes['area_of_interest_bounds'] = (-0.19385, 4.69839, 1.34427) + (0, 0, 0) + (25.75767, 18.8136, 10.50299)
    boxes['map_bounds'] = (0.10981, 5.1045, -1.04853) + (0, 0, 0) + (57.5275, 33.13962, 29.92689)


class KrustyKrabMap(ba.Map):
    defs = KrustykrabmapDefs()
    name = 'Krusty Krab'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill', 'race']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'krustyKrabMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('krustyKrabMap'),
            'collide_model': ba.getcollidemodel('krustyKrabMapCob'),
            'tex': ba.gettexture('krustyKrabMapColor'),
            'bgtex': ba.gettexture('krustyKrabBGMapColor'),
            'bgmodel': ba.getmodel('krustyKrabBGMap')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['bgtex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.15, 1.11, 1.03)
        gnode.ambient_color = (1.2, 1.1, 1.0)
        gnode.vignette_outer = (0.7, 0.73, 0.7)
        gnode.vignette_inner = (0.95, 0.95, 0.95)


class PicnicmapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-7.44398, 3.19387, -7.65979) + (1.50247, 0.03167, 0.55348)
    points['ffa_spawn2'] = (8.06371, 3.22003, -7.62365) + (1.4616, 0.02953, 0.51603)
    points['ffa_spawn3'] = (-7.41217, 3.194, 1.58774) + (1.49532, 0.05173, 0.50184)
    points['ffa_spawn4'] = (8.10603, 3.19399, 1.60122) + (1.42925, 0.05045, 0.48938)
    points['flag1'] = (-8.83272, 3.6421, -3.06993)
    points['flag2'] = (9.50256, 3.69934, -3.27696)
    points['flag_default'] = (0.30904, 3.54993, -3.16521)
    points['powerup_spawn1'] = (-3.82429, 3.7163, -6.69373)
    points['powerup_spawn2'] = (-6.30979, 3.77692, -0.92893)
    points['powerup_spawn3'] = (5.53497, 3.55785, -1.38555)
    points['powerup_spawn4'] = (5.67173, 3.55785, -6.19241)
    points['spawn1'] = (-8.88537, 3.19387, -3.02879) + (0.87378, 0.05, 1.6634)
    points['spawn2'] = (9.52927, 3.22003, -3.30216) + (0.87378, 0.05, 1.6634)
    points['tnt1'] = (0.73104, 3.61641, 0.91022)
    boxes['area_of_interest_bounds'] = (0.35441, 4.49356, -2.51839) + (0, 0, 0) + (23.64755, 8.06139, 18.50299)
    boxes['map_bounds'] = (0.39722, 4.89966, -5.12601) + (0, 0, 0) + (22.08287, 20.7854, 29.92689)


class PicnicMap(ba.Map):
    defs = PicnicmapDefs()
    name = 'Picnic'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'mapPicnicPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('mapPicnic'),
            'collide_model': ba.getcollidemodel('mapPicnicCob'),
            'modelc': ba.getmodel('mapPicnicTransparent'),
            'collide_modelc': ba.getcollidemodel('mapPicnicTransparentCob'),
            'collide_modeld': ba.getcollidemodel('mapPicnicDeathCob'),
            'tex': ba.gettexture('mapPicnicColor'),
            'bgtex': ba.gettexture('menuBG'),
            'bgmodel': ba.getmodel('thePadBG')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })
        self.nodec = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_modelc'],
                'model': self.preloaddata['modelc'],
                'color_texture': self.preloaddata['tex'],
                'opacity': 0.8,
                'materials': [shared.footing_material]
            })
        self.noded = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_modeld'],
                'materials': [shared.footing_material,
                              shared.death_material]
            })
        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['bgtex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.1, 1.0)
        gnode.ambient_color = (1.1, 1.1, 1.0)
        gnode.vignette_outer = (0.7, 0.65, 0.75)
        gnode.vignette_inner = (0.95, 0.95, 0.93)


class MarioworldmapDefs:
    # This file was automatically generated from "thePadLevel.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (3.151, 3.28557, -11.62294) + (0.78108, 0.05, 0.78913)
    points['ffa_spawn2'] = (-3.89813, 3.28557, -11.61621) + (0.77292, 0.05, 0.79949)
    points['ffa_spawn3'] = (-8.91371, 3.28557, -6.39059) + (0.76822, 0.05, 0.78687)
    points['ffa_spawn4'] = (-8.91988, 3.28557, 0.39817) + (0.77204, 0.05, 0.78333)
    points['ffa_spawn5'] = (-3.91388, 3.28557, 5.41779) + (0.7682, 0.05, 0.77865)
    points['ffa_spawn6'] = (3.13084, 3.28557, 5.42816) + (0.76469, 0.05, 0.80429)
    points['ffa_spawn7'] = (8.00649, 3.28557, 0.39817) + (0.76822, 0.05, 0.78687)
    points['ffa_spawn8'] = (7.9949, 3.28557, -6.39856) + (0.76689, 0.05, 0.7936)
    points['flag1'] = (5.29873, 4.46068, -8.91326)
    points['flag2'] = (5.29841, 4.46068, 2.67068)
    points['flag3'] = (-6.0173, 4.46068, 2.64588)
    points['flag4'] = (-6.00445, 4.46068, -8.91204)
    points['flag_default'] = (-0.32485, 4.64644, -2.97299)
    points['powerup_spawn1'] = (5.4662, 3.62173, -3.13033)
    points['powerup_spawn2'] = (-0.30004, 3.62173, -8.9136)
    points['powerup_spawn3'] = (-6.17938, 3.62173, -3.12631)
    points['powerup_spawn4'] = (-0.30531, 3.62173, 2.94049)
    points['spawn1'] = (9.04137, 3.02487, -2.90355) + (1.29071, 0.05, 1.91677)
    points['spawn2'] = (-9.729, 3.02487, -2.95026) + (1.29071, 0.05, 1.91677)
    points['spawn_by_flag1'] = (7.94788, 3.01322, -8.88789) + (0.75187, 0.05, 0.84538)
    points['spawn_by_flag2'] = (-8.87075, 3.01322, -8.93492) + (0.75187, 0.05, 0.84538)
    points['spawn_by_flag3'] = (-8.91571, 3.01322, 2.8066) + (0.75187, 0.05, 0.84538)
    points['spawn_by_flag4'] = (8.07702, 3.01322, 2.84106) + (0.75187, 0.05, 0.84538)
    points['tnt1'] = (3.16319, 3.31034, -6.37489)
    points['tnt2'] = (-3.86491, 3.31034, -6.42483)
    points['tnt3'] = (-3.83403, 3.31034, 0.45535)
    points['tnt4'] = (3.1593, 3.31034, 0.56443)
    boxes['area_of_interest_bounds'] = (0.35441, 0.15553, 0.02918) + (0, 0, 0) + (20.65136, 23.83756, 18.50299)
    boxes['map_bounds'] = (0.26088, 7.08896, -3.08543) + (0, 0, 0) + (29.00671, 28.73445, 27.12031)


class MarioWorldMap(ba.Map):
    defs = MarioworldmapDefs()
    name = 'Mario Bros World'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill', 'conquest']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'mbwMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('mbw'),
            'collide_model': ba.getcollidemodel('mbwCob'),
            'tex': ba.gettexture('mbwColor'),
            'bgtex': ba.gettexture('uknucklesBGColor'),
            'bgmodel': ba.getmodel('thePadBG')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        self.background = ba.newnode(
            'terrain',
            attrs={
                'model': self.preloaddata['bgmodel'],
                'lighting': False,
                'background': True,
                'color_texture': self.preloaddata['bgtex']
            })
        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.1, 1.1, 1.0)
        gnode.ambient_color = (1.1, 1.1, 1.0)
        gnode.vignette_outer = (0.7, 0.65, 0.75)
        gnode.vignette_inner = (0.95, 0.95, 0.93)

    def is_point_near_edge(self,
                           point: ba.Vec3,
                           running: bool = False) -> bool:
        box_position = self.defs.boxes['edge_box'][0:3]
        box_scale = self.defs.boxes['edge_box'][6:9]
        xpos = (point.x - box_position[0]) / box_scale[0]
        zpos = (point.z - box_position[2]) / box_scale[2]
        return xpos < -0.5 or xpos > 0.5 or zpos < -0.5 or zpos > 0.5


class PacmanmapDefs:
    # This file generated from "pacmanMap.ma"
    points = {}
    boxes = {}
    points['ffa_spawn1'] = (-9.67927, 0.58588, -7.13608) + (0.65447, 0.05, 0.58413)
    points['ffa_spawn2'] = (8.08484, 0.58588, 5.82097) + (0.71956, 0.05, 0.64222)
    points['ffa_spawn3'] = (-8.18949, 0.58588, 5.81325) + (0.65447, 0.05, 0.58413)
    points['ffa_spawn4'] = (9.5672, 0.58588, -7.12513) + (0.71956, 0.05, 0.64222)
    points['flag1'] = (-0.01855, 0.91513, 9.92087)
    points['flag2'] = (-0.05367, 0.92024, -7.16025)
    points['flag_default'] = (-0.05154, 0.99034, -0.74039)
    points['powerup_spawn1'] = (-9.6929, 0.93028, -8.68649)
    points['powerup_spawn2'] = (9.59894, 0.93028, -8.60753)
    points['powerup_spawn3'] = (-9.72155, 0.93028, 5.58694)
    points['powerup_spawn4'] = (9.72079, 0.93028, 5.6272)
    points['powerup_spawn5'] = (-0.01869, 0.93028, 1.34941)
    points['spawn1'] = (-0.01986, 0.77565, 9.98158) + (3.94253, 0.05, 0.38847)
    points['spawn2'] = (-0.05893, 0.77565, -7.1692) + (3.90012, 0.05, 0.3592)
    points['tnt1'] = (-1.42239, 0.98812, -0.69979)
    points['tnt2'] = (1.40068, 0.98811, -0.77369)
    boxes['area_of_interest_bounds'] = (-0.08534, 2.76726, 2.09197) + (0, 0, 0) + (14.50743, 14.58622, 28.3354)
    boxes['map_bounds'] = (-0.0229, 9.33466, -0.52407) + (0, 0, 0) + (21.48431, 18.8591, 22.6373)


class PortalPM(ba.Actor):
    def __init__(self,
                 position: Sequence[float] = (0.0, 1.0, 0.0),
                 position2: Sequence[float] = (0.0, 1.0, 0.0),
                 color: Sequence[float] = (1.0, 1.0, 1.0)):
        super().__init__()
        shared = SharedObjects.get()

        self.radius = 1.1
        self.position = position
        self.position2 = position2
        self.cooldown = False

        self.portalmaterial = ba.Material()
        self.portalmaterial.add_actions(
            conditions=(
                ('they_have_material', shared.player_material)
            ),
            actions=(('modify_part_collision', 'collide', True),
                     ('modify_part_collision', 'physical', False),
                     ('call', 'at_connect', self.portal)),
        )

        self.portalmaterial.add_actions(
            conditions=(
                ('they_have_material', shared.object_material),
                'or',
                ('they_dont_have_material', shared.player_material),
            ),
            actions=(('modify_part_collision', 'collide', True),
                     ('modify_part_collision', 'physical', False),
                     ('call', 'at_connect', self.objportal)),
        )

        self.node = ba.newnode(
            'region',
            attrs={'position': (self.position[0],
                                self.position[1],
                                self.position[2]),
                   'scale': (0.1, 0.1, 0.1),
                   'type': 'sphere',
                   'materials': [self.portalmaterial]}
        )
        ba.animate_array(self.node, 'scale', 3,
                         {0: (0, 0, 0), 0.5: (self.radius,
                                              self.radius,
                                              self.radius)})

        self.portal2material = ba.Material()
        self.portal2material.add_actions(
            conditions=(
                ('they_have_material', shared.player_material)
            ),
            actions=(('modify_part_collision', 'collide', True),
                     ('modify_part_collision', 'physical', False),
                     ('call', 'at_connect', self.portal2)),
        )

        self.portal2material.add_actions(
            conditions=(
                ('they_have_material', shared.object_material),
                'or',
                ('they_dont_have_material', shared.player_material),
            ),
            actions=(('modify_part_collision', 'collide', True),
                     ('modify_part_collision', 'physical', False),
                     ('call', 'at_connect', self.objportal2)),
        )

        self.node2 = ba.newnode(
            'region',
            attrs={'position': (self.position2[0],
                                self.position2[1],
                                self.position2[2]),
                   'scale': (0.1, 0.1, 0.1),
                   'type': 'sphere',
                   'materials': [self.portal2material]}
        )
        ba.animate_array(self.node2, 'scale', 3,
                         {0: (0, 0, 0), 0.5: (self.radius,
                                              self.radius,
                                              self.radius)})

    def cooldown1(self):
        self.cooldown = True

        def off():
            self.cooldown = False

        ba.timer(0.01, off)

    def portal(self):
        sound = ba.getsound('powerup01')
        ba.playsound(sound)
        node = ba.getcollision().opposingnode
        node.handlemessage(ba.StandMessage(self.node2.position))

    def portal2(self):
        sound = ba.getsound('powerup01')
        ba.playsound(sound)
        node = ba.getcollision().opposingnode
        node.handlemessage(ba.StandMessage(self.node.position))

    def objportal(self):
        node = ba.getcollision().opposingnode
        if node.getnodetype() == 'spaz':
            return
        v = node.velocity
        if not self.cooldown:
            node.position = self.position2
            self.cooldown1()

        def vel():
            node.velocity = v

        ba.timer(0.01, vel)

    def objportal2(self):
        node = ba.getcollision().opposingnode
        if node.getnodetype() == 'spaz':
            return
        v = node.velocity
        if not self.cooldown:
            node.position = self.position
            self.cooldown1()

        def vel():
            node.velocity = v

        ba.timer(0.01, vel)


class PacMan(ba.Map):
    defs = PacmanmapDefs()
    name = 'PAC-MAN'

    @classmethod
    def get_play_types(cls) -> list[str]:
        """Return valid play types for this map."""
        return ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']

    @classmethod
    def get_preview_texture_name(cls) -> str:
        return 'pacmanMapPreview'

    @classmethod
    def on_preload(cls) -> Any:
        data: dict[str, Any] = {
            'model': ba.getmodel('pacmanMap'),
            'collide_model': ba.getcollidemodel('pacmanMapCob'),
            'tex': ba.gettexture('pacmanMapColor')
        }
        return data

    def __init__(self) -> None:
        super().__init__()
        shared = SharedObjects.get()
        self.node = ba.newnode(
            'terrain',
            delegate=self,
            attrs={
                'collide_model': self.preloaddata['collide_model'],
                'model': self.preloaddata['model'],
                'color_texture': self.preloaddata['tex'],
                'materials': [shared.footing_material]
            })

        gnode = ba.getactivity().globalsnode
        gnode.tint = (1.3, 1.2, 1.0)
        gnode.ambient_color = (1.3, 1.2, 1.0)
        gnode.vignette_outer = (0.57, 0.57, 0.57)
        gnode.vignette_inner = (0.9, 0.9, 0.9)
        gnode.vr_camera_offset = (0.0, -4.2, -1.1)
        gnode.vr_near_clip = 0.5

        PortalPM(position=(-10.2929, 0.1028, -0.68649),
                 position2=(10.2929, 0.1028, -0.68649),
                 color=(3, 0, 9))


files_needed = {}
headless_mode = _ba.env()['headless_mode']
for file, value in package_files.items():
    if headless_mode:
        if not file.endswith('.cob'):
            continue
    else:
        if file.endswith('.dds'):
            if _ba.app.platform == 'android':
                continue
        elif file.endswith('.ktx'):
            if _ba.app.platform != 'android':
                continue
    files_needed[file] = value


check_md5 = True

PackInstaller(package_name, files_needed)


# ba_meta export plugin
class Map(ba.Plugin):
    def on_app_launch(self):
        for map in (GeomMap, WashMap, ArenaMinigore, BikiniBottomMap, BombermanMap, CourageMap, DreamlandMap, EliminationRawMap, EliminationSDMap, GotchaMap, GravityFallsMap, GuardianMap, Halloween, IceMap, KrustyKrabMap, PicnicMap, MarioWorldMap, PacMan):
            try:
                _map.register_map(map)
            except:
                pass

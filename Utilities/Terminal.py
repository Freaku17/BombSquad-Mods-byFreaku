# Made by your friend: Freaku


# Defines a simple plugin that allows you to:
### See any errors of your mods (if present) in folder BombSquad/console/logs.txt
### Get config contents
### Create/Delete sys
### Get 3D co-ordinate points in any Map!


# NOTE: Please perform the activities to log, if its a gamemode pls open and play it and then see logs. If its a window please touch buttons and then see logs
#       and so on according to the mod you're working...



#Join BCS:
# https://discord.gg/ucyaesh

#My GitHub:
# https://github.com/Freaku17/BombSquad-Mods-byFreaku




########## INDEX ##########
'''
- Must READ
- For beginners
'''


# ----- MUST READ -----
'''
# I hope you know Python Programming Language and have seen Bombsquad's API, avaiable at 
# https://ballistica.net/wiki

# else... its still fine :)

# Python is easiest language, hardly will take 1 week to learn (See YouTube tutorials)


# This mod is *genuinely* for Mobile Modders, 
# in PC you can directly get these Terminal Errors in console.
# but sadly on mobile there's no way to view console.
# We can alternatively, use https://tools.ballistica.net/devices
# but it only works on V2 accounts (and if you link your GooglePlay and V2, and login with GooglePlay... it won't work)
# This is helpful for new Modders (who don't use PC)
# Also I'll ***HIGHLY*** suggest to not use this when other mods are installed
# As a TONS of other mods includes errors (which aren't fixed)
# Happy coding! 🔥
'''

# ----- For beginners -----
'''
# Use create_sys / delete_sys in Plugins
# and a Code Editor app (on Play Store)

# Then start playing (editing) those internal .py files
# Incase you face a black screen on launch (you made an error while editing those sys files)
# Delete the sys folder of folder Bombsquad/sys/{version} and re-open game
'''


# Sometimes you need someone for help
# I would suggest to join BCS: A lovely discord server (link at top)

# Aimed 4 Android modders!





# ba_meta require api 8

import _babase, babase, baenv, os
import bascenev1 as bs
from efro.log import LogLevel
folder = _babase.env()['python_directory_user'] + "/console/"
log_post = folder + 'logs.txt'
config_post = folder + 'config.txt'


def make_folder():
    if not os.path.exists(folder):
        os.makedirs(folder)

def make_config(entry):
    with open(config_post, 'w+') as e:
        e.write(entry)
        e.close()

def dump_cache_logs():
    # Dumps all cache logs (including DEBUG ones)
    for entry in baenv._EnvGlobals.get().config.log_handler.get_cached().entries:
        write_logs(entry.message)

def make_logs(entry):
    if entry.level.value >= LogLevel.WARNING.value or entry.name in ('stdout', 'stderr'):
        write_logs(entry.message)

def write_logs(log):
    print(log, file=open(log_post, 'a+', encoding='utf-8'))

def make_sys():
    path = _babase.app.python_directory_user +'/sys/'+_babase.app.version
    if not os.path.exists(path):
        # Old method:
        # import babase.modutils as utils
        # utils.create_user_system_scripts()
        make_sys_wordaround(path)
        if babase.app.classic.platform == 'android':
            if path.find('/0/'):
                path = path.split('/0/')[1]
        _babase.screenmessage(f'Scripts created at {path}',color=(0, 1, 0))
        _babase.screenmessage('Restart BombSquad to use them',color=(0, 1, 0))
        babase.app.config['Plugins'][__name__+'.create_sys']['enabled'] = False
        babase.app.config.apply_and_commit()
    else:
        _babase.screenmessage('Cannot run '+__name__+'.create_sys\nScripts already exist :/',color=(1,0,0))

def make_sys_wordaround(path):
    # With continued increasing restrictions of Android,
    # it is not possible to "view" in-game folders copied to an external path.
    # Luckily we are still able to write files.
    # So as a "workaround" we create a zip of in-game folders and unzip them :D
    from shutil import make_archive, unpack_archive, rmtree
    sys_zip = make_archive('sys_zip', 'zip', _babase.app.python_directory_app)
    unpack_archive(sys_zip, path)
    
    # We also need to delete all `__pycache__` folders
    for root, dirs, files in os.walk(path):
        if '__pycache__' in dirs:
            pycache_folder = os.path.join(root, '__pycache__')
            rmtree(pycache_folder)

def yeet_sys():
    path = _babase.app.python_directory_user +'/sys/'+_babase.app.version
    if os.path.exists(path):
        import babase.modutils as utils
        utils.delete_user_system_scripts()
        _babase.screenmessage('Scripts deleted!',color=(1, 1, 0))
        _babase.screenmessage('Restart BombSquad to use internal',color=(1, 1, 0))
        babase.app.config['Plugins'][__name__+'.delete_sys']['enabled'] = False
        babase.app.config.apply_and_commit()
    else:
        _babase.screenmessage('Cannot run '+__name__+'.delete_sys\nNo Scripts exist :/',color=(1,0,0))




# ba_meta export plugin
class get_logs(babase.Plugin):
    def __init__(self):
        make_folder()
        open(log_post, 'w+').close()
        dump_cache_logs()
        baenv._EnvGlobals.get().config.log_handler.add_callback(make_logs)


# ba_meta export plugin
class get_config(babase.Plugin):
    def __init__(self):
        make_folder()
        configs = babase.app.config_file_path
        with open(configs) as f:
            make_config(f.read())
            f.close()


# ba_meta export plugin
class create_sys(babase.Plugin):
    def __init__(self):
        babase.apptimer(2.5, make_sys)


# ba_meta export plugin
class delete_sys(babase.Plugin):
    def __init__(self):
        babase.apptimer(3, yeet_sys)







class Player(bs.Player['Team']):
    """Our player type for this game."""
class Team(bs.Team[Player]):
    """Our team type for this game."""

# ba_meta export bascenev1.GameActivity
class Terminal_get3Dpoint(bs.TeamGameActivity[Player, Team]):
    name = '3D co-ordinate point'
    available_settings = [bs.BoolSetting('Boxes', default=False), bs.BoolSetting('Points', default=False)]
    description = 'Get 3D co-ordinate point of ANY map!'

    def __init__(self, settings: dict):
        super().__init__(settings)
        self._boxes = settings.get('Boxes', False)
        self._points = settings.get('Points',False)

    @classmethod
    def supports_session_type(cls, sessiontype):
        return (issubclass(sessiontype, bs.DualTeamSession) or issubclass(sessiontype, bs.FreeForAllSession))

    @classmethod
    def get_supported_maps(cls, sessiontype):
        # Support every single map registered to the game...
        maps = []
        for map in babase.app.classic.maps:
            maps.append(map)
        return maps

    def on_begin(self):
        super().on_begin()
        if self._boxes:
            self.spawn_boxes()
        if self._points:
            self.spawn_points()

    def spawn_boxes(self):
        for box in self.map.defs.boxes:
            box_pt = self.map.defs.boxes[box]
            box_locator = bs.newnode('locator', attrs={'shape':'box', 'position':( box_pt[0], box_pt[1], box_pt[2]), 'color':(1,1,0), 'opacity':1,'draw_beauty':True,'additive':False,'size':(box_pt[6], box_pt[7], box_pt[8])})
            mnode = bs.newnode('math', owner=box_locator, attrs={ 'input1': (0, 0, 0), 'operation': 'add'})
            box_locator.connectattr('position', mnode, 'input2')
            box_text = bs.newnode('text', owner=box_locator, attrs={ 'text': box, 'in_world': True, 'shadow': 0, 'flatness': 0, 'color': (1,1,1), 'scale': 0.01, 'h_align': 'center'})
            mnode.connectattr('output', box_text, 'position')

    def spawn_points(self):
        for point in self.map.defs.points:
            display_pt = self.map.defs.points[point]
            if len(display_pt) == 6:
                point_locator = bs.newnode('locator', attrs={'shape':'box', 'position':( display_pt[0], display_pt[1], display_pt[2]), 'color':(1,1,0), 'opacity':1,'draw_beauty':True,'additive':False,'size':(display_pt[3], display_pt[4], display_pt[5])})
            elif len(display_pt) == 3:
                point_locator = bs.newnode('locator',attrs={'shape':'circle','position':(display_pt[0], display_pt[1], display_pt[2]),'color':(1, 1, 0),'opacity':1,'draw_beauty':True,'additive':False,'drawShadow':False,'size': (0.4,0.4,0.4)})
            else:
                print('Invalid entry of;',point,'values given:',display_pt)
                continue
            mnode = bs.newnode('math', owner=point_locator, attrs={ 'input1': (0, 0, 0), 'operation': 'add'})
            point_locator.connectattr('position', mnode, 'input2')
            point_text = bs.newnode('text', owner=point_locator, attrs={ 'text': point, 'in_world': True, 'shadow': 1.0, 'flatness': 1.0, 'color': (0,0,0), 'scale': 0.01, 'h_align': 'center'})
            mnode.connectattr('output', point_text, 'position')

    def end_game(self):
        results = bs.GameResults()
        for team in self.teams:
            results.set_team_score(team, team.score)
        self.end(results=results)

    def handlemessage(self, msg):
        if isinstance(msg, bs._messages.PlayerDiedMessage):
            self.respawn_player(msg.getplayer(self.playertype), 1)
        else:
            return super().handlemessage(msg)
        return None
        return None

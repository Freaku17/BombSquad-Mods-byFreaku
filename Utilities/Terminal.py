#Made by your friend: Freaku / @[Just] Freak#4999


# Defines a simple plugin that allows you to:
## See any errors of your mods (if present) in folder BombSquad/logging/logs.txt
## Get config contents
## Enable internal debugging
## Create/Delete sys
## Get 3D co-ordinate points in any Map!


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
- Fixing errors...
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
# We can, by following GitHub's Android coding environment
# https://github.com/efroemling/ballistica/wiki/Coding-Environment-(Android)
# but it's long process, additionally around 500mb of data to download
# for Pydroid 3 and it's Pydroid's plugins... (not guaranteed to work properly)
# This is helpful for new Modders (who don't use PC)
# Also I'll ***HIGHLY*** suggest to not use this when other mods are installed
# As a TONS of other mods includes errors (which aren't fixed)
# Rename BombSquad folder to BombSquad1 and make a 
# new BombSquad folder and paste this in that
# and also the mod you're working on....
# Happy coding! 🔥

# Dont worry about those currency mods or similar stuffs...
# Their data is still stored on app so whenever you use them back 
# (deleting BombSquad folder and renaming BombSquad1 back to BombSquad)
# All currency/data will still be avaiable!!
'''

# ----- For beginners -----
'''
# Use create_sys / delete_sys in Plugins
# and a Code Editor app (on Play Store)
'''

# ----- Fixing errors... -----
'''
# Incase you haven't ever seen console:
# The logs.txt shows full stuff ...
# Like say you made a error in your mod but in logs you'll see entire file paths of in-game files.

# Over here you should ignore in-game files and just see Exception/Traceback (or the path where your mod file is named)
# and bottom lines (to know what error is it exactly)

# Reason? Game is certainly completed so no matter what it wont have any error, the error causing is just your file.
# Traceback could look like: Game called a activity as said in this-this line of file, then Map was loaded by the activity, then Map tried to fetch spawn points, but spawn points have error (since you modified it)
'''

# Additionally, errors like
# - Invalid Syntax (if you use code editor just press 3 dots and off word wrap, so you can scroll left/right so you can see the ^ arrow pointing correctly) This error is either cuz of some brackets opened but not closed or the other way around. Could also be if you put = instead of ==
# - Indentation error (this is related to spaces, Google can help/explain you in this...)
# - etc etc (take help of Google 🤐)

# Sometimes you can't just solve it yourself, so you need to ask someone for help
# I would suggest to join BCS: A lovely discord server (link at top)

# Aimed 4 Android modders!





# ba_meta require api 7

import _ba, ba, os
folder = _ba.env()['python_directory_user'] + "/logging/"
log_copy = folder + 'logs.txt'
config_copy = folder + 'config.txt'

def make_folder():
    if not os.path.exists(folder):
        os.makedirs(folder)

def make_logs(content):
    with open(log_copy, 'w+') as l:
        l.write(content)
        l.close()

def log_it():
    our_logs = _ba.getlog()
    if our_logs != '':
        make_logs(our_logs)
    else:
        make_logs("🔥 Congratulations! No errors were found during this playing session!! 🔥")

def make_config():
    configs = _ba.app.config_file_path
    config_contents = ''
    with open(configs) as f:
        config_contents = f.read()
        f.close()
    with open(config_copy, 'w+') as e:
        e.write(config_contents)
        e.close()

def internal_debug():
    """
    Eg. May show some error via screen msg even if try except is used.
    Use only if you are going for really ADVANCED modding...
    """
    setattr(_ba.app, '_debug_enabled', True)

def make_sys():
    path = _ba.app.python_directory_user +'/sys/'+_ba.app.version
    if not os.path.exists(path):
        ba.modutils.create_user_system_scripts()
        if _ba.app.platform == 'android':
            if path.find('/0/'):
                path = path.split('/0/')[1]
        ba.screenmessage(f'Scripts created at {path}',color=(0, 1, 0))
        ba.screenmessage('Restart BombSquad to use them',color=(0, 1, 0))
        ba.app.config['Plugins'][__name__+'.create_sys']['enabled'] = False
        ba.app.config.apply_and_commit()
    else:
        ba.screenmessage('Cannot run '+__name__+'.create_sys\nScripts already exist :/',color=(1,0,0))

def yeet_sys():
    path = _ba.app.python_directory_user +'/sys/'+_ba.app.version
    if os.path.exists(path):
        ba.modutils.delete_user_system_scripts()
        ba.screenmessage('Scripts deleted!',color=(1, 1, 0))
        ba.screenmessage('Restart BombSquad to use internal',color=(1, 1, 0))
        ba.app.config['Plugins'][__name__+'.delete_sys']['enabled'] = False
        ba.app.config.apply_and_commit()
    else:
        ba.screenmessage('Cannot run '+__name__+'.delete_sys\nNo Scripts exist :/',color=(1,0,0))

def update_mods():
    mods_folder = _ba.env()['python_directory_user']
    for mod in os.listdir(mods_folder):
        if mod.endswith('.py'):
            data = open(mods_folder+os.sep+mod).read()
            data = data.replace('# ba_meta require api 7', '# ba_meta require api 7')
            data = data.replace('def on_app_running(self)', 'def on_app_running(self)')
            data = data.replace('self.on_app_running', 'self.on_app_running')
            with open(mods_folder+os.sep+mod, 'w') as file:
                file.write(data)
                file.close()
    ba.screenmessage('Updated mods to 1.7!', color=(0,1,0))
    ba.screenmessage('All Mods are NOT guaranteed to work', color=(1,1,0))
    ba.app.config['Plugins'][__name__+'.update_16mods_to_17']['enabled'] = False
    ba.app.config.apply_and_commit()




# ba_meta export plugin
class update_16mods_to_17(ba.Plugin):
    def __init__(self):
        update_mods()


# ba_meta export plugin
class get_logs(ba.Plugin):
    def __init__(self):
        make_folder()
        log_it()
        ba.timer(1, log_it, repeat=True)


# ba_meta export plugin
class get_config(ba.Plugin):
    def __init__(self):
        make_config()


# ba_meta export plugin
class live_debug(ba.Plugin):
    def __init__(self):
        internal_debug()


# ba_meta export plugin
class create_sys(ba.Plugin):
    def __init__(self):
        ba.timer(3, make_sys)


# ba_meta export plugin
class delete_sys(ba.Plugin):
    def __init__(self):
        ba.timer(3.5, yeet_sys)







class Player(ba.Player['Team']):
    """Our player type for this game."""
class Team(ba.Team[Player]):
    """Our team type for this game."""

# ba_meta export game
class Terminal_get3Dpoint(ba.TeamGameActivity[Player, Team]):
    name = '3D co-ordinate point'
    available_settings = [ba.BoolSetting('Boxes', default=False), ba.BoolSetting('Points', default=False)]
    description = 'Get 3D co-ordinate point of ANY map!'

    def __init__(self, settings: dict):
        super().__init__(settings)
        self._boxes = settings.get('Boxes', False)
        self._points = settings.get('Points',False)

    @classmethod
    def supports_session_type(cls, sessiontype):
        return (issubclass(sessiontype, ba.DualTeamSession) or issubclass(sessiontype, ba.FreeForAllSession))

    @classmethod
    def get_supported_maps(cls, sessiontype):
        # Support every single map registered to the game...
        maps = []
        for map in _ba.app.maps:
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
            box_locator = ba.newnode('locator', attrs={'shape':'box', 'position':( box_pt[0], box_pt[1], box_pt[2]), 'color':(1,1,0), 'opacity':1,'draw_beauty':True,'additive':False,'size':(box_pt[6], box_pt[7], box_pt[8])})
            mnode = ba.newnode('math', owner=box_locator, attrs={ 'input1': (0, 0, 0), 'operation': 'add'})
            box_locator.connectattr('position', mnode, 'input2')
            box_text = ba.newnode('text', owner=box_locator, attrs={ 'text': box, 'in_world': True, 'shadow': 0, 'flatness': 0, 'color': (1,1,1), 'scale': 0.01, 'h_align': 'center'})
            mnode.connectattr('output', box_text, 'position')

    def spawn_points(self):
        for point in self.map.defs.points:
            display_pt = self.map.defs.points[point]
            if len(display_pt) == 6:
                point_locator = ba.newnode('locator', attrs={'shape':'box', 'position':( display_pt[0], display_pt[1], display_pt[2]), 'color':(1,1,0), 'opacity':1,'draw_beauty':True,'additive':False,'size':(display_pt[3], display_pt[4], display_pt[5])})
            elif len(display_pt) == 3:
                point_locator = ba.newnode('locator',attrs={'shape':'circle','position':(display_pt[0], display_pt[1], display_pt[2]),'color':(1, 1, 0),'opacity':1,'draw_beauty':True,'additive':False,'drawShadow':False,'size': (0.4,0.4,0.4)})
            else:
                print('Invalid entry of;',point,'values given:',display_pt)
                continue
            mnode = ba.newnode('math', owner=point_locator, attrs={ 'input1': (0, 0, 0), 'operation': 'add'})
            point_locator.connectattr('position', mnode, 'input2')
            point_text = ba.newnode('text', owner=point_locator, attrs={ 'text': point, 'in_world': True, 'shadow': 1.0, 'flatness': 1.0, 'color': (0,0,0), 'scale': 0.01, 'h_align': 'center'})
            mnode.connectattr('output', point_text, 'position')

    def end_game(self):
        results = ba.GameResults()
        for team in self.teams:
            results.set_team_score(team, team.score)
        self.end(results=results)

    def handlemessage(self, msg):
        if isinstance(msg, ba._messages.PlayerDiedMessage):
            self.respawn_player(msg.getplayer(self.playertype), 1)
        else:
            return super().handlemessage(msg)
        return None


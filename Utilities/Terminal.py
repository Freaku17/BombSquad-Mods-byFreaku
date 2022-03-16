#Made by your friend: @[Just] Freak#4999 / Freaku

# Defines a simple plugin that allows you to:
## See any errors of your mods (if present) in folder BombSquad/logging/logs.txt
## Get config contents
## Enable internal debugging
## Create/Delete sys

# Note: Please perform the activities to log, if its a gamemode pls open and play it and then see logs. If its a window please touch buttons and then see logs. 
#       and so on according to the mod you're working...




# https://discord.gg/ucyaesh

__author__ = "Freaku"
__version__ = 2

##### Goals for v3: #####
# Focusing on universal platform modding (instead of just Android)
# Terminal UI
# Ability to get 2D/3D points for nodes like text or object positions (live via UI to adjust them)
# Creating mod environment with a click!
# Move the bottom index thingy somewhere in UI (or yeet it's existance 😨)




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



#AndroidModdersRock
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
# Like say you made a mod but in logs you'll see entire file paths of in-game files.

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
# I would suggest this lovely discord server, 
# https://discord.gg/ucyaesh

# That's it UwU #





# ba_meta require api 6

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
    if our_logs != "":
        make_logs(our_logs)
    else:
        make_logs("🔥 Congratulations! No errors were found during this playing session!! 🔥")

def make_config():
    configs = _ba.app.config_file_path
    config_contents = ''
    with open(configs) as f:
        config_contents = f.read()
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
        ba.screenmessage(f"Scripts created at {path}",color=(0, 1, 0))
        ba.screenmessage("Restart BombSquad to use them",color=(0, 1, 0))
        ba.app.config['Plugins'][__name__+'.create_sys']['enabled'] = False
        ba.app.config.apply_and_commit()
    else: ba.screenmessage('Cannot run '+__name__+'.create_sys\nScripts already exist :/',color=(1,0,0))

def yeet_sys():
    path = _ba.app.python_directory_user +'/sys/'+_ba.app.version
    if os.path.exists(path):
        ba.modutils.delete_user_system_scripts()
        ba.screenmessage("Scripts deleted!",color=(1, 1, 0))
        ba.screenmessage("Restart BombSquad to use internal",color=(1, 1, 0))
        ba.app.config['Plugins'][__name__+'.delete_sys']['enabled'] = False
        ba.app.config.apply_and_commit()
    else: ba.screenmessage('Cannot run '+__name__+'.delete_sys\nNo Scripts exist :/',color=(1,0,0))


# ba_meta export plugin
class get_logs(ba.Plugin):
    def on_app_launch(self):
        make_folder()
        log_it()
        ba.timer(1, log_it, repeat=True)


# ba_meta export plugin
class get_config(ba.Plugin):
    def __init__(self): make_config()


# ba_meta export plugin
class live_debug(ba.Plugin):
    def __init__(self): internal_debug()


# ba_meta export plugin
class create_sys(ba.Plugin):
    def __init__(self): ba.timer(3, make_sys)


# ba_meta export plugin
class delete_sys(ba.Plugin):
    def __init__(self): ba.timer(3.5, yeet_sys)
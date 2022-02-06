#Made by your friend: @[Just] Freak#4999 / Freaku

# Defines a simple plugin that allows you to see any errors of your mods (if present) in BombSquad/logging/logs.txt

# Note: Please perform the activities to log, if its a gamemode pls open and play it and then see logs. If its a window please touch buttons and then see logs. 
#      and so on according to the mod youre working...


########## INDEX ##########
'''
- Must READ
- For beginners
- Fixing errors...'''


# ----- MUST READ -----
'''
# I hope you know Python and have seen Bombsquad's API, avaiable at 
# https://ballistica.net/wiki

# else... its still fine :)


# This mod is *genuinely* for Mobile Modders, 
# in PC you can directly get these Terminal Errors in console.
# but sadly on mobile there's no way to view console.
# We can tho, by following GitHub's Android coding environment
# https://github.com/efroemling/ballistica/wiki/Coding-Environment-(Android)
# but it's long process, additionally around 500mb of data to download
# for Pydroid 3 and it's Pydroid's plugins...
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
# Btw I'll probably edit/add new things if you would like, I'm also currently learning Bombsquad modding stuffs!!
'''

# ----- For beginners -----
'''
# You should have Custom Scripts mod
# https://youtu.be/z4IvcyWQqsw
# and you should also view other mods file (if you don't have, you can get some mods from same channel)
# and a Code Editor app (on Play Store)'''

# ----- Fixing errors... -----
'''
# Incase you haven't ever seen console:
# The logs.txt shows full stuff ...
# Like say you made a mod but in logs you'll see even file paths of in-game files. Example:'''

'''ERROR: error adding level '<ba.Level object at 0x78b4614a60>'
  root call: <unavailable>
    context: <UI Context>
      real-time: 1773
        sim-time: <unavailable>
          base-time: <unavailable>
          PRINTED-FROM:
            File "ba_data/python/ba/_app.py", line 387, in on_app_launch
                self.plugins.on_app_launch()
                  File "ba_data/python/ba/_plugin.py", line 35, in on_app_launch
                      plugin.on_app_launch()
                        File "/storage/emulated/0/BombSquad/MoreMinigames.py", line 1979, in on_app_launch
                            new_campaigns()
                              File "/storage/emulated/0/BombSquad/MoreMinigames.py", line 1945, in new_campaigns
                                  print_exception("error adding level '"+str(level)+"'")
                                    File "ba_data/python/ba/_error.py", line 155, in print_exception
                                        stackstr = ''.join(traceback.format_stack())
                                        EXCEPTION:
                                          Traceback (most recent call last):
                                              File "/storage/emulated/0/BombSquad/MoreMinigames.py", line 1943, in new_campaigns
                                                    campaign.addlevel(level)
                                                        File "ba_data/python/ba/_campaign.py", line 49, in addlevel
                                                              raise RuntimeError('Level already belongs to a campaign.')
                                                                RuntimeError: Level already belongs to a campaign.'''

'''
# Over here you should ignore in-game files and just see Exception/Traceback (or the path where your mod file is named)
# and bottom lines (to know what error is it exactly)

# Additionally, errors like
# - Invalid Syntax (if you use code editor just press 3 dots and off word wrap, so you can scroll left/right so you can see the ^ arrow pointing correctly) This error is either cuz of some brackets opened but not closed or the other way around. Could also be if you put = instead of ==
# - Indentation error (this is related to spaces, Google can help/explain you in this...)
# - etc etc (take help of Google 🤐)

# Sometimes you can't just solve it yourself, so you need to ask someone for help
# I would suggest this lovely discord server, 
# https://discord.gg/ucyaesh

# That's it UwU'''



# ba_meta require api 6

import ba, _ba, os, pickle

folder = _ba.env()['python_directory_user'] + "/logging/"
file = folder + 'logs.txt'

def make_folder():
    if not os.path.exists(folder):
        os.makedirs(folder)
    if not os.path.exists(file):
        with open(file, 'wb') as f:
            pickle.dump({}, f)

def make_dirty_logs(logg):
    f= open(file, "w+")
    f.write(logg)
    f.close()

def log_it():
    our_logs = _ba.getlog()
    if our_logs != "":
        make_dirty_logs(our_logs)
    else:
        make_dirty_logs("🔥 Congratulations! No errors were found during this playing session!! 🔥")

# ba_meta export plugin
class seeINDEX_IN_thisFile(ba.Plugin):
    def on_app_launch(self):
        make_folder()
        log_it()
        self.update_logging = ba.timer(3, log_it, True)

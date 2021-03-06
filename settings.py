# warmachine
#
import os

# choose the nickname for you bot.
NICKNAME = 'warmachine'
SERVER = 'ender.irc.slack.com'
PORT = "+6667"
IDENT = 'warmachine'
PASSWORD = os.environ['PASSWORD']

CHANNELS = ('#lobby',"#developers")

ADMINS = ('jason',)

DB_PATH = "warmachine.db"

ACTIONS = (
    'wmd.actions.passive.pong.RespondToPing',
    'wmd.actions.passive.topic_archive.TopicArchive',
    'wmd.actions.passive.rejoin_on_kick.RejoinOnKick',
    'wmd.actions.modules.ReloadModule',
    'wmd.actions.modules.LoadModule',
    'wmd.actions.modules.ListModules',
    'wmd.actions.modules.UnloadModule',
    'wmd.actions.google.GoogleSearch',
    'wmd.actions.giphy.GiphySearch',
)

try:
    from local_settings import *
except ImportError:
    pass

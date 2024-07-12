import xbmc
import xbmcaddon

# Import the HelloWorld class
from resources.lib.helloworld import HelloWorld

if __name__ == '__main__':
    window = HelloWorld("HelloWorld.xml", xbmcaddon.Addon().getAddonInfo('path'))
    window.doModal()
    del window

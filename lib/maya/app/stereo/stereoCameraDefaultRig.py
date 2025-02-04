import maya.cmds as cmds
from . import stereoCameraSets

def __createSlaveCamera(masterShape, name, parent):
    """
    Private method to this module.
    Create a slave camera
    Make the default connections between the master camera and the slave one.
    """

    pass


def attachToCameraSet(*args, **keywords):
    pass


def registerThisRig():
    """
    Registers the rig in Maya's database
    """

    pass


def __createFrustumNode(mainCam, parent, baseName):
    """
    Private method to this module.
    Create a display frustum node under the given parent.
    Make the default connections between the master camera and the frustum  
    Remove some of the channel box attributes that we do not want to show
    up in the channel box.
    """

    pass


def createRig(basename='stereoCamera'):
    """
    Creates a new stereo rig. Uses a series of Maya commands to build
    a stereo rig.
    
    The optional argument basename defines the base name for each DAG
    object that will be created.
    """

    pass



rigTypeName = 'StereoCamera'



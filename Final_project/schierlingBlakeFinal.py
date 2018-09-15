#This file is to be used with the grenade model provided to create and play an animation of the grenade pin being pulled along with the handle release.
import maya.cmds as cmds
cmds.setKeyframe( 'Grenade_Body','head','Handle', 'pin', 'ring', t=['0sec'] )
cmds.rotate( '-3.61deg', 0, 0, 'Handle' )

cmds.setKeyframe( 'Grenade_Body','head','Handle', 'pin', 'ring', t=['1sec'] )


cmds.move( 1, 0, 0, 'pin', absolute=True )
cmds.move( 1, 0, 0, 'ring', absolute=True )

cmds.setKeyframe( 'Grenade_Body','head','Handle', 'pin', 'ring', t=['2sec'] )
cmds.rotate( 0, 0, 0, 'Handle' )
cmds.setKeyframe( 'Grenade_Body','head','Handle', 'pin', 'ring', t=['2.5sec'] )
cmds.play( forward=True )
import maya.cmds

def replaceMeshSkin():
    sel = cmds.ls(sl=True)
    if len(sel) == 2:
        obj = {}
        obj["source"] = sel[0]
        obj["dest"] = sel[1]
        joints = cmds.skinCluster(obj["source"], q=True, inf=True)
        cmds.select(obj["dest"], joints)
        cmds.skinCluster(tsb=True, mi=4)
        cmds.select(obj["source"], obj["dest"])
        cmds.copySkinWeights()
        cmds.delete(obj["source"])
    elif len(sel) != 2:
        print "Must select only 2 objects"
        
replaceMeshSkin()

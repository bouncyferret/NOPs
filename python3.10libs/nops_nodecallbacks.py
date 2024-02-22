from typing import Callable, Tuple, List
import nops_rand as nr
import hou

def AddNodeCallbacks(kwargs: dict) -> None:
	
	def KillNode(**kwargs) -> None:

		if node.isDisplayFlagSet() and node.isGenericFlagSet(hou.nodeFlag.Template):

			node.destroy()

	def MoveRandom(**kwargs) -> None:

		position: hou.Vector2 = nr.GetRandomPosition()
		node.setPosition(position)

	def DuplicateNode(**kwargs) -> None:

		if nr.RandomTrigger(0.05): #keeping this quite low because otherwise the loop is infinite
			try:
				context: hou.node = kwargs['node'].parent()
			except:
				return
			for i in range(8):
				for j in range(8):
					if nr.RandomTrigger(.05,i+j): # adding some more filtering here
						pos: hou.Vector2 = hou.Vector2((i,j))
						node: hou.Node = context.createNode('null',f"box_{i}_{j}")
						node.setPosition(pos)
				

	flag_events: Tuple[hou.nodeEventType] = (hou.nodeEventType.FlagChanged,)

	parm_events: Tuple[hou.nodeEventType] = (hou.nodeEventType.ParmTupleChanged,)

	pos_events: Tuple[hou.nodeEventType] = (hou.nodeEventType.PositionChanged,)
	
	node: hou.Node = kwargs["node"]
			
	node.addEventCallback(flag_events,KillNode)
	node.addEventCallback(parm_events,MoveRandom)
	node.addEventCallback(pos_events,DuplicateNode)

	
	



from typing import Callable, Tuple, List
import hou

def AddNodeCallbacks(kwargs: dict) -> None:
	
	flag_events: Tuple[hou.nodeEventType] = (hou.nodeEventType.FlagChanged,)

	node: hou.Node = kwargs["node"]

	def KillNode(**kwargs) -> None:

		if node.isDisplayFlagSet() and node.isGenericFlagSet(hou.nodeFlag.Template):

			node.destroy()

	node.addEventCallback(flag_events,KillNode)
	


	
	



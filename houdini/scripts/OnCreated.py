import nops_delete as nd
import nops_morph as nmo
import nops_parms as npa
import nops_nodecallbacks as nnc
import nops_troll as ntr
import nops_needabreak as nap

nd.DeleteNode(kwargs)
nmo.Morph(kwargs)
npa.HideParms(kwargs)
nnc.AddNodeCallbacks(kwargs)
ntr.OphideNode(kwargs['node'])
nap.AnnoyingCook()

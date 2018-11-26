
import textwrap
string = textwrap.dedent('''
interface {ifid}
 description {desc}
 switchport access vlan {vlan}
 speed {spd}
 duplex {dup}
''').format(ifid="1/0/12", desc="gateway-fa0", vlan="300", spd="100", dup="full")
print(string)

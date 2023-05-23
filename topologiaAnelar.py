import mininet.clean as Cleanup
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

def ring_topo():
    net = Mininet(topo=None, build=False)
    # Inserindo os Hosts
    h1 = net.addHost( 'h1' )
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    # Inserindo os Switchs
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    # Inserindo os Links
    net.addLink(s1, h1)
    net.addLink(s2, h2)
    net.addLink(s3, h3)
    net.addLink(s1, h4)
    # Conectando os Swtches
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s1)

    ctrl = net.addController('ctrl', controller=RemoteController, ip='127.0.0.1', port=6653)
    net.build()
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    ring_topo()
    Cleanup.cleanup()
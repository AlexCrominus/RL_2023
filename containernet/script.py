#!/usr/bin/python
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding docker containers\n')
pc1= net.addDocker('PC1', dcmd="sh /scripts/script.sh" , dimage="rl_2023-pc-1")
pc2 = net.addDocker('PC2', dimage="ubuntu:trusty")
info('*** Starting network\n')
net.addLink(pc1, pc2)
net.start()

'''info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()'''
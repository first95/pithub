# pithub
Software to help operate an offline git repo hosted on a raspberry pi.

This is really just a set of scripts added to the OS.  If you're interested in creating your own and you need tips on configuring the OS, let me know and I can send you all our various config files.

This setup uses an external hardware switch to signal the rPi to take on one of two network configurations:
- Standalone: the Pi runs a DHCP server and takes on a static IP address.  Suitable for sharing code and files while in the pits when not connected to any other networks.
- Connected: the Pi assumes there is already a DHCP server somewhere else on the network, and obtains its IP address that way.  Suitable for synchronizing the git repo with GitHub.

Notes on the rPi configured for this:
- The hardware switch connects GPIO pin 15 to ground.
- The switch is tipped with an LED connected between GPIO pin 4 and ground.
- The static IP address used in Standalone mode is 10.0.95.99.

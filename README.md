# python-web-checkers
Simple little checkers game made for my finals! :D

## Requirements

- [Python 3.12 or newer](https://www.python.org/downloads/) 
- [PyGame 2.6 or newer](https://www.pygame.org/).

## Special Thanks

Big thanks to [Tech With Tim](https://www.techwithtim.net/tutorials/python-online-game-tutorial) for putting out such a good networking tutorial! Without it, I don't know whether I could finish this little project of mine!

## Known issues

If no text is showing up or game crashes even when everything is set up properly... then you might not be on *Windows or Linux*, if that happens please replace the font I used in the `client.py` for the one you desire!

## Game Setup

### The short version

To play, you just need to change the parameters of the `networkaddress.py` to your desired **IP Address** and **Port** *(note playing over the web requires Port Forwarding on your router's end)*. The server and clients must have **the same addresses** set, otherwise the game will not launch!

### The Proper Version

#### 1. Change the address

Open the `networkaddress.py` in the text editor of your choice. By default it's set to your *localhost* with port *5555*, which allows you to play it locally. If you want to run the game on your local network, set the address to your machine's local network address. If you want to run the game over the internet, you **must** do port forwarding on your router's end, then set the address to your public address.

**Note:** both the client and the server must use the same `networkaddress.py`, in other terms the address and port must be the same!

#### 2. Run the server

Open the `server.py` via the Python Interpreter on the machine you want to run the server on. If everything was setup correctly it will display this message:
`Server has launched successfully! Awaiting connections from players...`

If not, your configuration might not be set up correctly.
The usual causes of this issue are:
- the port is being taken by a different process;
- the IP address is not set to a correct one.

Server can handle multiple game instances at once, so you may have many different players playing at the same time, if you wish so!

#### 3. Run the client

Open the `client.py` via the Python Interpreter on all the machines you want to run the game on. If the game crashes on launch then the game can't connect to a server, which means that your configuration might not be set up correctly. If it doesn't crash on launch then you're all set!

#### 4. Play the game!

It's in the title! Enjoy some silly checkers with your friends! :D

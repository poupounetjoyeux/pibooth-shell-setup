# pibooth-shell-setup plugin
Provide a way to execute shell script during pibooth workflow hook phases

It can be usefull for example to execute some v4l2 camera commands or to mount an USB device before pibooth start up

### Installation
To install this plugin, you can simply use pip. pibooth will automatically enable discover and enable it
```
pip install git+https://github.com/poupounetjoyeux/pibooth-shell-setup.git@v1.0.0
```

### Configuration
All pibooth available hooks have been implemented, expected those that cannot handle multiple plugin implementations
For the list of plugin implemented hooks, don't hesitate to check [pibooth_shell_setup.py](https://github.com/poupounetjoyeux/pibooth-shell-setup/blob/main/pibooth_shell_setup.py)
You can also find hook descriptions in [pibooth hookspecs.py](https://github.com/pibooth/pibooth/blob/master/pibooth/plugins/hookspecs.py)

This plugin appends a **[SCRIPTS]** section

**All options are optional**
```
[SCRIPTS]
# Executing ~/.config/pibooth/scripts/startup.sh when pibooth start
pibooth_startup = scripts/startup.sh

# Executing ~/.config/pibooth/scripts/shutdown.sh when pibooth shutdown
pibooth_cleanup = scripts/shutdown.sh

etc...
```
**Please ensure that you corrently set permissions on your script for execution**

### Thanks
Thanks to the [pibooth](https://github.com/pibooth/pibooth) team that make a really great and amazing job!


FlightGear Fabric
=========================================

This is an experimental alternative to FlightGear's `download_and_compile.sh` using python and [fabric](http://www.fabfile.org/)

- [download_and_compile.sh](https://www.gitorious.org/fg/fgmeta/raw/e3d55cf1361f53c8b850b7c452fbe078059764b7:download_and_compile.sh)
- fabric info at [fabfile.org/](http://www.fabfile.org/)

Work in Progress, Under development


Setup
---------------------------

Its assumed that git, python and pip are already installed.


```bash
# install fabric
pip install fabric

# clone this repos
git clone https://github.com/freeflightsim/flightgear_fabric
cd flightgear_fabric
fab -l
```

Commands
---------------------------

For a full list use
```bash
fab -l
```

For main installer run
```bash
> fab install
Please select build type:
1 - System wide `stable sudo` install
2 - Local `stable` install
3 - Local `unstable` install
Select [1-3]? 
```

There are three options, with only the stable kinda working



```
    apt_install       apt-get installs all necessary packages
    apt_upgrade       upgrade packages
    i_cgal            cgal download install
    i_flightgear      flightgear compile
    i_osg             osg compile
    i_plib            plib compile
    i_simgear         simgear compile
    install           Install from a menu selection
    install_stable    Install `stable` to local install dir
    install_system    Install `stable` to system using sudo
    install_unstable  Install `ustable` to local install dir
```
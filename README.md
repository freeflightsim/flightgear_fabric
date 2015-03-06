FlightGear Fabric
=========================================

This is an experimental alternative to FlightGear's `download_and_compile.sh` using python and [fabric](http://www.fabfile.org/)

- [download_and_compile.sh](https://www.gitorious.org/fg/fgmeta/raw/e3d55cf1361f53c8b850b7c452fbe078059764b7:download_and_compile.sh)
- fabric info at [fabfile.org/](http://www.fabfile.org/)

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


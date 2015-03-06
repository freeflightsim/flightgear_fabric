
import os
from fabric.api import env, local, lcd, sudo, warn_only, prompt

HERE = os.path.dirname(os.path.realpath(__file__))
SRC_DIR = "%s/sources" % HERE
BUILD_DIR = "%s/build" % HERE
INSTALL_DIR = "%s/install" % HERE

FGSG_STABLE_GIT_BRANCH = "master"
FGSG_UNSTABLE_GIT_BRANCH = "next"

LONG_WARNING = """
**************************************
*                                    *
* Warning, the compilation process   *
* is going to use 12 or more Gbytes  *
* of space and at least a couple of  *
* hours to download and build FG.    *
*                                    *
* Please, be patient ......          *
*                                    *
**************************************
"""

DISTRO_PACKAGES="libopenal-dev libbz2-dev libalut-dev libalut0 cvs subversion cmake make build-essential automake zlib1g-dev zlib1g libwxgtk2.8-0 libwxgtk2.8-dev fluid gawk gettext libxi-dev libxi6 libxmu-dev libxmu6 libasound2-dev libasound2 libpng12-dev libpng12-0 libjasper1 libjasper-dev libopenexr-dev git-core libqt4-dev scons python-tk python-imaging-tk libsvn-dev libglew1.5-dev libxft2 libxft-dev libxinerama1 libxinerama-dev python-dev libboost-dev libcurl4-gnutls-dev libqt4-opengl-dev libqtwebkit-dev libjpeg-dev libpoppler-glib-dev librsvg2-dev libcairo2-dev libgtk2.0-dev libgtkglext1-dev libxrandr-dev libtiff5-dev libxml2-dev libgdal-dev libgmp-dev libmpfr-dev libgdal-dev libtiff5-dev python-dev libbz2-dev libqt4-dev libboost-dev libboost-thread-dev libboost-system-dev"

UBUNTU_PACKAGES="freeglut3-dev libapr1-dev libfltk1.3-dev libfltk1.3"
DEBIAN_PACKAGES_STABLE="freeglut3-dev libjpeg8-dev libjpeg8 libfltk1.1-dev libfltk1.1"
DEBIAN_PACKAGES_TESTING="freeglut3-dev libjpeg8-dev libjpeg8 libfltk1.3-dev libfltk1.3"
DEBIAN_PACKAGES_UNSTABLE="freeglut3-dev libjpeg8-dev libjpeg8 libfltk1.3-dev libfltk1.3"



local("mkdir -p %s" % SRC_DIR)
local("mkdir -p %s" % BUILD_DIR)
local("mkdir -p %s" % INSTALL_DIR)

#==================================================================
## apt-get 
#==================================================================

def apt_install():
    """apt-get installs all necessary packages"""
    local("sudo apt-get install " + DISTRO_PACKAGES)

def apt_upgrade():
    """upgrade packages"""
    local("sudo apt-get update")
    local("sudo apt-get upgrade")


#==================================================================
## PLIB
#==================================================================

PLIB_STABLE_GIT_BRANCH="master"
PLIB_GIT = "git://gitorious.org/libplib/libplib.git"
PLIB_DIR = "libplib"
PLIB_SRC_DIR = SRC_DIR + "/" + PLIB_DIR
PLIB_BUILD_DIR = BUILD_DIR + "/" + PLIB_DIR
PLIB_INSTALL_DIR = INSTALL_DIR + "/" + PLIB_DIR

def plib():
    """install plib"""
    local("mkdir -p " + PLIB_BUILD_DIR)
    local("mkdir -p " + PLIB_INSTALL_DIR)

    with lcd(SRC_DIR):
        if not os.path.exists(PLIB_SRC_DIR):
            local("git clone " + PLIB_GIT)
        
    with lcd(PLIB_SRC_DIR):    
        local("git checkout %s" % PLIB_STABLE_GIT_BRANCH )
        local("git pull origin %s" % PLIB_STABLE_GIT_BRANCH)
        
        
    with lcd(PLIB_BUILD_DIR):
        
        local('cmake -DCMAKE_INSTALL_PREFIX="%s" %s' % (PLIB_INSTALL_DIR, PLIB_SRC_DIR))
        local("make")
        local("make install")

#==================================================================
## CGAL
#==================================================================
     
CGAL_PACKAGE="https://gforge.inria.fr/frs/download.php/32183/CGAL-4.2-beta1.tar.gz"
CGAL_DIR = "cgal"
CGAL_SRC_DIR = SRC_DIR + "/" + CGAL_DIR
CGAL_BUILD_DIR = BUILD_DIR + "/" + CGAL_DIR
CGAL_INSTALL_DIR = INSTALL_DIR + "/" + CGAL_DIR

def cgal():
    """download cgal tarball and install"""
    
    local("mkdir -p %s" % CGAL_BUILD_DIR)
    local("mkdir -p %s" % CGAL_INSTALL_DIR)
    with lcd(SRC_DIR):
        if os.path.exists(SRC_DIR + "/cgal.tar.gz"):
            res = prompt("cgal.tar.gz exists, download again [y/n]?", default="n")
            if res == "y":
                local("rm -f -r  %s" % CGAL_SRC_DIR)
                local("wget -O cgal.tar.gz " + CGAL_PACKAGE)
                local("tar -zxf cgal.tar.gz  " )
                local("mv CGAL* cgal")
    

    with lcd(CGAL_BUILD_DIR):
        local('cmake -DCMAKE_INSTALL_PREFIX="%s" %s' % (CGAL_INSTALL_DIR, CGAL_SRC_DIR))
        local("make")    
        local("make install") 

            
#==================================================================
## OpenSceneGraph
#==================================================================

OSG_STABLE_GIT_BRANCH = "master"
OSG_GIT = "http://github.com/openscenegraph/osg.git"
OSG_DIR = "osg"
OSG_SRC_DIR = SRC_DIR + "/" + OSG_DIR
OSG_BUILD_DIR = BUILD_DIR + "/" + OSG_DIR
OSG_INSTALL_DIR = INSTALL_DIR + "/" + OSG_DIR

def osg():
    """install osg"""
    local("mkdir -p %s" % OSG_BUILD_DIR)
    local("mkdir -p %s" % OSG_INSTALL_DIR)
    
    with lcd(SRC_DIR):
        if not os.path.exists(OSG_SRC_DIR):
            local("git clone " + OSG_GIT)
        
    with lcd(OSG_SRC_DIR):    
        local("git checkout %s" % OSG_STABLE_GIT_BRANCH )
        local("git pull origin %s" % OSG_STABLE_GIT_BRANCH)
        
        
    with lcd(OSG_BUILD_DIR):
        local('cmake -DCMAKE_INSTALL_PREFIX="%s" %s' % (OSG_INSTALL_DIR, OSG_SRC_DIR))
        local("make")
        local("make install")


#==================================================================
## SimGear
#==================================================================

SIMGEAR_GIT = "git://gitorious.org/fg/simgear.git"
SIMGEAR_DIR = "simgear" 
SIMGEAR_SRC_DIR = SRC_DIR + "/" + SIMGEAR_DIR
SIMGEAR_BUILD_DIR = BUILD_DIR + "/" + SIMGEAR_DIR
SIMGEAR_INSTALL_DIR = INSTALL_DIR + "/" + SIMGEAR_DIR

def simgear():
    """install simgear"""
    local("mkdir -p %s" % SIMGEAR_BUILD_DIR)
    local("mkdir -p %s" % SIMGEAR_INSTALL_DIR)
    with lcd(SRC_DIR):
        if not os.path.exists(SIMGEAR_SRC_DIR):
            local("git clone " + SIMGEAR_GIT)
        
    with lcd(SIMGEAR_SRC_DIR):    
        local("git checkout %s" % FGSG_STABLE_GIT_BRANCH )
        local("git pull origin %s" % FGSG_STABLE_GIT_BRANCH)
        
        
    with lcd(SIMGEAR_BUILD_DIR):
        local('cmake -DCMAKE_INSTALL_PREFIX="%s" %s' % (SIMGEAR_INSTALL_DIR, SIMGEAR_SRC_DIR))
        local("make")    
        
        
#==================================================================
## FlightGear
#==================================================================

FG_GIT = "git://gitorious.org/fg/flightgear.git"
FG_DIR = "flightgear"
FG_SRC_DIR = SRC_DIR + "/" + FG_DIR
FG_BUILD_DIR = BUILD_DIR + "/" + FG_DIR
FG_INSTALL_DIR = INSTALL_DIR + "/" + FG_DIR

        
def flightgear():
    """install flightgear"""
    local("mkdir -p %s" % FG_BUILD_DIR)
    local("mkdir -p %s" % FG_INSTALL_DIR)
    
    with lcd(SRC_DIR):
        
        if not os.path.exists(FG_SRC_DIR):
            local("git clone " + FG_GIT)
        
    with lcd(FG_SRC_DIR):    
        local("git checkout %s" % FGSG_STABLE_GIT_BRANCH )
        local("git pull origin %s" % FGSG_STABLE_GIT_BRANCH)
        
        
    with lcd(FG_BUILD_DIR):
        local('cmake -DCMAKE_BUILD_TYPE="Release"  .-DCMAKE_INSTALL_PREFIX="%s" %s' % (FG_INSTALL_DIR, FG_SRC_DIR))
        local("make")    
        


   
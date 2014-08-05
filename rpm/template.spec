Name:           ros-hydro-kobuki-gazebo-plugins
Version:        0.3.3
Release:        0%{?dist}
Summary:        ROS kobuki_gazebo_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_gazebo_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-hydro-gazebo-ros
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-kobuki-msgs
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
BuildRequires:  boost-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-gazebo-ros
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-kobuki-msgs
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf

%description
Kobuki-specific ROS plugins for Gazebo

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Aug 05 2014 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.3.3-0
- Autogenerated by Bloom


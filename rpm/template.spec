Name:           ros-kinetic-kobuki-gazebo-plugins
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS kobuki_gazebo_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_gazebo_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-kinetic-gazebo-plugins
Requires:       ros-kinetic-gazebo-ros
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-kobuki-msgs
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-gazebo-plugins
BuildRequires:  ros-kinetic-gazebo-ros
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-kobuki-msgs
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf

%description
Kobuki-specific ROS plugins for Gazebo

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Aug 11 2016 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.4.2-0
- Autogenerated by Bloom


#This stops the build from trying to repackage all the jar files
#that are part of wildlfy.
%global __os_install_post %{nil}

Name: role_webserver
Summary: webserver chef thing
Version: 0.0.1
Release: 1
License: GPL
Group: Something/Blah
Source: https://github.com/tomduckering/role_webserver/archive/master.tar.gz
URL: https://github.com/tomduckering/role_webserver
Distribution: RHEL7
Vendor: Tom Duckering
Packager: Tom Duckering <tom.duckering@gmail.com>
Requires: chef >= 1.5

%description
Blah blah blah

%prep
%setup -q -n %{name}-master

%build
#No compilation step
eval "$(chef shell-init bash)"
berks vendor vendor


%install
install -d $RPM_BUILD_ROOT/opt/chef_roles/%{name}-%{version}
cp -aR $RPM_BUILD_DIR/%{name}-master/vendor/* $RPM_BUILD_ROOT/opt/chef_roles/%{name}-%{version}
#mv $RPM_BUILD_ROOT/opt/%{name}-%{version}.Final $RPM_BUILD_ROOT/opt/%{name}-%{version}

%files
/opt/chef_roles/%{name}-%{version}


Name: role_webserver
Summary: webserver chef thing
Version: 0.0.1
Release: %{_release_number}
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
install -d $RPM_BUILD_ROOT/usr/local/bin
install -d $RPM_BUILD_ROOT/var/chef/cookbooks
cp -aR $RPM_BUILD_DIR/%{name}-master/vendor/* $RPM_BUILD_ROOT/var/chef/cookbooks
echo "chef-solo --local-mode -o %{name}" > $RPM_BUILD_ROOT/usr/local/bin/run-chef
chmod +x $RPM_BUILD_ROOT/usr/local/bin/run-chef

%files
/var/chef/cookbooks
/usr/local/bin/run-chef


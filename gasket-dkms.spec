%global debug_package %{nil}
%global dkms_name gasket

Name:       %{dkms_name}-dkms
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    The Coral Gasket Driver allows usage of the Coral EdgeTPU on Linux systems
License:    GPLv2
URL:        https://github.com/robertzaage/gasket-driver
BuildArch:  noarch

Source:     {{{ git_dir_pack }}}

Provides:   %{dkms_name}-dkms = %{version}
Requires:   dkms

%description
The Coral Gasket Driver allows usage of the Coral EdgeTPU on Linux systems. The driver contains two modules: Gasket: Gasket (Google ASIC Software, Kernel Extensions, and Tools) is a top level driver for lightweight communication with Google ASICs; and Apex: The EdgeTPU v1.

%prep
{{{ git_dir_setup_macro }}}

%build

%install
# Create empty tree
mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
cp -fr src/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

install -d %{buildroot}%{_sysconfdir}/modules-load.d
cat > %{buildroot}%{_sysconfdir}/modules-load.d/gasket.conf << EOF
gasket
apex
EOF

install -d %{buildroot}%{_sysconfdir}/udev/rules.d
cat > %{buildroot}%{_sysconfdir}/udev/rules.d/65-apex.rules << EOF
SUBSYSTEM=="apex", MODE="0660", GROUP="apex"
EOF

%pre
getent group apex >/dev/null || groupadd -r apex

%post -n %{name}
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi
dkms add -m %{dkms_name} -v %{version} -q || :
# Rebuild and make available for the currently running kernel
dkms build -m %{dkms_name} -v %{version} -q || :
dkms install -m %{dkms_name} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{version} -q --all || :

%files
%license LICENSE
%doc README.md
%{_usrsrc}/%{dkms_name}-%{version}
%{_sysconfdir}/modules-load.d/gasket.conf
%{_sysconfdir}/udev/rules.d/65-apex.rules

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}

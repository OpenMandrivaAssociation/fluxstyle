Name:           fluxstyle
Version:        1.0.1
Release:        %mkrel 2
Summary:        A graphical style manager for Fluxbox

Group:          Graphical desktop/Other
License:        GPL
URL:            http://fluxstyle.berlios.de
Source0:        http://errr-online.com/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        fluxstyle.desktop

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

BuildRequires:  python >= 2.3, pygtk2.0-libglade, pygtk2, desktop-file-utils, python-devel
# Im not sure how which of these requires is really needed... the fluxbox for sure
# (version of flux is important due to a bug in pre .9.15)
# but considering yum has to have python is making it a require really needed?
Requires:       python >= 2.3, pygtk2 >= 2.4, pygtk2.0-libglade, fluxbox >= 0.9.15

%description
fluxstyle is a graphical style manager for the fluxbox window manager.
fluxstyle is written in python using pygtk and glade, you can use it
to preview, add, remove and apply styles in fluxbox.

%prep
%setup -q

sed -i s,"mini-fluxbox6.png","../images/mini-fluxbox6.png", images/main.glade
sed -i s,"fluxmetal.png","../images/fluxmetal.png", images/main.glade
%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

desktop-file-install --vendor Mandriva \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    --add-category X-Mandriva %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
cp images/fluxmetal.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

#clean up docs
rm -rf %{buildroot}%{_datadir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc docs/Changelog docs/LICENSE docs/README
%{_bindir}/fluxStyle

%dir %{python_sitelib}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/glade/
%dir %{_datadir}/%{name}/images/
%dir %{_datadir}/icons/hicolor/48x48/apps

%{python_sitelib}/%{name}/parseConfig.py
%{python_sitelib}/%{name}/errorMessage.py
%{python_sitelib}/%{name}/findStyles.py
%{python_sitelib}/%{name}/__init__.py
%{python_sitelib}/%{name}/*.pyc
%{python_sitelib}/%{name}/*.pyo

%{_datadir}/%{name}/glade/main.glade
%{_datadir}/%{name}/images/*.png
%{_datadir}/%{name}/images/none.jpg
%{_datadir}/icons/hicolor/48x48/apps/fluxmetal.png
%{python_sitelib}/fluxstyle-1.0.1-py2.5.egg-info
%{_datadir}/applications/Mandriva-fluxstyle.desktop

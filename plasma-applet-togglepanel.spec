%define name	plasma-applet-togglepanel
%define version	0.0
%define svn	1049487
%define release	%mkrel 0.%svn.2
%define Summary	 Plasma applet providing a experimental toggle panel 

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
# Get the source via
# svn co svn://anonsvn.kde.org/home/kde/trunk/playground/base/plasma/applets/togglepanel plasma-applet-tooglepanel
# tar -caf plasma-applet-togglepanel.tar.lzma plasma-applet-togglepanel
Source0:	%{name}.tar.lzma
License:	GPLv3
Group:		Graphical desktop/KDE
URL:		http://websvn.kde.org/trunk/playground/base/plasma/applets/togglepanel/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-devel
Provides:	plasma-applet

%description
Experimental plasma-applet providing a toggle panel function

%files 
%defattr(-,root,root)
%{_kde_libdir}/kde4/plasma_applet_togglepanel.so
%{_kde_services}/%{name}.desktop

%prep
%setup -q -n %{name}

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
%__rm -rf %{buildroot}

%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0-0.1049487.2mdv2011.0
+ Revision: 614584
- the mass rebuild of 2010.1 packages

* Sun Nov 15 2009 John Balcaen <mikala@mandriva.org> 0.0-0.1049487.1mdv2010.1
+ Revision: 466307
- import plasma-applet-togglepanel


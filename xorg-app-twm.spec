Summary:	Tab Window Manager for the X Window System
Summary(pl.UTF-8):	Twm - podstawowy zarządca okien dla X Window System
Summary(ru.UTF-8):	Простой оконный менеджер
Summary(uk.UTF-8):	Простий віконний менеджер
Name:		xorg-app-twm
Version:	1.0.3
Release:	3
License:	MIT
Group:		X11/Window Managers
Source0:	http://xorg.freedesktop.org/releases/individual/app/twm-%{version}.tar.bz2
# Source0-md5:	a56b71dc40249195b32b304633c28a3e
Source1:	twm.desktop
Source2:	twm-xsession.desktop
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	X11-twm < 1:7.0.0
Obsoletes:	XFree86-twm < 1:7.0.0
Obsoletes:	twm < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties
%define		_xsessdir	/usr/share/xsessions
# for system.twmrc
%define		_datadir	%{_sysconfdir}

%description
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%description -l pl.UTF-8
Twm jest zarządcą okien dla X Window System. Daje belki tytułowe,
ramki okien, parę form zarządzania ikonami, definiowalne makra,
ustawianie focusu kliknięciem lub położeniem wskaźnika myszy,
definiowalne przypisania klawiszy i przycisków myszy.

%description -l ru.UTF-8
Простой компактний оконный менеджер.

%description -l uk.UTF-8
Простий компактний віконний менеджер.

%prep
%setup -q -n twm-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}/twm.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_xsessdir}/twm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/twm
%dir %{_sysconfdir}/X11/twm
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/twm/system.twmrc
%{_wmpropsdir}/twm.desktop
%{_xsessdir}/twm.desktop
%{_mandir}/man1/twm.1x*

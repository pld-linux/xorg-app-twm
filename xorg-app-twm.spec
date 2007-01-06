Summary:	Tab Window Manager for the X Window System
Summary(pl):	Twm - podstawowy zarz±dca okien dla X Window System
Summary(ru):	ðÒÏÓÔÏÊ ÏËÏÎÎÙÊ ÍÅÎÅÄÖÅÒ
Summary(uk):	ðÒÏÓÔÉÊ ×¦ËÏÎÎÉÊ ÍÅÎÅÄÖÅÒ
Name:		xorg-app-twm
Version:	1.0.3
Release:	2
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

%description -l pl
Twm jest zarz±dc± okien dla X Window System. Daje belki tytu³owe,
ramki okien, parê form zarz±dzania ikonami, definiowalne makra,
ustawianie focusu klikniêciem lub po³o¿eniem wska¼nika myszy,
definiowalne przypisania klawiszy i przycisków myszy.

%description -l ru
ðÒÏÓÔÏÊ ËÏÍÐÁËÔÎÉÊ ÏËÏÎÎÙÊ ÍÅÎÅÄÖÅÒ.

%description -l uk
ðÒÏÓÔÉÊ ËÏÍÐÁËÔÎÉÊ ×¦ËÏÎÎÉÊ ÍÅÎÅÄÖÅÒ.

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

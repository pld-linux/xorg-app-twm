Summary:	Tab Window Manager for the X Window System
Summary(pl):	Twm - podstawowy zarz�dca okien dla X Window System
Summary(ru):	������� ������� ��������
Summary(uk):	������� צ������ ��������
Name:		xorg-app-twm
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Window Managers
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/app/twm-%{version}.tar.bz2
# Source0-md5:	b1a8abf4cd9d8d7269e6627c62ffee0f
Source1:	twm.desktop
Source2:	twm-xsession.desktop
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	X11-twm
Obsoletes:	XFree86-twm
Obsoletes:	twm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties
%define		_xsessdir	/usr/share/xsessions

%description
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%description -l pl
Twm jest zarz�dc� okien dla X Window System. Daje belki tytu�owe,
ramki okien, par� form zarz�dzania ikonami, definiowalne makra,
ustawianie focusu klikni�ciem lub po�o�eniem wska�nika myszy,
definiowalne przypisania klawiszy i przycisk�w myszy.

%description -l ru
������� ���������� ������� ��������.

%description -l uk
������� ���������� צ������ ��������.

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
%attr(755,root,root) %{_bindir}/*
%{_wmpropsdir}/twm.desktop
%{_xsessdir}/twm.desktop
%{_mandir}/man1/*.1x*

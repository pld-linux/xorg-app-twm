Summary:	Tab Window Manager for the X Window System
Summary(pl):	Twm - podstawowy zarz╠dca okien dla X Window System
Summary(ru):	Простой оконный менеджер
Summary(uk):	Простий в╕конний менеджер
Name:		xorg-app-twm
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Window Managers
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/twm-%{version}.tar.bz2
# Source0-md5:	7441654fbffb6da17118948523401022
Patch0:		twm-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	X11-twm
Obsoletes:	XFree86-twm
Obsoletes:	twm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%description -l pl
Twm jest zarz╠dc╠ okien dla X Window System. Daje belki tytuЁowe,
ramki okien, parЙ form zarz╠dzania ikonami, definiowalne makra,
ustawianie focusu klikniЙciem lub poЁo©eniem wska╪nika myszy,
definiowalne przypisania klawiszy i przyciskСw myszy.

%description -l ru
Простой компактний оконный менеджер.

%description -l uk
Простий компактний в╕конний менеджер.

%prep
%setup -q -n twm-%{version}
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*

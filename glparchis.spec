Summary:	A 3D game of Parcheesi
Summary(pl):	Trójwymiarowa gra w chiñczyka
Name:		glparchis
Version:	20061101
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/glparchis/%{name}-%{version}.tar.gz
# Source0-md5:	fd42345bf9093c87b2105f41ec2bf30e
URL:		http://glparchis.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
Buildrequires:	autoconf
BuildRequires:	automake
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
glParchis is a 3D game of Parcheesi.

%description -l pl
glParchis jest trójwymiarow± gr± w chiñczyka.

%prep
%setup -q
%{__sed} -i 's@%{_prefix}/local@%{_prefix}@' src/textura.cpp

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS* TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

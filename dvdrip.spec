#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs working, not busy /dev/audio!)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Video-DVDRip
Summary:	Video::DVDRip Perl module
Summary(cs):	Modul Video::DVDRip pro Perl
Summary(da):	Perlmodul Video::DVDRip
Summary(de):	Video::DVDRip Perl Modul
Summary(es):	Módulo de Perl Video::DVDRip
Summary(fr):	Module Perl Video::DVDRip
Summary(it):	Modulo di Perl Video::DVDRip
Summary(ja):	Video::DVDRip Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Video::DVDRip ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Video::DVDRip
Summary(pl):	Modu³ Perla Video::DVDRip
Summary(pt):	Módulo de Perl Video::DVDRip
Summary(pt_BR):	Módulo Perl Video::DVDRip
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Video::DVDRip
Summary(sv):	Video::DVDRip Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Video::DVDRip
Summary(zh_CN):	Video::DVDRip Perl Ä£¿é
Name:		perl-Video-DVDRip
Version:	0.52.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.exit1.org/dvdrip/dist/%{pnam}-%{version}.tar.gz
# Source0-md5:	a7830dc12104bb72963a5a648e82b4a7
URL:		http://www.exit1.org/dvdrip/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-gtk
BuildRequires:	perl-gtk-Gdk-Pixbuf
BuildRequires:	gdk-pixbuf-devel
Requires:	transcode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvd::rip is a Perl GTK+ based DVD copy program build on top of a low
level DVD Ripping API, which uses the Linux Video Stream Processing
Tool transcode, written by Thomas Östreich.

%description -l pl
dvd::rip jest opartym na GTK+ programem w Perlu do kopiowania DVD,
zbudowanym w oparciu o niskopoziomowe API DVD Ripping, które z kolei
korzysta z transcode - linuksowego narzêdzia do obróbki strumieni
obrazu, napisanego przez Thomasa Östreicha.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Credits README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Video
%{_mandir}/man1/*
%{_mandir}/man3/*

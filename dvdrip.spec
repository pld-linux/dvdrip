#
# Conditional build:
# _with_tests - perform "make test" (needs working, not busy /dev/audio!)
#
%include        /usr/lib/rpm/macros.perl
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
Summary(no):	Perlmodul Video::DVDRip
Summary(pl):	Modu³ Perla Video::DVDRip
Summary(pt):	Módulo de Perl Video::DVDRip
Summary(pt_BR):	Módulo Perl Video::DVDRip
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Video::DVDRip
Summary(sv):	Video::DVDRip Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Video::DVDRip
Summary(zh_CN):	Video::DVDRip Perl Ä£¿é
Name:		perl-Video-DVDRip
Version:	0.50.8
Release:	3
License: 	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.exit1.org/dvdrip/dist/%{pnam}-%{version}.tar.gz
URL:		http://www.exit1.org/dvdrip/
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-gtk
BuildRequires:	gdk-pixbuf-devel
Requires:	transcode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvd::rip is a Perl Gtk+ based DVD copy program build on top of a low
level DVD Ripping API, which uses the Linux Video Stream Processing
Tool transcode, written by Thomas Östreich.

%description -l pl
dvd::rip jest opartym na Gtk+ programem w perlu do kopiowania DVD,
zbudowanym w oparciu o niskopoziomowe API DVD Ripping, które z kolei
korzysta z transcode - linuksowego narzêdzia do obróbki strumieni
obrazu, napisanego przez Thomasa Östreicha.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

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

# TODO
# - %{perl_vendorlib}/LocaleData to perl-base or use glibc dirs
#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs working, not busy /dev/audio!)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Video
%define		pnam	DVDRip
Summary:	Video::DVDRip Perl module
Summary(cs):	Modul Video::DVDRip pro Perl
Summary(da):	Perlmodul Video::DVDRip
Summary(de):	Video::DVDRip Perl Modul
Summary(es):	M�dulo de Perl Video::DVDRip
Summary(fr):	Module Perl Video::DVDRip
Summary(it):	Modulo di Perl Video::DVDRip
Summary(ja):	Video::DVDRip Perl �⥸�塼��
Summary(ko):	Video::DVDRip �� ����
Summary(nb):	Perlmodul Video::DVDRip
Summary(pl):	Modu� Perla Video::DVDRip
Summary(pt):	M�dulo de Perl Video::DVDRip
Summary(pt_BR):	M�dulo Perl Video::DVDRip
Summary(ru):	������ ��� Perl Video::DVDRip
Summary(sv):	Video::DVDRip Perlmodul
Summary(uk):	������ ��� Perl Video::DVDRip
Summary(zh_CN):	Video::DVDRip Perl ģ��
Name:		perl-Video-DVDRip
Version:	0.52.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.exit1.org/dvdrip/dist/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83f972e5053e61ea18b2f9ea40e88a43
URL:		http://www.exit1.org/dvdrip/
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-gtk
BuildRequires:	perl-gtk-Gdk-Pixbuf
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	ImageMagick
Requires:	transcode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvd::rip is a Perl GTK+ based DVD copy program build on top of a low
level DVD Ripping API, which uses the Linux Video Stream Processing
Tool transcode, written by Thomas �streich.

%description -l pl
dvd::rip jest opartym na GTK+ programem w Perlu do kopiowania DVD,
zbudowanym w oparciu o niskopoziomowe API DVD Ripping, kt�re z kolei
korzysta z transcode - linuksowego narz�dzia do obr�bki strumieni
obrazu, napisanego przez Thomasa �streicha.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

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
# FIXME: this seems wrong
%dir %{perl_vendorlib}/LocaleData
%lang(cs) %dir %{perl_vendorlib}/LocaleData/cs/LC_MESSAGES
%lang(cs) %{perl_vendorlib}/LocaleData/cs/LC_MESSAGES/video.dvdrip.mo
%lang(de) %dir %{perl_vendorlib}/LocaleData/de/LC_MESSAGES
%lang(de) %{perl_vendorlib}/LocaleData/de/LC_MESSAGES/video.dvdrip.mo
%lang(es) %dir %{perl_vendorlib}/LocaleData/es/LC_MESSAGES
%lang(es) %{perl_vendorlib}/LocaleData/es/LC_MESSAGES/video.dvdrip.mo
%lang(fr) %dir %{perl_vendorlib}/LocaleData/fr/LC_MESSAGES
%lang(fr) %{perl_vendorlib}/LocaleData/fr/LC_MESSAGES/video.dvdrip.mo
%lang(it) %dir %{perl_vendorlib}/LocaleData/it/LC_MESSAGES
%lang(it) %{perl_vendorlib}/LocaleData/it/LC_MESSAGES/video.dvdrip.mo
%lang(sr) %dir %{perl_vendorlib}/LocaleData/sr/LC_MESSAGES
%lang(sr) %{perl_vendorlib}/LocaleData/sr/LC_MESSAGES/video.dvdrip.mo

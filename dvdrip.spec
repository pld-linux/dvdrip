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
Summary(es):	M�dulo de Perl Video::DVDRip
Summary(fr):	Module Perl Video::DVDRip
Summary(it):	Modulo di Perl Video::DVDRip
Summary(ja):	Video::DVDRip Perl �⥸�塼��
Summary(ko):	Video::DVDRip �� ����
Summary(no):	Perlmodul Video::DVDRip
Summary(pl):	Modu� Perla Video::DVDRip
Summary(pt):	M�dulo de Perl Video::DVDRip
Summary(pt_BR):	M�dulo Perl Video::DVDRip
Summary(ru):	������ ��� Perl Video::DVDRip
Summary(sv):	Video::DVDRip Perlmodul
Summary(uk):	������ ��� Perl Video::DVDRip
Summary(zh_CN):	Video::DVDRip Perl ģ��
Name:		perl-Video-DVDRip
Version:	0.50.3
Release:	1
License: 	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.exit1.org/dvdrip/dist/%{pnam}-%{version}.tar.gz
URL:		http://www.exit1.org/dvdrip/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-gtk
BuildRequires:	gdk-pixbuf-devel
Requires:	transcode
Provides:	perl(Video::DVDRip::GUI::Project::ClipZoomTab)
Provides:	perl(Video::DVDRip::GUI::Project::LoggingTab)
Provides:	perl(Video::DVDRip::GUI::Project::StorageTab)
Provides:	perl(Video::DVDRip::GUI::Project::TitleTab)
Provides:	perl(Video::DVDRip::GUI::Project::TranscodeTab)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvd::rip is a Perl Gtk+ based DVD copy program build on top of a low
level DVD Ripping API, which uses the Linux Video Stream Processing
Tool transcode, written by Thomas �streich.

%description -l pl
dvd::rip jest opartym na Gtk+ programem w perlu do kopiowania DVD,
zbudowanym w oparciu o niskopoziomowe API DVD Ripping, kt�re z kolei
korzysta z transcode - linuksowego narz�dzia do obr�bki strumieni
obrazu, napisanego przez Thomasa �streicha.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
%{perl_sitelib}/Video
%{_mandir}/man1/*
%{_mandir}/man3/*

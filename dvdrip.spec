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
Version:	0.44
Release:	0.2
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
Tool transcode, written by Thomas Östreich.

%description -l pl
dvd::rip jest opartym na Gtk+ programem w perlu do kopiowania DVD,
zbudowanym w oparciu o niskopoziomowe API DVD Ripping, które z kolei
korzysta z transcode - linuksowego narzêdzia do obróbki strumieni
obrazu, napisanego przez Thomasa Östreicha.

%prep
%setup -q -n %{pnam}-%{version}

%build
#CFLAGS="%{rpmcflags}"
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3

eval `perl '-V:installarchlib'`
install -d $RPM_BUILD_ROOT/$installarchlib 
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install

#find $RPM_BUILD_ROOT%{_prefix} -type f -print |
#	sed "s@^$RPM_BUILD_ROOT@@g" |
#	grep -v perllocal.pod |
#	grep -v "\.packlist" > Video-DVDRip-%{version}-filelist
#if [ "$(cat Video-DVDRip-%{version}-filelist)X" = "X" ] ; then
#    echo "ERROR: EMPTY FILE LIST"
#    exit -1
#fi

cd $RPM_BUILD_ROOT%{perl_sitelib}/Video
pod2man --section=3pm DVDRip.pm >$RPM_BUILD_ROOT%{_mandir}/man3/Video::DVDRip.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Credits README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Video
%{_mandir}/man3/*

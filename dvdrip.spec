# Conditional build:
%bcond_with	tests	# perform "make test" (needs working, not busy /dev/audio!)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Video::DVDRip Perl module
Summary(cs.UTF-8):	Modul Video::DVDRip pro Perl
Summary(da.UTF-8):	Perlmodul Video::DVDRip
Summary(de.UTF-8):	Video::DVDRip Perl Modul
Summary(es.UTF-8):	Módulo de Perl Video::DVDRip
Summary(fr.UTF-8):	Module Perl Video::DVDRip
Summary(it.UTF-8):	Modulo di Perl Video::DVDRip
Summary(ja.UTF-8):	Video::DVDRip Perl モジュール
Summary(ko.UTF-8):	Video::DVDRip 펄 모줄
Summary(nb.UTF-8):	Perlmodul Video::DVDRip
Summary(pl.UTF-8):	Moduł Perla Video::DVDRip
Summary(pt.UTF-8):	Módulo de Perl Video::DVDRip
Summary(pt_BR.UTF-8):	Módulo Perl Video::DVDRip
Summary(ru.UTF-8):	Модуль для Perl Video::DVDRip
Summary(sv.UTF-8):	Video::DVDRip Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Video::DVDRip
Summary(zh_CN.UTF-8):	Video::DVDRip Perl 模块
Name:		dvdrip
Version:	0.98.8
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.exit1.org/dvdrip/dist/%{name}-%{version}.tar.gz
# Source0-md5:	61b77b298b14c6bde83713e93e9ea4d8
Patch0:		%{name}-locale_path.patch
URL:		http://www.exit1.org/dvdrip/
BuildRequires:	perl-AnyEvent
BuildRequires:	perl-Event
BuildRequires:	perl-Event-RPC
BuildRequires:	perl-Gtk2-Ex-FormFactory
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libintl >= 1.16
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	ImageMagick
Requires:	perl-libintl >= 1.16
Requires:	transcode
Suggests:	ffmpeg
Suggests:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvd::rip is a Perl GTK+ based DVD copy program build on top of a low
level DVD Ripping API, which uses the Linux Video Stream Processing
Tool transcode, written by Thomas Oestreich.

%description -l en.UTF-8
dvd::rip is a Perl GTK+ based DVD copy program build on top of a low
level DVD Ripping API, which uses the Linux Video Stream Processing
Tool transcode, written by Thomas Östreich.

%description -l pl.UTF-8
dvd::rip jest opartym na GTK+ programem w Perlu do kopiowania DVD,
zbudowanym w oparciu o niskopoziomowe API DVD Ripping, które z kolei
korzysta z transcode - linuksowego narzędzia do obróbki strumieni
obrazu, napisanego przez Thomasa Östreicha.

%prep
%setup -q
%patch0 -p1

%build
export SKIP_UNPACK_REQUIRED_MODULES=1
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
mv $RPM_BUILD_ROOT%{perl_vendorlib}/LocaleData $RPM_BUILD_ROOT%{_datadir}/locale

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Credits README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Video
%{_mandir}/man1/*
%{_mandir}/man3/Video*
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/video.dvdrip.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/video.dvdrip.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/video.dvdrip.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/video.dvdrip.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/video.dvdrip.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/video.dvdrip.mo

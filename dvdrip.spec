%include        /usr/lib/rpm/macros.perl
Summary:	Video-DVDRip module for perl
Name:		perl-Video-DVDRip
Version:	0.44
Release:	0.1
Copyright:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.exit1.org/dvdrip/dist/Video-DVDRip-%{version}.tar.gz
URL:		http://www.exit1.org/dvdrip/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-gtk
BuildRequires:	gdk-pixbuf-devel
Requires:	transcode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvd::rip is a Perl Gtk+ based DVD copy program build on top of a low
level DVD Ripping API, which uses the Linux Video Stream Processing
Tool transcode, written by Thomas Östreich.

%prep
%setup -q -n Video-DVDRip-%{version}

%build
CFLAGS="%{rpmcflags}" perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

eval `perl '-V:installarchlib'`
install -d $RPM_BUILD_ROOT/$installarchlib
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install

find $RPM_BUILD_ROOT%{_prefix} -type f -print |
	sed "s@^$RPM_BUILD_ROOT@@g" |
	grep -v perllocal.pod |
	grep -v "\.packlist" > Video-DVDRip-%{version}-filelist
if [ "$(cat Video-DVDRip-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi

%files -f Video-DVDRip-%{version}-filelist
%defattr(644,root,root,755)

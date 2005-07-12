Summary:	Ruby - interpreted scripting language
Summary(ja):	¥ª¥Ö¥¸¥§¥¯¥È»Ø¸þ¸À¸ìRuby¥¤¥ó¥¿¥×¥ê¥¿
Summary(pl):	Ruby - interpretowany jêzyk skryptowy
Summary(pt_BR):	Linguagem de script orientada a objeto
Summary(zh_CN):	ruby - Ò»ÖÖ¿ìËÙ¸ßÐ§µÄÃæÏò¶ÔÏó½Å±¾±à³ÌÓïÑÔ
Name:		sydney
Version:	1.8.2
Release:	4
Epoch:		1
License:	The Ruby License
Group:		Development/Languages
Source0:	sydney-20050712.tar.gz
# Source0-md5:	13a0313067fd864123c73927049b78f6
Source1:	http://www.ibiblio.org/pub/languages/ruby/doc/ruby-texi-1.4-en.tar.gz
# Source1-md5:	839fda4af52b5c5c6d21f879f7fc62bf
Source2:	http://www.math.sci.hokudai.ac.jp/~gotoken/ruby/ruby-uguide-981227.tar.gz
# Source2-md5:	24eadcd067278901da9ad70efb146b07
Source3:	http://www.ibiblio.org/pub/languages/ruby/doc/rubyfaq-990927.tar.gz
# Source3-md5:	634c25b14e19925d10af3720d72e8741
Source4:	irb.1
%define stdlibdoc_version	0.9.13
Source6:	http://www.ruby-doc.org/downloads/stdlib/ruby-doc-stdlib-%{stdlibdoc_version}.tgz
# Source6-md5:	39dab8db652dad23ad8951f851549f06
Source8:	macros.ruby
Patch0:		ruby-info.patch
Patch1:		ruby-LIB_PREFIX.patch
Patch2:		ruby-ia64.patch
Patch3:		ruby-mkmf-shared.patch
URL:		http://www.ruby-lang.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	texinfo
BuildRequires:	unzip
Requires(post,postun): /sbin/ldconfig
Obsoletes:	ruby-doc
Obsoletes:	rdoc
Obsoletes:	ruby-REXML
Provides:	ruby = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/ruby-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

# bleh, some nasty (gcc or ruby) bug still not fixed
# (SEGV or "unexpected break" on miniruby run during build)
%define		specflags_ia64	-O0

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in Perl). It is simple,
straight-forward, extensible, and portable.

%description -l ja
Ruby¤Ï¥·¥ó¥×¥ë¤«¤Ä¶¯ÎÏ¤Ê¥ª¥Ö¥¸¥§¥¯¥È»Ø¸þ¥¹¥¯¥ê¥×¥È¸À¸ì¤Ç¤¹¡¥Ruby¤ÏºÇ½é
¤«¤é½ã¿è¤Ê¥ª¥Ö¥¸¥§¥¯¥È»Ø¸þ¸À¸ì¤È¤·¤ÆÀß·×¤µ¤ì¤Æ¤¤¤Þ¤¹¤«¤é¡¤¥ª¥Ö¥¸¥§¥¯¥È
»Ø¸þ¥×¥í¥°¥é¥ß¥ó¥°¤ò¼ê·Ú¤Ë¹Ô¤¦»ö¤¬½ÐÍè¤Þ¤¹¡¥¤â¤Á¤í¤óÄÌ¾ï¤Î¼êÂ³¤­·¿¤Î¥×
¥í¥°¥é¥ß¥ó¥°¤â²ÄÇ½¤Ç¤¹¡¥

Ruby¤Ï¥Æ¥­¥¹¥È½èÍý´Ø·¸¤ÎÇ½ÎÏ¤Ê¤É¤ËÍ¥¤ì¡¤Perl¤ÈÆ±¤¸¤¯¤é¤¤¶¯ÎÏ¤Ç¤¹¡¥¤µ¤é
¤Ë¥·¥ó¥×¥ë¤ÊÊ¸Ë¡¤È¡¤Îã³°½èÍý¤ä¥¤¥Æ¥ì¡¼¥¿¤Ê¤É¤Îµ¡¹½¤Ë¤è¤Ã¤Æ¡¤¤è¤êÊ¬¤«¤ê
¤ä¤¹¤¤¥×¥í¥°¥é¥ß¥ó¥°¤¬½ÐÍè¤Þ¤¹¡¥

%description -l pl
Ruby to interpretowany jêzyk skryptowy, w sam raz dla ³atwego i
szybkiego pisania zorientowanych obiektowo programów. Ma wiele funkcji
u³atwiaj±cych przetwarzanie plików tekstowych i wykonywanie prac
zwi±zanych z zarz±dzaniem systemu (podobnie jak Perl). Jest prosty,
rozszerzalny i przeno¶ny.

%description -l pt_BR
Ruby é uma linguagem de script interpretada de programação
orientada a objeto. Possui diversas características para
processamento de texto. É simples, extensível e direta.

%package devel
Summary:	Ruby development libraries
Summary(pl):	Biblioteki programistyczne interpretera jêzyka Ruby
Group:		Development/Languages
Requires:	ruby = %{epoch}:%{version}-%{release}

%description devel
Ruby development libraries.

%description devel -l pl
Biblioteki programistyczne interpretera jêzyka Ruby.

%package static
Summary:	Ruby static libraries
Summary(pl):	Biblioteki statyczne Ruby
Group:		Development/Languages
Requires:	ruby = %{epoch}:%{version}-%{release}

%description static
Ruby static libraries.

%description devel -l pl
Biblioteki statyczne Ruby.

%prep
%setup -q -n sydney -a1 -a2 -a3 -a6
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

find . -name '*.rb' -or -name '*.cgi' -or -name '*.test' | xargs perl -pi -e "s#/usr/local/bin#bin#"

%build
cp -f /usr/share/automake/config.sub .

rm -r ext/tcltklib

%{__autoconf}
%configure \
	--enable-shared \
	--enable-pthread
%{__make}

%{__make} info -C ruby-texi-1.4-en

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_mandir}/man1,%{_examplesdir}/ruby-%{version},%{_libdir}/rpm,%{_datadir}/ruby}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/ruby-%{version}
install ruby-texi-1.4-en/ruby.info* $RPM_BUILD_ROOT%{_infodir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/man1

mv -f ruby-uguide guide
mv -f rubyfaq faq

install %{SOURCE8} $RPM_BUILD_ROOT%{_libdir}/rpm

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc guide faq misc README README.EXT ChangeLog ToDo
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/ruby
%dir %{_libdir}/ruby
%dir %{_libdir}/ruby/1.8
%{_libdir}/ruby/1.8/bigdecimal
%{_libdir}/ruby/1.8/cgi
%{_libdir}/ruby/1.8/date
%{_libdir}/ruby/1.8/dl
%{_libdir}/ruby/1.8/drb
%{_libdir}/ruby/1.8/io
%{_libdir}/ruby/1.8/irb
%{_libdir}/ruby/1.8/net
%{_libdir}/ruby/1.8/openssl
%{_libdir}/ruby/1.8/optparse
%{_libdir}/ruby/1.8/racc
%{_libdir}/ruby/1.8/rdoc
%{_libdir}/ruby/1.8/rexml
%{_libdir}/ruby/1.8/rinda
%{_libdir}/ruby/1.8/rss
%{_libdir}/ruby/1.8/runit
%{_libdir}/ruby/1.8/shell
%{_libdir}/ruby/1.8/soap
%{_libdir}/ruby/1.8/test
%{_libdir}/ruby/1.8/uri
%{_libdir}/ruby/1.8/webrick
%{_libdir}/ruby/1.8/wsdl
%{_libdir}/ruby/1.8/xmlrpc
%{_libdir}/ruby/1.8/xsd
%{_libdir}/ruby/1.8/yaml
%{_libdir}/ruby/1.8/[A-Za-s]*.rb
%{_libdir}/ruby/1.8/tempfile.rb
%{_libdir}/ruby/1.8/thread.rb
%{_libdir}/ruby/1.8/thwait.rb
%{_libdir}/ruby/1.8/time.rb
%{_libdir}/ruby/1.8/timeout.rb
%{_libdir}/ruby/1.8/tmpdir.rb
%{_libdir}/ruby/1.8/tracer.rb
%{_libdir}/ruby/1.8/tsort.rb
%{_libdir}/ruby/1.8/[u-z]*.rb
%dir %{_libdir}/ruby/1.8/*-linux*
%dir %{_libdir}/ruby/1.8/*-linux*/digest
%dir %{_libdir}/ruby/1.8/*-linux*/io
%dir %{_libdir}/ruby/1.8/*-linux*/racc
%attr(755,root,root) %{_libdir}/ruby/1.8/*-linux*/[a-s]*.so
%attr(755,root,root) %{_libdir}/ruby/1.8/*-linux*/[u-z]*.so
%attr(755,root,root) %{_libdir}/ruby/1.8/*-linux*/digest/*.so
%attr(755,root,root) %{_libdir}/ruby/1.8/*-linux*/io/*.so
%attr(755,root,root) %{_libdir}/ruby/1.8/*-linux*/racc/*.so
%{_libdir}/ruby/1.8/*-linux*/rbconfig.rb
%dir %{_ulibdir}/ruby/site_ruby
%dir %{_ulibdir}/ruby/site_ruby/1.8
%dir %{_ulibdir}/ruby/site_ruby/1.8/*-linux*
%{_mandir}/*/*
%{_infodir}/*.info*
%{_examplesdir}/ruby-%{version}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/ruby/1.8/*/*.h
%{_libdir}/rpm/macros.ruby

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

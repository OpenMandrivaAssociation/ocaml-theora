Name:           ocaml-theora
Version:        0.2.0
Release:        3
Summary:        OCaml interface to the theora library
License:        GPL
Group:          Development/Other
URL:            https://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/project/savonet/ocaml-theora/%{version}/ocaml-theora-%{version}.tar.gz
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml
BuildRequires:  libtheora-devel
BuildRequires:  ocaml-ogg-devel
Requires:       ocaml-ogg

%description
This package contains an OCaml interface for 
Theora Video Compression Codec Library, 
otherwise known as libtheora.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure
make all
make doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/theora
make install

%files
%defattr(-,root,root)
%doc COPYING CHANGES README
%dir %{_libdir}/ocaml/theora
%{_libdir}/ocaml/theora/META
%{_libdir}/ocaml/theora/*.cma
%{_libdir}/ocaml/theora/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc/html
%{_libdir}/ocaml/theora/*.a
%{_libdir}/ocaml/theora/*.cmxa
%{_libdir}/ocaml/theora/*.cmx
%{_libdir}/ocaml/theora/*.mli



%changelog
* Mon Aug 23 2010 Florent Monnier <blue_prawn@mandriva.org> 0.2.0-1mdv2011.0
+ Revision: 572421
- updated to last version 0.2.0

* Tue Jan 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-1mdv2010.1
+ Revision: 496517
- update to new version 0.1.2

* Thu Aug 13 2009 Florent Monnier <blue_prawn@mandriva.org> 0.1.1-2mdv2010.0
+ Revision: 416091
- increm mkrel
- corrected summary

* Thu Aug 13 2009 Florent Monnier <blue_prawn@mandriva.org> 0.1.1-1mdv2010.0
+ Revision: 416088
- import ocaml-theora


Name:           ocaml-theora
Version:        0.1.1
Release:        %mkrel 1
Summary:        OCaml interface to the theora library
License:        GPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/project/savonet/ocaml-theora/%{version}/ocaml-theora-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
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
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/theora
make install

%clean
rm -rf %{buildroot}

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


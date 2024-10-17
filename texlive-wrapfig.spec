Name:		texlive-wrapfig
Version:	61719
Release:	2
Summary:	Produces figures which text can flow around
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wrapfig
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Allows figures or tables to have text wrapped around them. Does
not work in combination with list environments, but can be used
in a parbox or minipage, and in twocolumn format. Supports the
float package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/wrapfig/wrapfig.sty
%doc %{_texmfdistdir}/doc/latex/wrapfig/multiple-span.txt
%doc %{_texmfdistdir}/doc/latex/wrapfig/wrapfig-doc.pdf
%doc %{_texmfdistdir}/doc/latex/wrapfig/wrapfig-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

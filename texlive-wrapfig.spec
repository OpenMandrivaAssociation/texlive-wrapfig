# revision 22048
# category Package
# catalog-ctan /macros/latex/contrib/wrapfig
# catalog-date 2011-04-09 12:56:30 +0200
# catalog-license lppl
# catalog-version 3.6
Name:		texlive-wrapfig
Version:	3.6
Release:	1
Summary:	Produces figures which text can flow around
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wrapfig
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Allows figures or tables to have text wrapped around them. Does
not work in combination with list environments, but can be used
in a parbox or minipage, and in twocolumn format. Supports the
float package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/wrapfig/wrapfig.sty
%doc %{_texmfdistdir}/doc/latex/wrapfig/multiple-span.txt
%doc %{_texmfdistdir}/doc/latex/wrapfig/wrapfig-doc.pdf
%doc %{_texmfdistdir}/doc/latex/wrapfig/wrapfig-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

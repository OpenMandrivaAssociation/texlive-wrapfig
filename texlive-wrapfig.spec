%global tl_name wrapfig
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.6
Release:	%{tl_revision}.1
Summary:	Produces figures which text can flow around
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wrapfig
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapfig.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Allows figures or tables to have text wrapped around them. Does not work
in combination with list environments, but can be used in a parbox or
minipage, and in twocolumn format. Supports the float package.


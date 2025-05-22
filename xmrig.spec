Name:		xmrig
Version:	6.22.2
Release:	1
Source0:	https://github.com/xmrig/xmrig/archive/refs/tags/v%{version}.tar.gz
Summary:	Crypto currency miner supporting Monero
URL:		https://github.com/xmrig/xmrig
License:	GPL-3.0
Group:		Servers
BuildRequires:	cmake
BuildRequires:	pkgconfig(hwloc)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libuv)
BuildSystem:	cmake

%patchlist
xmrig-6.22.2-allow-donate-level-0.patch

%description
XMRig is a high performance, open source, cross platform RandomX, KawPow,
CryptoNight and GhostRider unified CPU/GPU miner and RandomX benchmark.

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 _OMV_rpm_build/xmrig %{buildroot}%{_bindir}/

%files
%{_bindir}/xmrig

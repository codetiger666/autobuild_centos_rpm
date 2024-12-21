Name:           openssh-server
Version:        codetiger_version
Release:        1%{?dist}
Summary:        openssh-server编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz
Source1:        onedrive.service
Source2:        config
Source3:        onedrive

BuildRequires:  openssl-devel == openssl_version
BuildRequires:  zlib-devel cmake gcc libselinux-devel
Requires: openssl == openssl_version
Requires: zlib libselinux

# 描述
%description
openssh-server编译

%prep
%setup -q

# 编译
%build
CFLAGS="-fPIC" ./configure --prefix=/usr --sysconfdir=/etc/ssh --with-selinux
make -j6

# 安装
%install
make install DESTDIR=%{buildroot}
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/sshd.service


# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/sshd.service ]; then
    %systemd_preun sshd.service
    fi
fi

# 文件列表
%files
%defattr(-,root,root,0755)
%dir /etc
%dir /usr
%dir /var
%config(noreplace) %{_etc}/ssh/ssh_config
%config(noreplace) %{_etc}/ssh/sshd_config
# 文档
%doc

# 更改日志
%changelog

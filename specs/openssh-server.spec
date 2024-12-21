Name:           openssh
Version:        codetiger_version
Release:        1%{?dist}
Summary:        openssh-server编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz
Source1:        sshd.service

BuildRequires:  openssl-devel == openssl_version
BuildRequires:  zlib-devel gcc libselinux-devel
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
/etc/ssh/moduli
%{_usr}/bin/scp
%{_usr}/bin/sftp
%{_usr}/bin/ssh
%{_usr}/bin/ssh-add
%{_usr}/bin/ssh-agent
%{_usr}/bin/ssh-keygen
%{_usr}/bin/ssh-keyscan
%{_usr}/lib/systemd/system/sshd.service
%{_usr}/libexec/sftp-server
%{_usr}/libexec/ssh-keysign
%{_usr}/libexec/ssh-pkcs11-helper
%{_usr}/libexec/ssh-sk-helper
%{_usr}/libexec/sshd-session
%{_usr}/sbin/sshd
%{_usr}/share/man/man1/scp.1.gz
%{_usr}/share/man/man1/sftp.1.gz
%{_usr}/share/man/man1/ssh-add.1.gz
%{_usr}/share/man/man1/ssh-agent.1.gz
%{_usr}/share/man/man1/ssh-keygen.1.gz
%{_usr}/share/man/man1/ssh-keyscan.1.gz
%{_usr}/share/man/man1/ssh.1.gz
%{_usr}/share/man/man5/moduli.5.gz
%{_usr}/share/man/man5/ssh_config.5.gz
%{_usr}/share/man/man5/sshd_config.5.gz
%{_usr}/share/man/man8/sftp-server.8.gz
%{_usr}/share/man/man8/ssh-keysign.8.gz
%{_usr}/share/man/man8/ssh-pkcs11-helper.8.gz
%{_usr}/share/man/man8/ssh-sk-helper.8.gz
%{_usr}/share/man/man8/sshd.8.gz
%config(noreplace) /etc/ssh/ssh_config
%config(noreplace) /etc/ssh/sshd_config
# 文档
%doc

# 更改日志
%changelog

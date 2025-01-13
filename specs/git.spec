Name:           git
Version:        codetiger_version
Release:        1%{?dist}
Summary:        openresty编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://www.kernel.org/pub/software/scm/git/git-%{version}.tar.gz

BuildRequires:  
Requires:       

# 描述
%description
git自编译

# 编译前准备
%prep
%setup -q

# 编译
%build
CFLAGS="-fPIC" ./configure --prefix=/usr/local
make all -j6

# 安装
%install
make install DESTDIR=%{buildroot}

# 文件列表
%files
%defattr(-,root,root,0755)
# 文档
%doc

# 更改日志
%changelog
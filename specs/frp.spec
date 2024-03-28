Name:           frp
Version:        codetiger_version
Release:        1%{?dist}
Summary:        frp编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/fatedier/frp/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz
Source1:        frpc.service
Source2:        frps.service
    

%description


%prep
rm -rf %{_builddir}/*
cp %{SOURCE0} %{_builddir}
tar xf %{SOURCE0}
mv frp_%{version}_linux_amd64 %{name}-%{version}


%install
%{__mkdir} -p %{buildroot}/usr/local/frp
cp %{name}-%{version}/frpc* %{buildroot}/usr/local/frp
cp %{name}-%{version}/frps* %{buildroot}/usr/local/frp
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_usr}/lib/systemd/system/frpc.service
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_usr}/lib/systemd/system/frps.service

%files
%{_usr}/local/frp/frpc
%{_usr}/local/frp/frps
%{_usr}/local/frp/frpc.toml
%{_usr}/local/frp/frps.toml
%{_usr}/lib/systemd/system/frpc.service
%{_usr}/lib/systemd/system/frps.service
%config
%{_usr}/local/frp/frpc.toml
%{_usr}/local/frp/frps.toml
%doc

%changelog
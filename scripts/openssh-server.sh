OPENSSL_VERSION=1:3.2.2

program_init(){
  docker exec -i $centos dnf install -y zlib-devel libselinux-devel openssl-devel-$OPENSSL_VERSION
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/openssh-server.spec
  sudo sed -i "s/openssl_version/$OPENSSL_VERSION/g" specs/openssh-server.spec
  sudo /bin/cp specs/openssh-server.spec rpm/rpmbuild/SPECS/openssh-server.spec
  wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-${project_version}.tar.gz
  tar -zxvf openssh-${project_version}.tar.gz
  mv openssh-${project_version} openssh-server-${project_version}
  tar -zcvf openssh-server-${project_version}.tar.gz openssh-server-${project_version}
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp openssh-server-${project_version}.tar.gz rpm/rpmbuild/SOURCES/openssh-server-${project_version}.tar.gz
}
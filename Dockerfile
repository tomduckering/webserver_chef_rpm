FROM centos:7
RUN yum -y install epel-release
RUN yum -y install rpm-build rpmdevtools redhat-rpm-config yum-utils rpmlint
RUN curl -OL https://packages.chef.io/files/stable/chefdk/1.4.3/el/7/chefdk-1.4.3-1.el7.x86_64.rpm
RUN yum -y localinstall chefdk-1.4.3-1.el7.x86_64.rpm
RUN rpmdev-setuptree
ADD ./build_rpm.sh /build_rpm.sh
RUN chmod u+x ./build_rpm.sh
VOLUME /spec_src
ENTRYPOINT ["/build_rpm.sh"]


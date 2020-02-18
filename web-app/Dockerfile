FROM centos:8.1.1911
# hadolint ignore=DL4000
MAINTAINER nickgitshub

stupid error

RUN yum -y install httpd
RUN yum -y install git

#Pull website code from github and copy into the html folder

RUN git clone https://github.com/nickgitshub/TestJenkins 
WORKDIR /home/ubuntu/TestJenkins
COPY index.html /var/www/html

# hadolint ignore=DL3025
CMD /usr/sbin/httpd -D FOREGROUND
EXPOSE 80
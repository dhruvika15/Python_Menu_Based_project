FROM centos
RUN yum install evince -y
COPY resume.pdf /resume.pdf
CMD evince resume.pdf


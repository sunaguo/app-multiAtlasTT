FROM brainlife/freesurfer-mini:7.1.1
MAINTAINER Joshua Faskowitz <jfaskowi@iu.edu>

#python used by maTT_remap.py 
RUN yum install -y python3-pip wget

RUN pip3 install nibabel six

RUN wget -q -O - https://ndownloader.figshare.com/files/25079594 | tar -xz

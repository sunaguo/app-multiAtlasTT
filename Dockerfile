FROM brainlife/freesurfer:6.0.0
MAINTAINER Joshua Faskowitz <jfaskowi@iu.edu>

#python used by maTT_remap.py 
RUN apt-get update && apt-get install -y python3 python3-pip wget
RUN pip3 install nibabel six

RUN wget -q -O - https://ndownloader.figshare.com/files/14037086 | tar -xz



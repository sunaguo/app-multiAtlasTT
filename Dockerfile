FROM brainlife/freesurfer
MAINTAINER Joshua Faskowitz <jfaskowi@iu.edu>

RUN apt-get update && apt-get install -y python python-p wget
RUN pip install nibabel

RUN wget -q -O - https://ndownloader.figshare.com/files/11768399 | tar -xz



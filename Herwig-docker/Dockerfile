FROM ubuntu:latest
RUN mkdir /herwig
WORKDIR /herwig
RUN apt-get update && \
    apt-get install --yes curl g++ gcc gfortran \
                          python python-dev make \
                          binutils zlib1g-dev rsync \
                          patch git autoconf && \
    apt-get clean
RUN curl -O -L https://herwig.hepforge.org/herwig-bootstrap
RUN chmod +x herwig-bootstrap
RUN  ./herwig-bootstrap /usr/local 
COPY docker-entrypoint.sh /herwig/docker-entrypoint.sh
RUN chmod +x /herwig/docker-entrypoint.sh
ENTRYPOINT ["/herwig/docker-entrypoint.sh"]
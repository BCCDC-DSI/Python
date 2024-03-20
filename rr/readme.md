# Research Reproducibility (RR)

Goodman et al. (2016):
- Methods
- Results
- Inferential

[More details](theory.md)

## Version control
- [Git](../git)

## Reproducible environments

- [Blog from Nov 2023](https://occasionaldivergences.com/posts/rep-env/)
- Python:
  ```
  pip freeze requirements.txt
  ```
  
  <details>
  <summary>Dockerfile</summary>
  ```
    
  FROM alpine:3.15
  
  RUN apk add curl linux-headers bash gcc musl-dev g++ pkgconf make file
  
  # zlib --------------------------------------------------------------------
  
  RUN curl -OL https://downloads.sourceforge.net/project/libpng/zlib/1.2.11/zlib-1.2.11.tar.gz
  RUN tar xzf zlib-*.tar.gz && rm zlib-*.tar.gz
  RUN cd zlib-* &&                                    \
      CFLAGS=-fPIC ./configure --static &&            \
      make &&                                         \
      make install
  
  # openssl -----------------------------------------------------------------
  
  RUN curl -O https://www.openssl.org/source/openssl-1.1.1w.tar.gz
  RUN tar xzf openssl-*.tar.gz && rm openssl-*.tar.gz
  RUN apk add perl linux-headers
  RUN cd openssl-* &&                                 \
      CFLAGS=-fPIC ./config -fPIC no-shared &&        \
      make &&                                         \
      make install_sw &&                              \
      rm -rf /usr/local/bin/openssl                   \
         /usr/local/share/{man/doc}
  
  # install rust toolchain for 'rigbuild' user ==============================
  
  RUN adduser rigbuild -D
  USER rigbuild
  RUN cd && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o rust.sh && sh rust.sh -y
  USER root
  ENV PATH="/home/rigbuild/.cargo/bin:$PATH"
  COPY entrypoint.sh /entrypoint.sh
  RUN chmod +x /entrypoint.sh
  ENTRYPOINT [ "sh", "/entrypoint.sh" ]
  
  # this is the shared directory =============================================
  
  RUN mkdir /work
  WORKDIR /work
  
  # packageer ===============================================================
  
  RUN curl -LO https://github.com/goreleaser/nfpm/releases/download/v2.32.0/nfpm_2.32.0_$(arch).apk && \
    apk add --allow-untrusted nfpm*.apk && \
    rm nfpm*.apk
  ```
  </details>

  
## Platforms
- Kaggle
- Digital Ocean
- Google Colab
- Jupyter.org
- ...


## Recommended practices
- [markdown](https://www.markdownguide.org/basic-syntax/)

## Example workflows
<details>
<summary>R</summary>

  ```
  # Makefile (target: required_files)
  
  manuscript.pdf: manuscript.Rmd simulated_data.csv 
  
  Rscript -e 'rmarkdown::render("manuscript.Rmd")' 
  
  simulated_data.csv: simulate.R
  
  Rscript -e 'source("simulate.R")' 
  ```
Source: [MDPI 2020](https://mdpi-res.com/psych/psych-03-00053/article_deploy/psych-03-00053.pdf)

</details>


## References
- Davos: A Python package ‘‘smuggler’’ for constructing lightweight reproducible notebooks, Paxton C. Fitzpatrick, Jeremy R. Manning [2024 article](https://doi.org/10.1016/j.softx.2023.101614)

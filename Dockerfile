FROM continuumio/anaconda3:2020.11
LABEL mantainer="QMENTA Inc."
WORKDIR '/root'

# Add tool script
COPY tool.py /root/tool.py

# Install and upgrade all the required libraries and tools (in this case only python libraries are needed)
RUN python -m pip install --upgrade pip
RUN python -m pip install qmenta-sdk-lib
RUN conda install -c mrtrix3 mrtrix3

# Configure entrypoint
RUN python -m qmenta.sdk.make_entrypoint /root/entrypoint.sh /root/
RUN chmod +x /root/entrypoint.sh
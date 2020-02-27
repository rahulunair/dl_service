FROM pytorch/pytorch

WORKDIR /efficient_net/
COPY . /efficient_net/
RUN /opt/conda/bin/pip install -r requirements.txt
RUN echo -e "\e[31mThis server should only be used for debugging purposes."
ENTRYPOINT ["python"]
CMD ["rest.py"]

FROM pytorch/pytorch

WORKDIR /efficient_net/
COPY . /efficient_net/
RUN /opt/conda/bin/pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["rest.py"]

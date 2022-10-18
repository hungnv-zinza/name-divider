FROM public.ecr.aws/lambda/python:3.9

RUN  pip3 install namedivider-python --target "${LAMBDA_TASK_ROOT}"
RUN  pip3 install requests --target "${LAMBDA_TASK_ROOT}"
RUN  pip3 install lightgbm --target "${LAMBDA_TASK_ROOT}"
RUN  yum install libgomp -y
RUN  sed -i 's/~\/.cache/\/var\/task/g' /var/task/namedivider/util.py

COPY app.py ${LAMBDA_TASK_ROOT}
COPY ./namedivider-python/* /var/task/namedivider-python/

CMD [ "app.handler" ] 
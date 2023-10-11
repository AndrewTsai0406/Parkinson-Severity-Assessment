FROM public.ecr.aws/lambda/python:3.10

RUN pip install joblib
RUN pip install scikit-learn

COPY ["models/.", "./models/"]
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]
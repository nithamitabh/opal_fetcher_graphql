FROM permitio/opal-client:latest
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --user -r /tmp/requirements.txt
COPY ./src/opal_fetcher_graphql /app/opal_fetcher_graphql
COPY ./.env /app/.env

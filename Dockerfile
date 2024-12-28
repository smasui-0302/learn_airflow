FROM apache/airflow:2.3.2

USER root

# システムパッケージのインストール
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtをコピー
COPY requirements.txt /

# airflowユーザーに切り替えてPythonパッケージをインストール
USER airflow
RUN pip install --no-cache-dir -r /requirements.txt
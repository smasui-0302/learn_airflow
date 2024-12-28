# learn_airflow

## 起動方法

- 以下コマンドを順次実行

```bash
    make build
    make init (※初回のみ)
    make up
```
- 2回目以降であれば以下コマンドでbuildとupをまとめて実行できる

```bash
    make run
```

## 停止

```bash
    make down
```

## フォルダ構成


```
{repo}
  ├─ README.md
  ├─ Makefile
  ├─ compose.yml
  ├─ Dockerfile
  ├─ requirements.txt
  ├─ dags
  ├─ logs
  ├─ plugins
```
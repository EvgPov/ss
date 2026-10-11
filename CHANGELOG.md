# Changelog

Все заметные изменения проекта документируются в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/),
проект следует [семантическому версионированию](https://semver.org/lang/ru/).

## [Unreleased]

## [1.0.0] - 2026-10-11

### Added
- Эндпоинт `/` — возвращает приветствие из настройки `GREETING`.
- Эндпоинт `/health` — проверка, что сервис жив: отвечает `{"status": "ok"}`.
- Эндпоинт `/db-check` — проверка подключения к базе данных PostgreSQL.
- Конфигурация через переменные окружения и файл `.env` (pydantic-settings);
  шаблон настроек — `.env.example`.
- Docker-образ на Python 3.12 с зависимостями из `uv.lock`.
- Запуск стека (приложение + PostgreSQL) через Docker Compose:
  healthcheck базы, данные хранятся в volume.
- CI на GitHub Actions: линтер Ruff и тесты pytest на каждый пуш.
- Публикация образа в GitHub Container Registry для `linux/amd64`
  и `linux/arm64`: тег `latest` из ветки `main` и тег версии
  при релизе по git-тегу `v*`.
# Веб-платформа tp-ga

Интерфейс диссертации и статьи: обзор исследования, карта планов, пошаговые объяснения декодера, классических методов и ГА, лаборатория расчётов и просмотр артефактов эксперимента. Бэкенд — FastAPI поверх библиотеки `tpga`, фронтенд — Next.js 16, React 19, Leaflet, lucide-react (JSX).

## Запуск в Windows

Нужны `.venv` в корне проекта и Node.js 24. Из корня проекта:

~~~powershell
python -m venv .venv
.venv\Scripts\pip install -e ".[dev]" -r platform\backend\requirements.txt
powershell -ExecutionPolicy Bypass -File scripts\dev.ps1
~~~

Скрипт собирает интерфейс, поднимает API на `127.0.0.1:8000` и интерфейс на `127.0.0.1:3000`, проверяет `/health` и печатает адреса. Оба сервера слушают только loopback. Если порт занят другой программой, скрипт сообщит об этом; задайте другой порт, например `-ApiPort 8010` или `-WebPort 3001`. Остановка: `scripts\dev.ps1 -Stop` — останавливаются только процессы, запущенные этим скриптом. Режим разработки: `-Dev`. Логи: `platform/data/logs/`.

Адрес API для интерфейса задаёт переменная `TPGA_API_ORIGIN` (её читает `next.config.mjs` при сборке и запуске). Разрешённые источники CORS задаёт `TPGA_CORS_ORIGINS`, по умолчанию `http://127.0.0.1:3000` и `http://localhost:3000`.

## Страницы

| Адрес | Содержание |
|---|---|
| `/` | Цель исследования, RQ1–RQ4, ключевые результаты из `paper_artifacts/` со ссылкой на таблицу-источник, статус эксперимента, версия кода и окружение. |
| `/map` | Планы LP, VAM и ГА на карте: экспорт пшеницы (векторные границы Natural Earth, необязательная подложка OSM, ж/д переходы), модельная сеть Астаны, синтетическая задача на плоскости. |
| `/decoder` | Пошаговая работа декодера на задачах 3×4 и 4×5. |
| `/classical` | Шаги NWC, LCM и VAM (со штрафами строк и столбцов), стоимости и отклонение от оптимума. |
| `/ga` | ГА по поколениям: турниры, OX1-кроссовер, мутация, элита, сходимость, лучший план. |
| `/lab` | Выбор задачи, методов и параметров; расчёт с прогрессом через SSE, отмена с подтверждением, история (SQLite), экспорт CSV/JSON. |
| `/experiment` | Таблицы T1–T6, тесты, кривые сходимости и рисунки F1–F6 из `paper_artifacts/`; скачивание архива. Только чтение. |
| `/methods` | METHODS.md, LIMITATIONS.md, NUMBERS.md, README артефактов, `environment.json`, команды воспроизведения. |

Интерфейс на русском с переключением на английский. Настройки (тема Aspan или Astana, масштаб текста, плотность строк, насыщенность плиток, язык) хранятся в localStorage; на телефоне всегда тема Aspan.

## API

| Метод | Назначение |
|---|---|
| `GET /health`, `GET /version` | Проверка доступности и версия библиотеки. |
| `POST /solve` | Синхронный расчёт произвольной матрицы до 400 направлений (прежний API, поведение сохранено). |
| `GET /scenarios`, `GET /scenarios/benchmark`, `POST /scenarios/{id}/plan` | Пакетные датасеты, как в 0.2 (параметр `dataset_id`). |
| `POST /jobs` → id; `GET /jobs/{id}`; `GET /jobs/{id}/events` (SSE); `DELETE /jobs/{id}` | Асинхронные расчёты в пуле процессов: задача (матрица, сценарий, генерация или задача статьи) до 200×200, методы, параметры ГА. События: `started`, `method_started`, `progress` (поколение, лучшая стоимость, отклонение, вызовы декодера), `method_done`, `done`, `cancelled`, `error`. Одновременно не более двух расчётов. |
| `POST /trace/decoder`, `POST /trace/classical`, `POST /trace/ga`, `GET /trace/examples` | Пошаговые трассировки для учебных страниц (до 100 направлений). |
| `POST /plans` | Планы нескольких методов для карты (бюджет ГА не более 200 000 вызовов). |
| `GET /artifacts`, `/artifacts/tables/{name}`, `/artifacts/figures/{lang}/{name}.{png,pdf}`, `/artifacts/docs/{name}`, `/artifacts/convergence`, `/artifacts/instances`, `/artifacts/download` | Только чтение `paper_artifacts/`. |
| `GET/POST /history`, `GET/DELETE /history/{id}` | История запусков в `platform/data/runs.db`; схема ведётся миграциями Alembic (`platform/backend/migrations`, `alembic upgrade head` / `alembic downgrade -1`). |

Контейнер API: `docker compose -f platform/docker-compose.yml up --build` (порт 8000).

## Проверки

~~~powershell
$env:PYTHONPATH = "platform/backend"; .venv\Scripts\python -m pytest -q platform/backend/tests
cd platform/web; npm run lint; npm run build; npm run test:e2e
~~~

Playwright по умолчанию обращается к уже запущенному интерфейсу (`E2E_BASE_URL`, по умолчанию `http://127.0.0.1:3000`); с `E2E_START=1` он сам поднимает API и интерфейс (так работает CI). Скриншоты в `docs/screenshots`: `SCREENSHOTS=1 npx playwright test e2e/screenshots.spec.js`.

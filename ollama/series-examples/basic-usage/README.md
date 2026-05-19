# Ollama Basic Usage

Ollama 2편 글에서 사용하는 기본 CLI와 API 호출 예제입니다.

> 이 폴더는 Ollama를 처음 실행하는 독자가 모델 다운로드, CLI 실행, curl API 호출을 빠르게 복습할 수 있도록 만든 학습용 샘플입니다.

---

## 📎 관련 아티클

- [Ollama 기본 사용법: 설치부터 모델 실행, API 호출까지](https://tistory-cloud.tistory.com/entry/Ollama-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-%EB%AA%A8%EB%8D%B8-%EC%8B%A4%ED%96%89-API-%ED%98%B8%EC%B6%9C%EA%B9%8C%EC%A7%80)

---

## ✅ 이 예제가 보여주는 것

- 자주 쓰는 Ollama CLI 명령어
- 로컬 모델을 내려받고 실행하는 기본 흐름
- `generate` API를 curl로 호출하는 방법
- `chat` API를 curl로 호출하는 방법
- `stream:false` 옵션으로 단일 JSON 응답을 받는 방법

---

## 📁 폴더 구조

```text
commands.md
api-examples/
  curl-generate.sh
  curl-chat.sh
```

---

## 🚀 빠른 시작

### 1. 이 폴더로 이동합니다

```bash
cd cloud-public/ollama/series-examples/basic-usage
```

### 2. Ollama가 실행 중인지 확인합니다

```bash
curl http://localhost:11434
```

### 3. 사용할 모델을 내려받습니다

```bash
ollama pull gemma3
```

### 4. CLI로 모델을 직접 실행합니다

```bash
ollama run gemma3
```

터미널에서 아래처럼 질문해 볼 수 있습니다.

```text
로컬 LLM이 무엇인지 한 문장으로 설명해줘.
```

### 5. curl 예제를 실행합니다

macOS/Linux/Git Bash 기준:

```bash
bash api-examples/curl-generate.sh
bash api-examples/curl-chat.sh
```

Windows PowerShell에서 실행한다면 `.sh` 파일 대신 파일 안의 curl 요청을 참고해 직접 실행하거나, Git Bash를 사용하는 편이 가장 간단합니다.

---

## 🧪 예제 파일 설명

| 파일 | 설명 |
|---|---|
| `commands.md` | `ollama run`, `ollama list`, `ollama show`, `ollama rm` 등 기본 명령어 모음 |
| `api-examples/curl-generate.sh` | `/api/generate`를 호출하는 가장 작은 예제 |
| `api-examples/curl-chat.sh` | `/api/chat`을 호출하는 가장 작은 예제 |

---

## ⚠️ 사용 전 확인

- Ollama가 설치되어 있어야 합니다.
- Ollama 로컬 서버가 실행 중이어야 합니다.
- 예제 모델은 `gemma3`를 기준으로 작성했습니다.
- 다른 모델을 사용할 경우 shell 파일 안의 `model` 값을 변경하세요.
- 모델을 처음 실행하면 다운로드 또는 로딩 때문에 시간이 걸릴 수 있습니다.

---

## 🧯 자주 막히는 지점

| 증상 | 확인할 것 |
|---|---|
| `model not found` | `ollama pull gemma3`를 먼저 실행했는지 확인 |
| `connection refused` | Ollama 앱 또는 서버가 실행 중인지 확인 |
| 응답이 여러 줄로 나옴 | API 요청에 `"stream": false`가 있는지 확인 |
| shell 파일 실행이 안 됨 | Git Bash 또는 macOS/Linux 터미널에서 실행 |

---

## 다음 단계

CLI와 curl 호출이 익숙해졌다면 다음 폴더로 이동하세요.

```bash
cd ../app-integration-guide
```

다음 예제에서는 Python, JavaScript, Modelfile로 Ollama를 애플리케이션 코드에 연결합니다.

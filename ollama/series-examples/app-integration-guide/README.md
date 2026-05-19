# Ollama App Integration Guide

Ollama 3편 글에서 사용하는 Python, JavaScript, Modelfile 예제입니다.

> 이 폴더는 Ollama를 단순히 터미널에서 실행하는 단계를 넘어, 실제 개발 코드에서 로컬 LLM을 호출하는 방법을 보여주는 학습용 샘플입니다.

---

## 📎 관련 아티클

- [Ollama를 개발에 붙이는 방법: Python, JavaScript, Modelfile까지](https://tistory-cloud.tistory.com/entry/Ollama%EB%A5%BC-%EA%B0%9C%EB%B0%9C%EC%97%90-%EB%B6%99%EC%9D%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-Python-JavaScript-Modelfile%EA%B9%8C%EC%A7%80)

---

## ✅ 이 예제가 보여주는 것

- Python 공식 `ollama` 패키지로 로컬 모델 호출
- JavaScript 공식 `ollama` 패키지로 로컬 모델 호출
- `chat` API의 `messages` 구조 이해
- `Modelfile`로 시스템 프롬프트와 temperature 재사용
- 작은 예제를 실제 애플리케이션 호출 함수로 확장하는 기본 방향

---

## 📁 폴더 구조

```text
python/
  chat_example.py
javascript/
  chat_example.js
modelfile/
  Modelfile
requirements.txt
package.json
```

---

## 🚀 빠른 시작

### 1. 이 폴더로 이동합니다

```bash
cd cloud-public/ollama/series-examples/app-integration-guide
```

### 2. Ollama와 모델을 확인합니다

```bash
curl http://localhost:11434
ollama pull gemma3
```

### 3. Python 의존성을 설치합니다

```bash
pip install -r requirements.txt
```

### 4. Python 예제를 실행합니다

```bash
python python/chat_example.py
```

### 5. JavaScript 의존성을 설치합니다

```bash
npm install
```

### 6. JavaScript 예제를 실행합니다

```bash
npm run example
```

---

## 🧪 예제 파일 설명

| 파일 | 설명 |
|---|---|
| `python/chat_example.py` | Python에서 Ollama chat API를 호출하는 최소 예제 |
| `javascript/chat_example.js` | Node.js에서 Ollama chat API를 호출하는 최소 예제 |
| `modelfile/Modelfile` | 기본 모델, temperature, 시스템 프롬프트를 정의하는 예제 |
| `requirements.txt` | Python 예제 실행에 필요한 패키지 |
| `package.json` | JavaScript 예제 실행에 필요한 패키지와 npm script |

---

## 🧩 Modelfile 사용하기

`Modelfile`은 기존 모델 위에 재사용 가능한 설정을 얹는 파일입니다. 이 예제에서는 `gemma3`를 기반으로 간단한 한국어 기술 어시스턴트 설정을 만듭니다.

```bash
ollama create concise-ko-assistant -f modelfile/Modelfile
ollama run concise-ko-assistant
```

이후 코드에서 모델 이름을 바꾸면 커스텀 설정을 사용할 수 있습니다.

```text
gemma3 → concise-ko-assistant
```

---

## ⚠️ 사용 전 확인

- Ollama가 로컬에서 실행 중이어야 합니다.
- 예제 모델은 `gemma3`를 기준으로 작성했습니다.
- Node.js 예제는 ES Module 방식입니다. `package.json`의 `"type": "module"` 설정을 사용합니다.
- 실제 서비스에서는 예외 처리, timeout, 재시도, 로깅을 반드시 추가하세요.
- 브라우저 프론트엔드에서 Ollama API를 직접 호출하는 구조는 보안과 CORS 문제를 검토해야 합니다.

---

## 🧯 자주 막히는 지점

| 증상 | 확인할 것 |
|---|---|
| Python에서 `ollama` 모듈을 찾지 못함 | `pip install -r requirements.txt` 실행 여부 확인 |
| Node.js에서 import 오류 발생 | `npm install`과 `package.json`의 `type: module` 확인 |
| 모델 응답이 없음 | `ollama run gemma3`로 모델이 직접 응답하는지 먼저 확인 |
| Modelfile 생성 실패 | `modelfile/Modelfile` 경로에서 명령을 실행했는지 확인 |

---

## 다음 단계

코드에서 Ollama를 호출할 수 있게 되었다면 다음 단계는 응답 형식을 고정하는 것입니다.

```bash
cd ../structured-outputs-guide
```

다음 예제에서는 Pydantic, Zod, JSON Schema를 사용해 로컬 LLM 응답을 JSON으로 고정합니다.

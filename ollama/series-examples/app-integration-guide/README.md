# Ollama App Integration Guide

Companion sample folder for the article:

- [Ollama를 개발에 붙이는 방법: Python, JavaScript, Modelfile까지](https://tistory-cloud.tistory.com/entry/Ollama%EB%A5%BC-%EA%B0%9C%EB%B0%9C%EC%97%90-%EB%B6%99%EC%9D%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-Python-JavaScript-Modelfile%EA%B9%8C%EC%A7%80)

## What this sample covers

- Python 공식 라이브러리 호출 예제
- JavaScript 공식 라이브러리 호출 예제
- 시스템 프롬프트와 temperature를 재사용하기 위한 `Modelfile`

## Files

```text
python/chat_example.py
javascript/chat_example.js
modelfile/Modelfile
requirements.txt
package.json
```

## Install dependencies

```bash
# Python
pip install -r requirements.txt

# JavaScript
npm install
```

## Run the examples

```bash
python python/chat_example.py
npm run example
```

## Create a custom model from the Modelfile

```bash
ollama create concise-ko-assistant -f modelfile/Modelfile
ollama run concise-ko-assistant
```

## Notes

- 예제는 가장 작은 호출 흐름만 보여 줍니다.
- 운영 코드에서는 예외 처리, 타임아웃, 재시도, 로깅을 추가하세요.
- `Modelfile`은 재사용 가능한 설정을 저장하는 예제이지, 새로운 모델을 학습시키는 파일은 아닙니다.

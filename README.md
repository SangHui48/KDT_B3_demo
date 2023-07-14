# KDT_B3_demo

> 참고 : https://www.youtube.com/watch?v=lenV5aVOMp8

## backend setting

0. backend 디렉터리로 이동후
1. python -m venv (venv) => 가상환경 세팅
2. 가상환경 진입
3. pip install -r requirements.txt
4. python main.py 실행해서 서버 띄우기


## frontend setting

> node.js 설치되있는지 확인

* 이어서 개발할 경우
0. npm install
1. cd frontend
2. npm run serve


* 처음 부터 세팅할 경우
0. npm install -g @vue/cli
1. npm install --save-dev eslint eslint-plugin-vue
2. vscode에서 작업시 prettier, vue language feature extension 다운로드
4. vue create (frontend : 프로젝트명)
5. cd frontend
6. npm run serve

backend와 연결
7. npm install axios
8. npm install bootstrap@4.6.0 --save


* frontend
    src
        assets: 정적 파일 저장되는곳
        components: 화면 구성하는 파일, UI, css 같은 화면 디자인 적용은 여기서 하면됨
        router: routing 관련
        
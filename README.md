
# n8n-docker 실행 가이드

아래는 레포지토리를 Git으로 Clone한 뒤 `n8n-docker` 프로젝트를 실행하는 방법에 대한 상세 가이드입니다.
#### 설치가 완료되면 다음의 URL이 접속 주소 입니다. localhost를 ngrok domain을 넣을 경우, 해당 도메인 주소로 변경해도 접속이 가능 합니다. 다만, traefik은 인터넷을 접속 할 수 없습니다.
    - traefik : http://localhost:8080
    - n8n : http://localhost/n8n
    - ngrok : http://localhost/ngrok
    - fastapi-app : http://localhost/fastapi-app/docs
---
---

## 1. 레포지토리 Clone 완료 상태
- 이미 Git을 통해 `https://github.com/pollux-choh/n8n-docker.git` 레포지토리를 Clone했다고 가정합니다.
- Clone된 경로는 `D:\ws-n8n\n8n-docker`입니다.

---

## 2. Docker 네트워크 및 볼륨 생성
프로젝트 실행 전에 Docker 네트워크와 볼륨을 생성해야 합니다.

1. **Docker 네트워크 생성**
   - 다음 명령어를 실행하여 `proxy`라는 네트워크를 생성합니다:
     ```bash
     docker network create proxy
     ```

2. **Docker 볼륨 생성**
   - 다음 명령어를 실행하여 `n8n_data`라는 볼륨을 생성합니다:
     ```bash
     docker volume create n8n_data
     ```

---

## 3. 환경 변수 설정하기
프로젝트 실행 전에 `.env` 파일을 생성하여 필요한 환경 변수를 설정해야 합니다.

### 방법 1: 명령 프롬프트를 사용해 생성
1. **명령 프롬프트 실행**:
   - 시작 메뉴에서 **cmd**를 검색하고 실행합니다.
2. **`.env` 파일 생성**:
   ```cmd
   cd D:\ws-n8n\n8n-docker
   echo. > .env
   ```

### 방법 2: 파일 탐색기를 사용해 생성
1. **파일 탐색기 열기**:
   - `D:\ws-n8n\n8n-docker` 폴더로 이동합니다.
2. **새 파일 생성**:
   - 마우스 오른쪽 클릭 > **새로 만들기(New)** > **텍스트 문서(Text Document)**를 선택합니다.
3. **이름 변경**:
   - 생성된 파일의 이름을 `.env`로 변경합니다.
   - 파일 확장자가 보이지 않는 경우:
     - 파일 탐색기 메뉴 > **보기(View)** > **파일 이름 확장명(File name extensions)**을 체크합니다.
   - 이후 이름을 `.env`로 변경하세요.

### 방법 3: PowerShell을 사용해 생성
1. **PowerShell 실행**:
   - 시작 메뉴에서 **PowerShell**을 검색하고 실행합니다.
2. **`.env` 파일 생성**:
   ```powershell
   cd D:\ws-n8n\n8n-docker
   New-Item -Path . -Name ".env" -ItemType "File"
   ```

3. **환경 변수 추가**
   - `.env` 파일을 열어 아래 내용을 입력합니다:
     ```env
     NGROK_AUTHTOKEN=your_ngrok_auth_token
     NGROK_API_KEY=your_ngrok_api_key
     NGROK_DOMAIN_NAME=your_custom_domain_name
     ```
   - 각 값(`your_ngrok_auth_token`, `your_ngrok_api_key`, `your_custom_domain_name`)을 실제로 사용하려는 값으로 대체하세요.

---

## 4. Dockerfile 빌드
`fastapi-app` 디렉토리에 있는 Dockerfile을 빌드하여 이미지를 생성합니다.

1. **`fastapi-app` 디렉토리로 이동**
   ```bash
   cd fastapi-app
   ```

2. **Docker 이미지 빌드**
   - 다음 명령어를 입력하여 Docker 이미지를 빌드합니다:
     ```bash
     docker build -t fastapi-app .
     ```
   - 빌드가 완료되면 이미지가 생성됩니다.

---

## 5. docker-compose 실행
`docker-compose.yml` 파일을 실행하여 모든 서비스를 시작합니다.

1. **프로젝트 루트 디렉토리로 이동**
   ```bash
   cd ..
   ```

2. **docker-compose 실행**
   - 다음 명령어를 입력하여 서비스를 시작합니다:
     ```bash
     docker-compose up -d
     ```
   - `-d` 옵션은 백그라운드에서 실행되도록 설정합니다.

---

## 6. 실행 상태 확인
1. **Docker 컨테이너 상태 확인**
   - 다음 명령어를 실행하여 컨테이너가 정상적으로 실행 중인지 확인합니다:
     ```bash
     docker ps
     ```
   - 실행 중인 컨테이너 목록에 `fastapi-app` 및 기타 관련 서비스가 표시되어야 합니다.

2. **서비스 접속**
   - 브라우저에서 `NGROK_DOMAIN_NAME`을 통해 서비스에 접속합니다.
   - 예: `https://your_custom_domain_name`

---

## 7. 서비스 종료
- 실행 중인 서비스를 중단하려면 아래 명령어를 사용합니다:
  ```bash
  docker-compose down
  ```

---

## 추가 정보
- **로그 확인**
  - 특정 컨테이너의 로그를 확인하려면:
    ```bash
    docker logs <container_id>
    ```
- **이미지 삭제**
  - 빌드된 Docker 이미지를 삭제하려면:
    ```bash
    docker rmi fastapi-app
    ```

---

이 가이드를 따라 `n8n-docker` 프로젝트를 성공적으로 실행할 수 있습니다. 🌟

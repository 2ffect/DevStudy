# Git
**Git** - 분산 버전 관리 시스템

**버전 관리** - 변화를 기록하고 추적하는 것
---
### * 명령어
- git init : 로컬 저장소 설정 (초기화)
- git add : 변경 사항이 있는 파일을 staging area에 추가
- git commit -m '메세지' :  staging area 에 있는 파일들을 저장소에 기록 ( 해당 시점에서 버전을 생성하고 이력을 남김)
- git config —global user.email “메일주소” : commit 작성자 정보 설정
- git config —global user.name “유저네임” : commit 작성자 정보 설정
- git log : commit history 조회

- git status : 현재 로컬 저장소의 파일 상태 확인

- gif config --global alias.st 'status' : git status 명령어를 git st로 간단하게 설정가능

- git remote add origin **remote_repo_url**  : 로컬 저장소에 원격 저장소 추가 ( 볼드체에 레퍼지토리 url 을 입력 )

- git remote remove origin : origin에 연결 된 레퍼지토리의 연결 끊기.

- git remote -v : 현재 연결 된 원겨 저장소 확인인

- git push origin master : 원격 저장소에 commit 목록을 업로드  **commit 이력이 없으면 push 할 수 없다.**

- git pull origin master :  원격 저장소의 변경사항만을 받아옴 (업데이트 된)

- git clone remote_repo_url :  원격 저장소 전체를 복제 (다운로드) *  이미 git init이 되 있음.

- git pull —rebase origin master : 로컬 브랜치의 변경 사항을 원격 브랜치 위에 재적용

- git config --global --list : global 설정 된 config 리스트 확인

- git config --unset --global “해제할 것것” : global 설정 된 config 해제

# Gitignore
- Git 에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍스트 파일 (프로젝트에 따라 공유하지 않아야 하는 것들도 존재하기 때문에 활용)

### * 주의사항
- 이미 git의 관리를 받은 이력이 있는 파일이나 디렉토리는 추후 gitignore에 작성해도 적용되지 않음.
- git rm --cached : 명령어를 통해 git 캐시에서 삭삭제 필요
### * gitignore 목록 생성 서비스
- 운영체제, 프레임워크, 프로그래밍 언어 등 개발 환경에 따라 gitignore 목록을 만들어주는 사이트
- https://www.toptal.com/developers/gitignore/


# fork

- 노래로 치면 편곡의 느낌. 다른 사람의 레퍼지토리를 출처를 남긴 상태로 내 레퍼지토리로 가져와 수정 할 수 있음. 
- 오픈소스 활용해서 개발 할 때 씀. (버그 수정 반영 등)
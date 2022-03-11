### 저장소 복제 혹은 업데이트

- 최초 바탕화면에서 Git bash 열어서 `clone`

```shell
$ git clone <주소>
```

- 이후 바탕화면 폴더에서 Git bash 열어서 `pull`

```shell
$ git pull origin master
```

### 프로젝트 진행

- `pjtxx` 폴더를 바탕화면에 복사-붙여넣기를 해주세요.
- 바탕화면에 있는 `pjtxx` 폴더에서 git 저장소로 초기화 해주세요.

```shell
$ git init
```

- `commit`을 해주세요.

```shell
$ git add .
$ git commit -m 'Init'
```

- GitLab에서 `pjtxx` 라는 프로젝트를 생성하고 원격저장소 설정을 해주세요.

```shell
$ git remote add origin <주소>
```

- 원격저장소에 `push`를 해보세요. (확인)

```shell
$ git push origin master
```

- 프로젝트를 하고 `commit`, `push`를 합니다.
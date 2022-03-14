# 03.11

## Git_branch



<br>

### branch를 사용하는 이유?

* branch는 가볍고 빠르다. 

  1. master : 상용이라고 생각하면됨. 공개용

  2. branch : 코드를 수정, 삭제해야하는 경우가 필요할 때 사용한다. 별도의 branch를 가지 치기한 후  변경사항을 만든다. 

<br>

### branch 사용하기

* **git의 기본 명령어**

  ```bash
  git init
  ```

  ```bash
  # 브랜치 목록 확인
  git branch
  ```

  ```bash
  # 새로운 브랜치 생성
  git branch <브랜치 이름>
  ```

  ```bash
  # 특정 브랜치 삭제
  git branch -d <브랜치 이름> : 병합된 브랜치만 삭제
  git branch -D <브랜치 이름> : 강제 삭제
  ```

  ```bash
  # 다른 브랜치 이동 -> 그 당시의 버전으로 넘어가기 때문에 그 시점의 모습으로 바뀜
  git switch <브랜치 이름>
  git switch -c <브랜치 이름> : 브랜치를 새로 생성과 동시에 이동
  ```

  * git switch 사용 전에 주의사항!

    :small_red_triangle: working directory의 관리를 받고 있는지 확인하기 : 새로운 branch를 만들어도 버전관리(commit)를 해주어야 독립적인 관리를 받을 수 있다. switch 하기 전에 버전 관리 해주어야 한다. 

  * (HEAD -> master) : 가장최신 버전을 바라보고 있다는 의미이다.

  * branch를 생성한 곳에서 머물러 있다.

* **편리한 명령어**

  ```bash
  # 한줄로 정렬
  git log --oneline
  git log --oneline --all
  # 가지치기
  git log --oneline --all --graph  
  ```

<br>

### merge (병합)

* branch와 branch 병합

* **git의 기본 명령어**

  :small_red_triangle_down: merge하기 전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야 함.

  ```bash
  git merge <병합할 브랜치 이름>
  ```

1. **fast-forward** : A 브랜치와 B 브랜치를 병합할 때 두 브랜치가 동일한 커밋을 바라보도록 한다. merge를 하면 새로운 버전이 생겨야 하는데 그렇지 않고, master에 아무 행동도 하지 않았다면 새로운 버전을 만들지 않아도 된다고 판단한다. 단순히 새로운 버젼을 만들었다고 생각!

   :star: merge된 branch는 삭제하기! (login 브랜치는 삭제 명령어를 통해 삭제한다.)

2. **3-way-merge (merge commit)** : A의 커밋과 B의 커밋의 공통된 조상을 찾아서 커밋한다. 별도로 커밋 이름을 지정하지 않아도 자동으로 생성된다.

3. **merge conflict** 

   * merge하는 두 브랜치에서 같은 파일의 같은 부분을 동시에 수정하고 merge하면 git은 해당 부분을 자동으로 merge 해주지 못한다.

   * 반면 동일 파일이더라도 서로 다른 부분을 수정했다면 conflict 없이 자동으로 merge commit 된다.

   * 충돌을 수정 후

     ```bash
     git add .
     git status
     git commit 
     # vim 화면 보임
     esc+:+wq
     ```

     ![image-20220311104828740](git branch.assets/image-20220311104828740.png)

4. ```bash
    # cjeckout -> switch로 변화
    git checkout == git switch
   ```
   
   

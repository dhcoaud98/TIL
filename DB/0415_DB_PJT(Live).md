# 04.13

## DB 02_Git+PJT07

[TOC]

<br>

### 1. GIT 

#### 1.Undoing things (되돌리기)

1. **파일 내용을 수정 전으로 되돌리기 **

   `add .` 하기 전이다.  수정 사항을 모두 제거하므로 수정사항이 많을 때는 주의 해야 한다. 

   ```bash
   $ git restore <file>	
   ```

2. `staging area -> working directory`

   `commit`이 없을 경우이고, `add .`한 후 에 `staging area`에 올라가 있는 경우 

   ```bash
   $ git rm --cached test.md
   ```

   이전 `commit`이 있을 경우 

   ```bash
   $ git restore --staged test.md
   ```

3. **바로 직전 완료한 커밋 수정하기**

   * 커밋 메시지만 수정 : 마지막으로 커밋하고 나서 수정한 것이 없을 때(커밋하자마자 바로 이 명령을 실행하는 경우)

   ```bash
   # A를 수행하고 B라고 커밋한 경우 
   
   $ git commit -m 'B feature completed'
   $ git log
   $ git commit --amend
   hint: Waiting for your editor to close the file..[master c01f908] Add no.txt
   ...
   
   A feature completed
   $ git log  #g 해시 값 변경
   ```

   * 파일 하나를 빼고 커밋 해버린 경우

   ```bash
   $ touch foo.txt bar.txt
   $ git add foo.txt
   
   $ git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           new file:   foo.txt
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           bar.txt
           
   $ git commit -m "foo & bar"
   [master 4221af6] foo & bar
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 foo.txt
    
   $ git status
   On branch master
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           bar.txt
           
   $ git add bar.txt  # 누락된 파일을 S.A로 옮긴다. 
   
   $ git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           new file:   bar.txt
           
   $ git commit --amend
   foo & bar  # Vim 편집기가 열리면 커밋 메시지 수정하기
   $ git commit --amend  # 해시 값이 변경된다. 
   [master 7f6c24c] foo & bar
    Date: Mon Jun 7 22:32:58 2021 +0900
    2 files changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 bar.txt
    create mode 100644 foo.txt
   ```

   * `--amend` 옵션으로 커밋을 고치는 작업이 주는 장점은 마지막 커밋 작업에서 뭔가 빠뜨린 것을 넣거나 변경하는 것을 새 커밋으로 분리하지 않고 하나의 커밋에서 처리하는 것이다. 이전의 커밋은 일어나지 않은 일이 되는 것이고, 히스토리에도 남지 않는다. 

<br>

#### 2. Reset & Revert

> `Reset`과 `Revert`의 공통점은 '과거로 되달린다'라는 행위이나 '과거로 되돌리겠다는 내용도 기록이 되는가(==commit 이력에 남는가)'의 차이가 있다. 

1. **Git reset**

   가끔 앱을 사용하다가 업데이트를 했는데, 오히려 예전 버전이 더 좋다고 느낄 때가 있다. 이처럼 예전 버전으로 돌아가고 싶을 때?

   ```bash
   $ git reset [옵션] <커밋 ID>
   # 특정 커밋 상태로 되돌아가며 해당 커밋 이후로 쌓아 놨던 커밋들은 전부 사라진다. 
   ```

   **옵션**

   1. `--soft` : 돌아가려는 커밋으로 되돌아가고, 이후의 commit된 파일들을 스테이징에어리어에 돌려 놓는다. 다시 커밋할 수 있다. 
   2. `--mixed` : 돌아가려는 커밋으로 되돌아가고, 이후의 commit된 파일들을 `working directory`로 돌려 놓는다. `unstage`상태로 남는다. 
   3. `--hard` : 돌아가려는 커밋으로 되돌아가고, 이후의 commit된 파일들은 모두 `working directory`에서 **삭제** 된다.

   [참고사항]

   이미 삭제한 커밋으로 돌아가고 싶다면? `git reflog`를 사용함 

   ```bash
   $ git reflog
   1a410ef HEAD@{0}: reset: moving to 1a410ef
   ab1afef HEAD@{1}: commit: modified repo.rb a bit
   484a592 HEAD@{2}: commit: added repo.rb
   
   $ git reset --hard <복구하고자 하는 커밋ID>
   ```

2. **Git revert**

   커밋 내역이 사라지지 않는다.  특정 사건을 없었던 일로 만드는 행위로써, 이전 커밋을 취소한다는 새로운 커밋을 만든다. `git reset`은 커밋 내역을 삭제하는 반면, `git revert`는 새로 커밋을 쌓는 다는 차이가 있다. 

   ```bash
   $ git revert <커밋 ID>
   ```

   ```bash
   $ git log --oneline
   20d320d third
   1eb059e second
   6baf32f first
   
   $ git revert 1eb059  
   # second 커밋에 있었던 2.txt가 사라진 것을 확인
   # second 커밋을 없었던 일로 만드는 것
   
   $ git log --oneline
   f0b5364 (HEAD -> master) Revert "second" # 새로 쌓인 커밋
   20d320d third
   1eb059e second # 히스토리는 남아있음
   6baf32f first
   ```

   

<br>

#### 3. Switch & Restore

- `checkout`

  - Switch branches or restore
- `switch`

  - Switch branches
- `restore`

  - Restore working tree files

**기존 `checkout` 의 많은 책임을 깔끔하게 분리하여 각각 명확하게 구분 하기 위함**

---

**브랜치 이동**

```bash
# 기존
$ git checkout 브랜치명

# 신규
$ git switch 브랜치명
```



**브랜치 생성 및 이동**

```bash
# 기존
$ git checkout -b 브랜치명

# 신규
$ git switch -c 브랜치명
```



**Unstaged 상태의 변경(modified) 파일을 복구**

```bash
# 기존
$ git checkout -- README.md

# 신규
$ git restore README.md
```




🎈 Algorithm Study
====================================

**팀장 : `김윤빈`**

**팀원 : `권예빈`,`성루비`, `임광훈`**

**졸업자 : `정예울`**,**`김영균`**

<br>

---

## 🎉Intro

-	💁 누가? : SSAFY_계란3반
-	🎁 무엇을? : [백준](https://www.acmicpc.net/) , [SWEA](https://swexpertacademy.com/main/code/problem/problemList.do) 알고리즘 문제
-	⏰ 언제? : 평일 08:00 ~ 09:00
-	🏛 어디서? : Webex / Discord
-	✏️ 어떻게? : [백준 문제장](https://velog.io/@kimyunbin/Stack-%EB%AC%B8%EC%A0%9C-%ED%92%80%EA%B8%B0)을 기준으로 풉니다

<br>

---

## ❗❗ 스터디 진행 과정 및 Github Push 방법❗❗

- [🐣튜토리얼](files/tutorial.md)을 진행하는 것으로 스터디에 참여해보세요!

- 출제자

  1. 최신화 작업을 위해 master에서 PULL 받아오기

     ```bash
     $ git pull origin master
     ```

  2. README.md에 주차별 문제 링크 추가하기

     1. 스터디 이루어지는 날 작성 `ex) (21.01.01)`
     2. 문제 추가 `ex) 사이트_문제번호_문제이름`

  3. **``Study/week_x/사이트_문제번호_문제이름/input.txt``** 넣기

  4. master에 올려주기

     ```bash
     $ git add .
     $ git commit -m '출제날짜_사이트_문제번호_문제이름_출제자'
     $ git push origin master
     ```

- 스터디원 모두

  1. 본인 branch로 이동한 뒤, master에 있는 최신 파일 PULL 받아오기

     ```bash
     $ git switch 본인branch이름
     ```

     ```bash
     $ git pull origin master
     ```

  2. 각 주차별 해당 문제 폴더에 들어가서

     `문제위치_문제번호_문제이름_본인이름.py`,

     `solution_본인이름.md`

     두 파일 추가한 뒤, 본인 branch에서 커밋 메세지 잘 지켜 푸쉬하기

     ```bash
     $ git add .
     $ git commit -m '커밋 메세지'
     $ git push origin 본인branch이름
     ```
     
  3. 레포로 다시 돌아와서 Pull requests 탭 들어온 다음에 create pull request 까지만하기

     Merge❌❌❌

  4. 스터디 끝나고 Merge가 완료된 후 branch 삭제하기
  
     >  관리자가 원격에 있는 브랜치는 삭제한 상태이므로 로컬  branch만 삭제해주기
  
     ```bash
     $ git switch master
     
     (master)
     $ git pull origin master  
     $ git branch -d 본인 branch 이름
     ```

<br>

---

## 📨 Github Commit Message

- [💡Commit Message](files/Commit_Meessage.md)을 참고해서 커밋 메시지를 작성해주세요!

<br>

---

## 📅 스터디 진행

<br>

### 21.02~21.06

- 문제 출제 :  백준과 SWEA에서  매주 1문제씩
- 문제 풀이 : 매주 화요일, 목요일 20:00에 디스코드에서 서로의 풀이를 공유
- [1학기 진행 상황 ](Study/1st/README.md)

<br>

### 21.07~ 

- 문제 출제 : [백준 온라인 강의 알고리즘 기초](https://code.plus/course/41) 를 바탕으로 한 유형별 문제 풀이 
- 문제 풀이: 매주 평일 08:00~09:00에 디스코드에서 모각코 진행 
- [2학기 진행 상황](Study/2st/README.md)


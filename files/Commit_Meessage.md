# ๐Commit Message ์์ฑ๋ฒ

## ๐ฉ๐ปโ๐ซ์ถ์ ์

```bash
$ git add .
$ git commit -m '๋ ์ง_์ฌ์ดํธ_๋ฌธ์ ๋ฒํธ_๋ฌธ์ ์ด๋ฆ_์ถ์ ์'
$ git push origin master
```

<br>

---

## ๐ฉ๐ปโ๐์คํฐ๋์ ๋ชจ๋

```bash
# ๋ณธ์ธ branch๋ก ๋ฐ๋์ด ์๋ ํ์ธ

$ git add .
$ git commit -m "์ปค๋ฐ ๋ฉ์ธ์ง"
$ git push origin ๋ณธ์ธ branch๋ก ์ด๋ฆ
```

Commit ์นดํ๊ณ ๋ฆฌ๋ฅผ ํฌ๊ฒ 3๊ฐ์ง๋ก ๋๋๋ค.

> C : Create

> U : Update

> D : Delete



## Type : C

๋ณธ์ธ์ด ํผ ์ฝ๋๋ฅผ ์ฌ๋ฆด ๋ ์ฌ์ฉํ๋ค.

> **`Create ์ฌ์ดํธ_๋ฌธ์ ๋ฒํธ_๋ฌธ์ ์ด๋ฆ_๋ณธ์ธ์ด๋ฆ`**

```bash
$ git commit -m "Create BOJ_1004_์๊ณ ๋ฆฌ์ฆ_bomin"
```

๋ค๋ฅธ ํ์ด ๋ฐฉ๋ฒ์ ๋ ์ฌ๋ฆฌ๊ณ  ์ถ๋ค๋ฉด **`Create ์ฌ์ดํธ_๋ฌธ์ ๋ฒํธ_๋ฌธ์ ์ด๋ฆ_๋ณธ์ธ์ด๋ฆ_x`**

```bash
$ git commit -m "Create BOJ_1004_์๊ณ ๋ฆฌ์ฆ_bomin_1"
```

```bash
$ git commit -m "Create BOJ_1004_์๊ณ ๋ฆฌ์ฆ_bomin_2"
```



## Type : U

๋ฌธ์ ๋ฅผ ๋ค์ ํ์๊ฑฐ๋, ์์ ํ์ ๊ฒฝ์ฐ ์ฌ์ฉํ๋ค.

> **`Update ์์ ํ ์ด์ (์งง๊ฒ)`**

```bash
$ git commit -m "Update ์์ ํ ์ด์ "
```

์ด๋ค ๋ถ๋ถ์ ์ด๋ป๊ฒ ์์ ํ๋์ง ๋ ์์ธํ๊ฒ ์ ๊ณ  ์ถ๋ค๋ฉด ์ค์ ๋ฐ๊พธ๊ณ  ๋ด์ฉ์ ์์ฑํ๋๋ก ํ๋ค.

```bash
$ git commit -m "Update ํ์ด ์์ 
์ด๋ถ ํ์ ๋ฌธ์ ๋ก ์ ๊ทผํ๊ณ  ํ์ด์ ํ๋ ธ์ต๋๋ค๋ฅผ ๋ฐ์์ง๋ง, DP ๋ฐฉ์์ผ๋ก ์ ๊ทผํด์ ๋ฌธ์ ๋ฅผ ํ ์ ์์์ต๋๋ค."
```



## Type : D

ํ์ผ์ ์ญ์ ํ๋ ๊ฒฝ์ฐ ์ฌ์ฉํ๋ค.

์ญ์ ๋ฅผ ์งํํ  ๊ฒฝ์ฐ ์ ์ญ์ ํ๋์ง ์ด์ ๋ฅผ ๋ด์ฉ์ ์์ฑํ๋๋ก ํ๋ค

> **`Delete ์ฌ์ดํธ_๋ฌธ์ ๋ฒํธ_๋ฌธ์ ์ด๋ฆ_๋ณธ์ธ์ด๋ฆ_์ญ์ ์ด์ `**

```bash
$ git commit -m "Delete BOJ_1004_์๊ณ ๋ฆฌ์ฆ_bomin
๋ค๋ฅธ ๋ฌธ์  ํ์ด๊ฐ ์ฌ๋ผ๊ฐ์ต๋๋ค"
```
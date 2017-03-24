---
layout: post
title:  "自由群"
date:   2017-03-12 00:00:00 +0800
categories: 代數與組合
---

自由群
========

自由群是一種特殊的群，它的迷人之處在接下來會一一看到，不過在這之前要先刻畫一下自由群的樣貌。

[TOC]

許多群都不是阿貝爾群，但我們仍能確定它的某些元素會滿足交換率，例如：

-  <script type="math/tex">a^{-1}\cdot a = e = a \cdot a^{-1}</script>
-   <script type="math/tex">a^3\cdot a^2 = a^5 = a^2\cdot a^3</script>

可見一個元素 <script type="math/tex">a</script> 與它的高次方 <script type="math/tex">a^n</script> 或反元素的高次方 <script type="math/tex">a^{-m}</script> 之間無可避免的會有交換率，在任何群都如此。

而自由群某種意義上可以看成是一個交換率最少的群。除非滿足以上的情況，否則 <script type="math/tex">a\cdot b \neq b \cdot a</script>。來看看它的定義。

一、定義
-------------

給定一個字符的集合 <script type="math/tex">S=\{a, b, c, ...\}</script> ，我們都可以用以下方法構造出一個群 <script type="math/tex">F_S</script>，它是由字串構成的集合：

1. 規定 <script type="math/tex">a, b, c, ...</script> 等字都是 <script type="math/tex">F_S</script> 中的字串（只有一個字的字串）。

2. 規定單位元素 <script type="math/tex">\varepsilon</script> （空字串）與符號 <script type="math/tex">a^{-1}</script>, <script type="math/tex">b^{-1}</script>, <script type="math/tex">c^{-1}</script> 也都是 <script type="math/tex">F_S</script> 中的字串。

3. 兩個字串 <script type="math/tex">a</script> 和 <script type="math/tex">b</script> 的相乘結果定為新字串 <script type="math/tex">ab</script> ，也就是單純串起來。

4. 一個字串與其他字串相乘可以串成更長，如 <script type="math/tex">(ab)\cdot (c^{-1}a) = (abc^{-1}a)</script> 這樣，越串越長。這些字串也在 <script type="math/tex">F_S</script> 裡面。

5. 如果字串有相鄰的 <script type="math/tex">k</script> 與 <script type="math/tex">k^{-1}</script> 則可以消掉，如 <script type="math/tex">a^{-1}b^{-1}bbc = a^{-1}bc</script>，有相鄰的同樣字符也可以簡寫為次方，如 <script type="math/tex">abbba = ab^3a</script>。

這個 <script type="math/tex">S</script> 就稱為 <script type="math/tex">F_S</script> 的生成集，<script type="math/tex">S</script> 的元素稱為生成元。

二、就只是符號
-----------------------

注意到這些 <script type="math/tex">\{a, b, c, ..., a^{-1}, b^{-1}, c^{-1}, ... , ab, ab^{-1}a, bca^{-1}b^2, a^6...\}</script> 都只是字串，而不是某個群中的未知數。然而特別的地方就是：即便我們把自由群運算規則中的 <script type="math/tex">a,b,c</script> 等符號用其他群的元素取代，這些替換後的「句子」仍然有意義。

例如把 <script type="math/tex">a,b,c</script> 取代成 <script type="math/tex">\mathbb R^+</script> 中的元素 <script type="math/tex">3,2,4</script>，那麼前面第 5 點的字串 <script type="math/tex; mode=display">a^{-1}b^{-1}bbc = a^{-1}bc</script> 會被取代成 <script type="math/tex; mode=display"> \frac{1}{3}\cdot\frac{1}{2}\cdot 2\cdot 2 \cdot 4 = \frac{1}{3} \cdot 2 \cdot 4 </script>，果然左右算式的確是相等的，但那也只是消掉一組倒數而已。或許你會覺得這個取代後的實數乘法簡直是理所當然的廢話，那是因為替換前的字串就是記載著廢話的結構，自由群就是所有關於乘法（或加法）的廢話的蒐集。

> 自由群 <script type="math/tex">F_S</script> 利用符號在做一些「本來就會對」的乘法。

這有時稱為自由群的泛性質，這裡不介紹什麼是泛性質。

不過取代的動作不能套用到不等式中。在自由群中 <script type="math/tex">ab \neq ba</script>是相異的字串，但是照剛剛的取代 <script type="math/tex">3\cdot 2\neq 2\cdot 3</script> 就錯了。因為不等號並不是什麼運算規則。


三、自由群的凱萊圖 (Cayley Graph)
------------------------------

下列這張圖取自維基百科，是自由群 <script type="math/tex">F_{\{a,b\}}</script> 的凱萊圖，上面每個頂點都代表 <script type="math/tex">F_{\{a,b\}}</script> 中的一個字串：中心點是空字串，從中心往右邊走一個線段等於乘上 <script type="math/tex">a</script>，往左則是乘以 <script type="math/tex">a^{-1}</script>；往上是乘以 <script type="math/tex">b</script>，往下則是 <script type="math/tex">b^{-1}</script>。

![cayley graph of free 2](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Cayley_graph_of_F2.svg/240px-Cayley_graph_of_F2.svg.png)

在圖中「向右再向上」與「向上再向右」會走到不同點，可見 <script type="math/tex">ab\neq ba</script>。由於這個圖形是無限分支下去的，因此無論多長的字串，在圖中都找得到對應點，就照著字串上的行進方向一直走就是了。。

這個圖形每個接口都是四叉路，如果換成三個生成元的自由群，圖形的每個接口就是六叉路；如果只有一個生成元，那這個自由群與無限循環群 <script type="math/tex">\mathbb Z</script> 無異，圖形就是一直線。

其實這張圖可以不用畫成碎形，但是為了在畫面上擠下這麼多分枝，通常都是會畫成碎形，而且也很好看。

四、群的展示 (Presentation of Groups)
-----------------------

要寫出一個群，除了寫出它約定俗成的名稱（如 <script type="math/tex">\mathbb Z_2</script>）或寫出它的凱萊表 (Cayley Table)，還有一個常用的方式是利用群的展示 (Presentation of Groups)：列出它的所有生成元 <script type="math/tex">S</script>、以及生成元之間該有的關係 <script type="math/tex">R</script>，寫成 <script type="math/tex">\langle S|R \rangle</script>。

例如兩個無限循環群的直積 <script type="math/tex">\mathbb Z \otimes \mathbb Z </script>，寫成 <script type="math/tex">\langle a,b\ |\ ab=ba\rangle</script>，而有限循環群 <script type="math/tex">\mathbb{Z}_n</script> 寫成 <script type="math/tex">\langle a\ |\ a^n=e\rangle</script>.

關於群的展示一言難盡，詳細說明可以看[維基百科：群的展示](https://zh.wikipedia.org/wiki/%E7%BE%A4%E7%9A%84%E5%B1%95%E7%A4%BA)。

方才說自由群 <script type="math/tex">F_S</script> 是交換律最少的群，非不得已任兩個元素之間都沒有交換律（<script type="math/tex">ab</script> 字串與 <script type="math/tex">ba</script> 字串是不同字串），這可以看成自由群的生成元之間不存在任何關係，因此由 <script type="math/tex">S=\{a,b,c,...\}</script> 生成的自由群 <script type="math/tex">F_S</script> 寫起來就是 <script type="math/tex">\langle S\ |\ \varnothing\rangle</script>.

從凱萊圖上看起來，自由群的生成元之間不存在任何關係，代表它的凱萊圖上沒有迴路。當我們在寫其他群 <script type="math/tex">G</script> 的展示，其實是準備一個由 <script type="math/tex">G</script> 的生成元 <script type="math/tex">S</script> 生成的自由群 <script type="math/tex">F_S</script>，再把 <script type="math/tex">F_S</script> 的凱萊圖上的某些「樹枝」整捆整捆拗在一起。

[comment]: <> (為了滿足封閉性就勉強把相加後的新元素（囫圇吞棗地）塞到這個群之中。)

[comment]: <> (將自由群中的字串對應到其中 <script type="math/tex">'a'</script> 這個字元的出現次數，而 <script type="math/tex">a^{-1}</script> 出現的次數就算負的。這個對應 <script type="math/tex">N_a(str)</script> 是一個到整數 <script type="math/tex">(\mathbb{Z}, +)</script> 的同態，我們可以檢驗下面的例子： <script type="math/tex; mode=display">N_a(aabcaa) + N_a(a^{-1}bb) = 4 + (-1) = N_a(aabcaa \cdot a^{-1}bb)</script>)


五、自由么半群
------------------------

自由么半群的部份是針對電腦科學的討論，可以忽略。

研究過計算理論或形式語言的同學可能會覺得自由群很像 regular expression 中的 `*` 算符（Kleene star），例如 `{a,b}*` 會匹配 `{'',a,b,ab,ba,aba,bab,bba,bbb,aab...}` 等所有字串。

與自由群不同的是，利用 Kleene star 製造不出含有 <script type="math/tex">a^{-1}</script>、<script type="math/tex">b^{-1}...</script> 的字串，因此 Kleene star 並不會替你製造一個自由群：它製造的是「自由么半群」。所謂[么半群](https://zh.wikipedia.org/wiki/%E5%B9%BA%E5%8D%8A%E7%BE%A4) (Monoid) 是一種比群更弱的結構，么半群中並不要求反元素的存在。

除此之外 Kleene star 是給你一個集合，而不是代數結構，代表它製造出自由么半群之後便讓那個么半群忘掉自己的運算模式，成為一個純粹的集合。從範疇論來說就是先丟進一個*自由函子*成為么半群，再用*遺忘函子*打回集合的原形。
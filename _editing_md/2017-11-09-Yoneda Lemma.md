
圖解 Yoneda Lemma
================

本文將會以初等的角度來圖解 Hom functor、Natural transformation、證明 Yoneda lemma 並舉例。

<!-- TOC -->

- [Notations](#notations)
- [Functors](#functors)
    - [Covarent functor](#covarent-functor)
    - [Contravarient functor](#contravarient-functor)
- [The Hom Functor](#the-hom-functor)
    - [Hom functor](#hom-functor)

<!-- /TOC -->

本人是範疇論的初學者，若有錯誤請不吝指正。主要參考的書是 *《The Joy of Cats, Abstract and Concrete Categories》*，其他的參考書目附錄在文末。

## Notations

範疇：

- $\mathcal C, \mathcal D, ...$: 某些不特定的 locally small category. 
- $\mathbf {Set}$: the category of sets.
- $\mathbf {Grp}$: the category of groups. 這並不是 a group as a category.

記號：

- $\operatorname{Ob}(\mathcal C)$: the collection of objects in a category $\mathcal C$. 其中的物件以明體字 $A,B,...$ 表示.
- $\operatorname{Hom}(A,B)$: the collection of morphisms from $A$ to $B$.

在此我們忽略某些範疇「過大」的問題，例如 $\operatorname{Ob}(\mathbf{Set})$ 並不構成一個集合（我們也沒有要求它是集合）。

在範疇 $\mathbf{Set}$ 中，$\operatorname{Hom}(A,B)$ 總是一個集合，這是沒問題的。可想而知，兩個空間之間的所有連續函數、兩個群之間的所有 homomorphism（同態）也能形成集合（而不會太多），因此 $\mathbf{Grp}$、$\mathbf{Top}$、$\mathbf{Set}$ 等等都是 locally small 的。

## Functors

為了統一風格，先來看 functor 的記號。

### Covarent functor

一個 [functor](https://en.wikipedia.org/wiki/Functor#Definition) $F:\mathcal C\to\mathcal D$ 能將範疇 $\mathcal C$ 中的 diagram $$A\overset{f}{\longrightarrow} B$$ 變成 $\mathcal D$ 中的 diagram $$F(A)\overset{F(f)}{\longrightarrow}\mathcal F(B).$$ 畫起來就是從 $\mathcal C$ 拉一張窗簾到 $\mathcal D$：

?

並且 preserve composition：

?

也 preserve $\operatorname{Id}_A$：

?

### Contravarient functor

另一種 functor 能夠讓箭頭變方向，要取另外一個名字，稱之為 contravarient functor（反變函子）：

?

而之前保持讓箭頭同方向的 functor 也相對地稱為 covarient functor（協變或共變函子）。

<!-- ## Locally Small Categories

在此，我們稱一個範疇是 concrete 的，代表其中的物件總是某個集合加上某個結構。例如*群*總是一個集合加上一個運算，因此 $\mathbf{Grp}$ 是 concrete 的。同樣地，$\mathbf{Top}$ 也是 concrete 的。

Group as a category, monoid as a category 就暫時不當它是 concrete 的。

有時候，concrete category 用來指稱「能夠嵌入到 $\mathbf{Set}$」的範疇。 -->

## The Hom Functor

Hom functor 是數學上常見的 functor，用來製造 dual space 或是 cohomology 等結構。

### Hom functor

給定一個 locally small category $\mathcal C$ 與 $A\in\operatorname{Ob}\mathcal (C)$，我們可以構造 $\operatorname{Hom}(A,-)$ 以及 $\operatorname{Hom}(-,A)$ 兩個 functor，前者是協變的，後者是反變的。

$\operatorname{Hom}(A,-):\mathcal C\to\mathbf{Set}$ 這個協變函子會將範疇 $\mathcal C$ 中的任何物件 $B$ 送到 $\operatorname{Hom}(A,B)$ 這個集合，也就是 $$\{f:\textrm{morphism from }A \textrm{ to } B\}$$ 這個集合

?

並且將 $\mathcal C$ 中的箭頭 $f:B\to C$ 變成函數 「$f\circ -$」。這個函數將每個 $\operatorname{Hom}(A,B)$ 內的箭頭的都接上 $f$，形成一個 $A$ 到 $C$ 的箭頭。

？

另外一個 $\operatorname{Hom}(-,A):\mathcal C\to\mathbf{Set}$ 則是反變的，其將範疇 $\mathcal C$ 中的任何物件 $B$ 送到 $\operatorname{Hom}(B,A)$ 這個集合
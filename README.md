# davidhu3141.github.io

David Hu 的個人網站與文章封存，使用 GitHub Pages 原生支援的 Jekyll 建置。

## 本機預覽

需要 Ruby、Bundler，以及與 GitHub Pages 相容的 gems：

```bash
bundle install
bundle exec jekyll serve --livereload
```

開啟 `http://127.0.0.1:4000`。產生的 `_site/` 不納入版本控制。

## 結構

- `_posts/`：文章 Markdown；既有 permalink 保持不變。
- `_layouts/`、`_includes/`：共用頁面結構。
- `css/main.scss`：全站樣式。
- `independentPages/`：保留的舊互動實驗。

數學公式使用 MathJax 4。舊文章的 v2-style `script[type="math/tex"]` 由官方建議的相容 render action 處理，因此不需要再執行文字前處理腳本。

cp _editing_md/* _posts/

perl -pi -e 's|\$\$(.+?)\$\$|<script type="math\/tex; mode=display">\1</script>|g' _posts/*
perl -pi -e 's|(^[\#\.\>0-9 \-\[\]]*?)\$(.+?)\$|\1 <script type="math\/tex">\2</script>|u' _posts/*
perl -pi -e 's|\$(.+?)\$|<script type="math\/tex">\1</script>|g' _posts/*

perl -pi -e 's|```|~~~ |g' _posts/*
#perl -pi -e 's|(```$)|</code></pre>|g' _posts/*


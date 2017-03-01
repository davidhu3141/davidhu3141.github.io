perl -pi -e 's|\$\$(.+?)\$\$|<script type="math\/tex; mode=display">\1</script>|g' _posts/*
perl -pi -e 's|\$(.+?)\$|<script type="math\/tex">\1</script>|g' _posts/*

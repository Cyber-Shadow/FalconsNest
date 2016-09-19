var gulp = require("gulp");
var coffee = require("gulp-coffee");
var concat = require("gulp-concat");
var inject = require("gulp-inject-string");
var rename = require("gulp-rename");

gulp.task("coffee", function() {
  gulp.src("./webapp/static/webapp/coffee/*.coffee")
    .pipe(concat("orderscript.html"))
    .pipe(coffee({bare: true}))
    .pipe(inject.prepend("<html>\n\n<head>\n  " +
                         "<script type='text/javascript' src='https://code.jquery.com/jquery-3.1.0.min.js'></script>\n" +
                         "</head>\n\n<body>\n\n<script>\n" + 
                         "var menulist = [\n  {% for order in menulist %}\n    " +
                         "['{{ order.name }}', {{ order.price }}, 0],\n  {% endfor %}\n];\n"))
    .pipe(inject.append("</script>\n\n</body>\n</html>"))
    .pipe(rename(function(path) {
      path.extname = ".html";
    }))
    .pipe(gulp.dest("webapp/templates/webapp"));
});

gulp.task("watch-coffee", function() {
  gulp.watch(["./webapp/static/webapp/coffee/*.coffee"], ["coffee"]);
});

var gulp = require("gulp");
var coffee = require("gulp-coffee");

gulp.task("coffee", function() {
  gulp.src("./webapp/static/webapp/coffee/*.coffee")
    .pipe(coffee({bare: true}))
    .pipe(gulp.dest("webapp/static/webapp/js/project"))
});

gulp.task("watch-coffee", function() {
  gulp.watch(["./webapp/static/webapp/coffee/*.coffee"], ["coffee"]);
});

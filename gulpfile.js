var gulp = require("gulp");
var coffee = require("gulp-coffee");
var concat = require("gulp-concat");
var uglify = require("gulp-uglify");

gulp.task("coffee", function() {
  gulp.src("./webapp/static/webapp/coffee/*.coffee")
    .pipe(concat("menusearch.js"))
    .pipe(coffee({bare: true}))
    .pipe(uglify({beautify: true}))
    .pipe(gulp.dest("webapp/static/webapp/js/project"));
});

gulp.task("watch-coffee", function() {
  gulp.watch(["./webapp/static/webapp/coffee/*.coffee"], ["coffee"]);
});

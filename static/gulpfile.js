'use strict';


var gulp = require('gulp'),
	sass = require('gulp-sass'),
  concat = require('gulp-concat'),
  uglify = require('gulp-uglify'),
  rename = require('gulp-rename'),
  	maps = require('gulp-sourcemaps'),
  	 del = require('del');


var paths = {
	scripts: [],
	sytles: [],
	images: [],
};


gulp.task('concatScripts', function() {
	return gulp.src(paths.scripts)
		.pipe(maps.init())
		.pipe(concat('app.js'))
		.pipe(maps.write('./'))
		.pipe(gulp.dest('js'));
});

gulp.task('minifyScripts', function() {
	return gulp.src('js/app.js')
		.pipe(uglify())
		.pipe(rename('app.min.js'))
		.pipe(gulp.dest('js'));
});

gulp.task('compileSass', function(){
	return gulp.src('scss/app.scss')
		.pipe(maps.init())
		.pipe(sass())
		.pipe(maps.write('./'))
		.pipe(gulp.dest('css'));
});

gulp.task('watch', function() {
	gulp.watch('scss/**/*.scss', ['compileSass']);
	gulp.watch('js/**/*.js', ['minifyScripts']);
});

gulp.task('build', ['minifyScripts', 'compileSass']);

gulp.task('serve', ['minifyScripts', 'compileSass', 'watch']);

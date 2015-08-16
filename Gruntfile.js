module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
      styl: {
        files: ['mozart/static/app/styl/*.styl'],
        tasks: ['compileStylus']
      },
      js: {
        files: ['Gruntfile.js', 'mozart/static/app/js/app.js', 'mozart/static/app/js/*/*.js'],
        tasks: ['compileJavascript']
      }
    },
    stylus: {
      options: {
        use : [
          function(){
            return require('autoprefixer-stylus')('last 2 versions', 'ie 8');
          }
        ]
      },
      compile: {
        files: {
          'dist/css/styles.min.css': 'mozart/static/app/styl/main.styl'
        }
      }
    },
    jshint: {
      all: ['Gruntfile.js', 'mozart/static/app/js/app.js', 'mozart/static/app/js/*/*.js']
    },
    concat: {
      options: {
        separator: ''
      },
      basic: {
        src: ['mozart/static/app/js/app.js', 'mozart/static/app/js/*/*.js'],
        dest: 'mozart/static/dist/js/<%= pkg.name %>.js'
      }
    },
    bower_concat: {
      all: {
        dest: 'mozart/static/dist/js/bower.js',
        dependencies: {
          'underscore': 'jquery'
        }
      }
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      dist: {
        files: {
          'mozart/static/dist/js/<%= pkg.name %>.min.js': ['<%= concat.basic.dest %>'],
          'mozart/static/dist/js/bower.min.js': ['<%= bower_concat.all.dest %>']
        }
      }
    },
    copy: {
      foo : {
        files : [
          {
            expand : true,
            dest   : 'mozart/static/dist/img',
            cwd    : 'mozart/static/app/img',
            src    : [
              '**/*'
            ]
          },
          {
            expand : true,
            dest   : 'mozart/static/dist/fonts',
            cwd    : 'mozart/static/app/fonts',
            src    : [
              '**/*'
            ]
          },
          {
            src: 'mozart/static/app/favicon.ico',
            dest: 'mozart/static/dist/favicon.ico'
          }
        ]
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-stylus');
  grunt.loadNpmTasks('grunt-bower-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.registerTask('default', ['stylus', 'jshint', 'concat','bower_concat','uglify','copy', 'watch']);
  grunt.registerTask('compileStylus', ['stylus']);
  grunt.registerTask('compileJavascript', ['jshint', 'concat', 'uglify']);
};

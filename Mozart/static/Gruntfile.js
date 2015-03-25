module.exports = function(grunt) {  
  grunt.initConfig({  
    pkg: grunt.file.readJSON('package.json'),  
    watch: {
      styl: {
        files: ['app/styl/*.styl'],
        tasks: ['compileStylus']
      },
      js: {
        files: ['app/js/app.js', 'app/js/*/*.js'],
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
          'dist/css/styles.min.css': 'app/styl/main.styl'
        }
      }
    },
    concat: {   
      options: {
        separator: ''  
      },
      basic: {
        src: ['app/js/app.js', 'app/js/*/*.js'],  
        dest: 'dist/js/<%= pkg.name %>.js'  
      }
    },
    bower_concat: {
      all: {
        dest: 'dist/js/bower.js',
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
          'dist/js/<%= pkg.name %>.min.js': ['<%= concat.basic.dest %>'],
          'dist/js/bower.min.js': ['<%= bower_concat.all.dest %>']
        }
      }
    },
    copy: {
      foo : {
        files : [
          {
            expand : true,
            dest   : 'dist/img',
            cwd    : 'app/img',
            src    : [
              '**/*'
            ]
          },
          {
            expand : true,
            dest   : 'dist/fonts',
            cwd    : 'app/fonts',
            src    : [
              '**/*'
            ]
          },
          {
            src: 'app/favicon.ico',
            dest: 'dist/favicon.ico'
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
  grunt.registerTask('default', ['stylus', 'concat','bower_concat','uglify','copy', 'watch']);
  grunt.registerTask('compileStylus', ['stylus']);
  grunt.registerTask('compileJavascript', ['concat', 'uglify']);
};
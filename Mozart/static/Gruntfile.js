module.exports = function(grunt) {  
  grunt.initConfig({  
    pkg: grunt.file.readJSON('package.json'),  
    stylus: {
      compile: {
        options: {
          compress: false
        },
        files: {
          'app/css/styles.css': 'app/styl/main.styl'
        }
      }
    },
    autoprefixer: {
      dist: {
        files: {
          'app/css/styles-WAP.css': 'app/css/styles.css'
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
    cssmin: {
      target: {
        files: {
          'dist/css/styles.min.css': ['app/css/styles-WAP.css']
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
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-autoprefixer');
  grunt.registerTask('default', ['stylus', 'autoprefixer', 'concat','bower_concat','uglify', 'cssmin','copy']);
  grunt.registerTask('onlyConcat', ['concat']);
};
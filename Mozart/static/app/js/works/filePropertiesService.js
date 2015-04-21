(function() {
  'use strict';

  function filePropertiesService() {
    this.getExtension = function(file){
      var divisions = file.name.split('.');
      var fileExtension = divisions[divisions.length -1];
      return fileExtension.toLowerCase();
    };
    this.validateFormat = function(fileExtension){
      var validFormats = ['pdf', 'mp3', 'aac', 'wma', 'mp4', 'mpeg', 'avi', '3gp'];
      for(var i = 0; i < validFormats.length; i++){
        if(fileExtension == validFormats[i]){
          return true;
        }
      }
      return false;
    };
    this.isAnImage = function(fileExtension){
      var imageFormats = ['png', 'gif', 'jpg', 'jpeg', 'bmp', 'tiff'];
      for(var i = 0; i < imageFormats.length; i++){
        if(fileExtension == imageFormats[i]){
          return true;
        }
      }
      return false;
    };
    this.isAVideo = function(fileExtension){
      videoFormats = ['mp4', 'mpeg', 'avi', '3gp'];
      for(var i = 0; i < videoFormats.length; i++){
        if(fileExtension == videoFormats[i]){
          return true;
        }
      }
      return false;
    };
    this.getFileSize = function(file){
      var fileSize = file.size/1024;
      return fileSize.toFixed(1);
    };
  }

  angular.module('mozArtApp')
    .service('fileProperties', filePropertiesService);
})();
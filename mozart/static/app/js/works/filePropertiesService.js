(function () {
    'use strict';

    function filePropertiesService() {
        /* jshint validthis:true */
        this.getExtension = function (file) {
            var divisions, fileExtension;
            divisions = file.name.split('.');
            fileExtension = divisions[divisions.length - 1];
            return fileExtension.toLowerCase();
        };
        this.validateFormat = function (fileExtension) {
            // var validFormats = ['pdf', 'mp3', 'aac', 'wma', 'mp4', 'mpeg', 'avi', '3gp'];  Future valid formats
            var validFormats, i;
            validFormats = ['mp3'];
            for (i = 0; i < validFormats.length; i += 1) {
                if (fileExtension === validFormats[i]) {
                    return true;
                }
            }
            return false;
        };
        this.isAnImage = function (fileExtension) {
            var imageFormats, i;
            imageFormats = ['png', 'jpg', 'jpeg'];
            for (i = 0; i < imageFormats.length; i += 1) {
                if (fileExtension === imageFormats[i]) {
                    return true;
                }
            }
            return false;
        };
        this.isAVideo = function (fileExtension) {
            var videoFormats, i;
            videoFormats = ['mp4', 'mpeg', 'avi', '3gp'];
            for (i = 0; i < videoFormats.length; i += 1) {
                if (fileExtension === videoFormats[i]) {
                    return true;
                }
            }
            return false;
        };
        this.getFileSize = function (file) {
            var fileSize = file.size / 1024;
            return fileSize.toFixed(1);
        };
    }

    angular.module('mozArtApp')
        .service('fileProperties', filePropertiesService);
}());
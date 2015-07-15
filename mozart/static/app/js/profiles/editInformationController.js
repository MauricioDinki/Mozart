(function() {
  'use strict';

  function editInformationController($scope, fileProperties){
    var validVideo = true;
    var validCover = true;
    var validImage = true;

    function onVideoFile(event, args) {
      $scope.$apply(function () { 
        $scope.video = args.file;
        var fileFormat = fileProperties.getExtension($scope.video);
        validVideo = fileProperties.isAnImage(fileFormat);
      });
    }
    function onCoverFile(event, args) {
      $scope.$apply(function () { 
        $scope.cover = args.file;
        var fileFormat = fileProperties.getExtension($scope.cover);
        validCover = fileProperties.isAnImage(fileFormat);
      });
    }
    function onProfilePictureFile(event, args) {
      $scope.$apply(function () { 
        $scope.image = args.file;
        var fileFormat = fileProperties.getExtension($scope.image);
        validImage = fileProperties.isAnImage(fileFormat);
      });
    }

    $scope.video = {
      name: ''
    };
    $scope.cover = {
      name: ''
    };
    $scope.image = {
      name: ''
    };
    $scope.showText = function(){
      return $scope.image.name !== '';
    };
    $scope.showMessage = function(){
      return !(validImage || $scope.image.name === '');
    };
    $scope.$on('videoFile', onVideoFile);
    $scope.$on('coverFile', onCoverFile);
    $scope.$on('profilePicture', onProfilePictureFile);

    $scope.validate = function(){
      return !(!validImage || !validVideo || !validCover || $scope.informationform.$invalid);
    };
  }

  editInformationController.$inject = ['$scope', 'fileProperties'];

  angular.module('mozArtApp')
    .controller('editInformationCtrl', editInformationController);
})();
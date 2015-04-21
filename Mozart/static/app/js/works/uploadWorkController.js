(function() {
  'use strict';

  function uploadWorkController($scope, fileProperties){
    var workIsAnImage = true;
    var workFileIsValid = false;
    var workCoverIsValid = false;

    function onArchiveFunction() {
      $scope.workFile = args.file;
      var fileFormat = fileProperties.getExtension($scope.workFile);
      workIsAnImage = fileProperties.isAnImage(fileFormat);
      if(workIsAnImage){
        workFileIsValid = true;
        workCoverIsValid = true;
      }
      else{
        workFileIsValid = fileProperties.validateFormat(fileFormat);
        workCoverIsValid = false;
      }
    }

    function onCoverFunction() {
      $scope.workCover = args.file;
      var fileFormat = fileProperties.getExtension($scope.workCover);
      workCoverIsValid = fileProperties.isAnImage(fileFormat);
    }

    $scope.workFile = {
      name:''
    };
    $scope.workCover = {
      name:''
    };

    $scope.showText1 = function(){
      return $scope.workFile.name !== '';
    };
    $scope.showText2 = function(){
      return $scope.workCover.name !== '';
    };
    $scope.showMessage1 = function(){
      return !(workFileIsValid || $scope.workFile.name === '');
    };
    $scope.showMessage2 = function(){
      return !(workCoverIsValid || $scope.workCover.name === '');
    };
    $scope.showButton2 = function(){
      return !(workIsAnImage || !workFileIsValid);
    };

    $scope.$on('archive', function (event, args) {
      $scope.$apply(onArchiveFunction);
    });

    $scope.$on('cover', function (event, args) {
      $scope.$apply(onCoverFunction);
    });

    $scope.validate = function(){
      return !(!workFileIsValid || !workCoverIsValid || $scope.workform.title.$invalid || $scope.workform.description.$invalid || $scope.workform.category.$invalid);
    };
  }

  uploadWorkController.$inject = ['$scope', 'fileProperties'];

  angular.module('mozArtApp')
    .controller('uploadWorkCtrl', uploadWorkController);
})();
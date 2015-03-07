'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:uploadWorkCtrl
 * @description
 * # uploadWorkCtrl
 * Controller of the mozArtApp
 */

app.controller('uploadWorkCtrl', ['$scope', 'fileProperties', function($scope, fileProperties){
  $scope.workFile = {
    name:''
  };
  $scope.workCover = {
    name:''
  };

  var workIsAnImage = true;
  var workFileIsValid = false;
  var workCoverIsValid = false;

  $scope.showText1 = function(){
    return $scope.workFile.name != '';
  };
  $scope.showText2 = function(){
    return $scope.workCover.name != '';
  };
  $scope.showMessage1 = function(){
    return !(workFileIsValid || $scope.workFile.name == '');
  };
  $scope.showMessage2 = function(){
    return !(workCoverIsValid || $scope.workCover.name == '');
  };
  $scope.showButton2 = function(){
    return !(workIsAnImage || !workFileIsValid);
  };

  $scope.$on('archive', function (event, args) {
    $scope.$apply(function () {
      $scope.workFile = args.file;
      var formato = fileProperties.getExtension($scope.workFile);
      workIsAnImage = fileProperties.isAnImage(formato);
      if(workIsAnImage){
        workFileIsValid = true;
        workCoverIsValid = true;
      }
      else{
        workFileIsValid = fileProperties.validateFormat(formato);
        workCoverIsValid = false;
      }
    });
  });

  $scope.$on('cover', function (event, args) {
    $scope.$apply(function () {
      $scope.workCover = args.file;
      var formato = fileProperties.getExtension($scope.workCover);
      workCoverIsValid = fileProperties.isAnImage(formato);
    });
  });

  $scope.validate = function(){
    return !(!workFileIsValid || !workCoverIsValid || $scope.workform.title.$invalid || $scope.workform.description.$invalid || $scope.workform.category.$invalid);
  };
}]);

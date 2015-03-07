'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:menuCtrl
 * @description
 * # menuCtrl
 * Controller of the mozArtApp
 */
app.controller('menuCtrl', ['$scope', function($scope){
  $scope.visible = false;
  $scope.buttonText = 'Mostrar';
  $scope.menuClass = 'hide-menu';
  $scope.showMenu= function(){
    if($scope.visible == true){
      $scope.menuClass = 'hide-menu';
      $scope.buttonText = 'Mostrar';
      $scope.visible = false;
    }
    else{
      $scope.menuClass = 'show-menu';
      $scope.buttonText = 'Ocultar';
      $scope.visible = true;
    }
  };
}]);

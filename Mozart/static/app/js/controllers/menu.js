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
  $scope.textoMenu = 'Mostrar';
  $scope.menuClass = 'menuoculto';
  $scope.mostrarMenu= function(){
    if($scope.visible == true){
      $scope.menuClass = 'menuoculto';
      $scope.textoMenu = 'Mostrar';
      $scope.visible = false;
    }
    else{
      $scope.menuClass = 'menuvisible';
      $scope.textoMenu = 'Ocultar';
      $scope.visible = true;
    }
  };
}]);

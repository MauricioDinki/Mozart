'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:menuIzquierdoCtrl
 * @description
 * # menuIzquierdoCtrl
 * Controller of the mozArtApp
 */

app.controller('menuIzquierdoCtrl', ['$scope', function($scope){
  $scope.visible = false;
  $scope.posicion1 = {
    'left' : '-305px'
  };
  $scope.posicion2 = {
    'left' : '0'
  };
  $scope.posicionIzquierda = $scope.posicion1;
  $scope.mostrarMenu= function(){
    if($scope.visible == true){
      $scope.posicionIzquierda = $scope.posicion1;
      $scope.visible = false;
    }
    else{
      $scope.posicionIzquierda = $scope.posicion2
      $scope.visible = true;
    }
  };
}]);

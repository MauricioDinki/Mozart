'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:cargarObrasCtrl
 * @description
 * # cargarObrasCtrl
 * Controller of the mozArtApp
 */

app.controller('cargarObrasCtrl', ['$scope','recentWorks', function($scope, recentWorks){
  $scope.cantidad = 6;
  $scope.mostrarMensaje = false;
  $scope.cargar = function(){
    recentWorks.get(
      function(obras) {
        $scope.obras = obras;
        var size = angular.fromJson($scope.obras).length;
        if(size < $scope.cantidad){
          if($scope.cantidad == 6){
            $scope.mostrarMensaje = false;
          }
          else{
            $scope.mostrarMensaje = true;
          }
          $scope.cantidad = size + 6;
        }
        else{
          $scope.mostrarMensaje = false;
          $scope.cantidad += 6;
        }
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      $scope.categoria,
      $scope.autor,
      $scope.cantidad
    );
  };
  $scope.cargar();
}]);
'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:cargarObrasCtrl
 * @description
 * # cargarObrasCtrl
 * Controller of the mozArtApp
 */

//Falta opcion de mostrar mensajes
app.controller('cargarObrasCtrl', ['$scope','peticionObras', function($scope, peticionObras){
  $scope.cantidad = 20;
  $scope.mostrarMensaje = false;
  $scope.cargar = function(nuevaCantidad){
    peticionObras.get(
      function(obras) {
        $scope.obras = obras;
        var size = angular.fromJson($scope.obras).length;
        if(size < $scope.cantidad){
          $scope.mostrarMensaje = true;
          $scope.cantidad = size + 20;
        }
        else{
          $scope.mostrarMensaje = false;
          $scope.cantidad += 20;
        }
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      'recientes',
      $scope.categoria,
      'todos',
      nuevaCantidad
    );
  };
  $scope.cargar($scope.cantidad);
}]);

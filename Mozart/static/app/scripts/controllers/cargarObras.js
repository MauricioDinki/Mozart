'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:cargarObrasCtrl
 * @description
 * # cargarObrasCtrl
 * Controller of the mozArtApp
 */

//Falta opcion de mostrar mensajes
app.controller('cargarObrasCtrl', ['$scope', '$routeParams', 'peticionObras', function($scope, $routeParams, peticionObras){
  $scope.cantidad = 5;
  $scope.categoria = $routeParams.categoria;
  $scope.cargar = function(nuevaCantidad){
    peticionObras.get(
      function(obras) {
        $scope.obras = obras;
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      'recientes',
      $scope.categoria,
      'todos',
      nuevaCantidad
    );
    $scope.cantidad += 4;
  };
  $scope.cargar($scope.cantidad);
  $scope.prueba = 'http://www.google.com';
}]);

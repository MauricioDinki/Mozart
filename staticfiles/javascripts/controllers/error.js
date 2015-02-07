'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:errorCtrl
 * @description
 * # errorCtrl
 * Controller of the mozArtApp
 */

app.controller('errorCtrl', ['$scope', '$routeParams', 'peticionObras', function($scope, $routeParams, peticionObras){
  $scope.cantidad = 3;
  $scope.cargar = function(){
    peticionObras.get(
      function(obras) {
        $scope.obras = obras;
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      'aleatorio',
      'todas',
      'todos',
      $scope.cantidad
    );
  };
  $scope.cargar();
}]);

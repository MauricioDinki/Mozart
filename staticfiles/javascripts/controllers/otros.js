'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:otros
 * @description
 * # otros
 * Controller of the mozArtApp
 */

//Este controlador aun no esta escrito
app.controller('perfilArtistaCtrl', ['$scope', '$log', function($scope, $log){
  $log.log('Hola');
}]);

//Este controlador aun no esta escrito
app.controller('perfilPromotorCtrl', ['$scope', '$log', function($scope, $log){
  $log.log('Hola');
}]);

//Este controlador aun no esta escrito
app.controller('informacionPerfilCtrl', ['$scope', '$log', function($scope, $log){
  $log.log('Hola');
}]);

//Este controlador aun no esta escrito
app.controller('configuracionesCtrl', ['$scope', function($scope){
  $scope.validar = function(){
    alert('Hola ' + $scope.email + '!');
  };
}]);

//Este controlador aun no esta escrito, es necesario agregar funciones para login con vinculacion
app.controller('loginCtrl', ['$scope', function($scope){
  $scope.validar = function(){
    alert('Hola ' + $scope.email + '!');
  };
}]);

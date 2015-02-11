'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:formularioRegistroCtrl
 * @description
 * # formularioRegistroCtrl
 * Controller of the mozArtApp
 */
//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('formularioRegistroCtrl', ['$scope', 'validateAge', function($scope, validateAge){
  $scope.acepto = false;
  $scope.fechaValida = true;
  $scope.mensaje = true;
  var month = 1;
  $scope.validarFecha = function(){
    $scope.mensaje = validateAge.validDate($scope.signup.day_of_birth, $scope.signup.month_of_birth, $scope.signup.year_of_birth);
    $scope.fechaValida = ($scope.mensaje === 'Ok');
  };
  $scope.validar = function(){
    return !(!$scope.fechaValida || $scope.signupform.$invalid);
  };
}]);

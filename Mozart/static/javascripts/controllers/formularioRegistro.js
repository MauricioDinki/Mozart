'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:formularioRegistroCtrl
 * @description
 * # formularioRegistroCtrl
 * Controller of the mozArtApp
 */
//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('formularioRegistroCtrl', ['$scope', function($scope){
  $scope.acepto = false;
  $scope.fechaValida = true;
  $scope.mayorEdad = true;
  $scope.nicknameValido = true;
  $scope.nicknamePrueba = 'holi crayholi';
  $scope.emailValido = true;
  $scope.emailPrueba = 'aaa@aaa.com';
  $scope.fecha_actual = new Date();
  $scope.this_year = parseInt($scope.fecha_actual.getYear()) + 1900;
  $scope.validarFecha = function(){
    var date = new Date($scope.year,$scope.mes, '0');
    var this_month = parseInt($scope.fecha_actual.getMonth() + 1);
    var this_day = parseInt($scope.fecha_actual.getDate());
    var resta_fechas = $scope.this_year - $scope.year;
    if(($scope.dia-0)>(date.getDate()-0)){
      $scope.fechaValida = false;
    }
    else{
      $scope.fechaValida = true;
    }
    if(this_month < $scope.mes){
      resta_fechas--;
    }
    if(($scope.mes == this_month) && (this_day < $scope.dia)){
      resta_fechas--;
    }
    if(resta_fechas > 1900){
      resta_fechas -= 1900;
    }
    if(resta_fechas >= 18){
      $scope.mayorEdad = true;
    }
    else{
      $scope.mayorEdad = false;
    }
  };
  $scope.verificarNickname = function(){
    if($scope.nickname == $scope.nicknamePrueba){
      $scope.nicknameValido = false;
    }
    else{
      $scope.nicknameValido = true;
    }
  };
  $scope.verificarEmail = function(){
    if($scope.email == $scope.emailPrueba){
      $scope.emailValido = false;
    }
    else{
      $scope.emailValido = true;
    }
  };
  $scope.validar = function(){
    return !(!$scope.fechaValida || !$scope.mayorEdad || !$scope.emailValido || !$scope.nicknameValido || $scope.registro.$invalid);
  };
}]);

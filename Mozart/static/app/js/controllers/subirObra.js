'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:subirObraCtrl
 * @description
 * # subirObraCtrl
 * Controller of the mozArtApp
 */

app.controller('subirObraCtrl', ['$scope', 'validateFile', function($scope, validateFile){
  $scope.maxeti = 30;
  $scope.archivo = {
    name: ''
  };
  $scope.portada = {
    name: ''
  };

  var archivoImagen = true;
  var archivoValido = false;
  var portadaValida = false;

  $scope.mostrarTexto1 = function(){
    return $scope.archivo.name != '';
  };
  $scope.mostrarTexto2 = function(){
    return $scope.portada.name != '';
  };
  $scope.mostrarMensaje1 = function(){
    return !(archivoValido || $scope.archivo.name == '');
  };
  $scope.mostrarMensaje2 = function(){
    return !(portadaValida || $scope.portada.name == '');
  };
  $scope.mostrarBoton2 = function(){
    return !(archivoImagen || !archivoValido);
  };

  $scope.$on('archive', function (event, args) {
    $scope.$apply(function () {
      $scope.archivo = args.file;
      var formato = validateFile.getExtension($scope.archivo);
      archivoImagen = validateFile.isAnImage(formato);
      if(archivoImagen){
        archivoValido = true;
        portadaValida = true;
      }
      else{
        archivoValido = validateFile.validateFormat(formato);
        portadaValida = false;
      }
    });
  });
  $scope.$on('cover', function (event, args) {
    $scope.$apply(function () {
      $scope.portada = args.file;
      var formato = validateFile.getExtension($scope.portada);
      portadaValida = validateFile.isAnImage(formato);
    });
  });
  $scope.validar = function(){
    return !(!archivoValido || !portadaValida || $scope.workform.$invalid);
  };
}]);

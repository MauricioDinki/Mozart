'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:subirObraCtrl
 * @description
 * # subirObraCtrl
 * Controller of the mozArtApp
 */

app.controller('subirObraCtrl', ['$scope', 'fileService', function($scope, fileService){
  $scope.maxeti = 30;
  $scope.archivo = {
    name:''
  };
  $scope.portada = {
    name:''
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
      var formato = fileService.getExtension($scope.archivo);
      archivoImagen = fileService.isAnImage(formato);
      if(archivoImagen){
        archivoValido = true;
        portadaValida = true;
      }
      else{
        archivoValido = fileService.validateFormat(formato);
        portadaValida = false;
      }
    });
  });
  $scope.$on('cover', function (event, args) {
    $scope.$apply(function () {
      $scope.portada = args.file;
      var formato = fileService.getExtension($scope.portada);
      portadaValida = fileService.isAnImage(formato);
    });
  });
  $scope.validar = function(){
    return !(!archivoValido || !portadaValida || $scope.workform.title.$invalid || $scope.workform.description.$invalid || $scope.workform.category.$invalid);
  };
}]);

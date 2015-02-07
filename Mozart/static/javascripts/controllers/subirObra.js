'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:subirObraCtrl
 * @description
 * # subirObraCtrl
 * Controller of the mozArtApp
 */

//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('subirObraCtrl', ['$scope', function($scope){
  $scope.maxeti = 30;
  $scope.archivo = {
    name: ''
  };
  $scope.portada = {
    name: ''
  };
  $scope.formatoArchivo = '';
  $scope.formatoPortada = '';
  $scope.archivoImagen = true;
  $scope.archivoValido = false;
  $scope.portadaValida = false;

  $scope.$on('archivoPrincipal', function (event, args) {
    $scope.$apply(function () {
      $scope.archivo = args.file;
      divisiones = $scope.archivo.name.split('.');
      $scope.formatoArchivo = divisiones[divisiones.length - 1];
      $scope.archivoValido = $scope.verificarFormato();
    });
  });
  $scope.$on('archivoPortada', function (event, args) {
    $scope.$apply(function () {
      $scope.portada = args.file;
      divisiones = $scope.portada.name.split('.');
      $scope.formatoPortada = divisiones[divisiones.length - 1];
      $scope.portadaValida = $scope.verificarImagen($scope.formatoPortada);
    });
  });
  $scope.verificarFormato = function(){
    otrosFormatos = ['pdf', 'mp3', 'aac', 'wma', 'mp4', 'mpeg', 'avi', '3gp'];
    $scope.archivoImagen = $scope.verificarImagen($scope.formatoArchivo);
    if($scope.archivoImagen == true){
      $scope.portadaValida = true;
      return true;
    }
    else{
      $scope.portadaValida = $scope.verificarImagen($scope.formatoPortada);
      for(i = 0; i < otrosFormatos.length; i++){
        if($scope.formatoArchivo == otrosFormatos[i]){
          return true;
        }
      }
    }
    return false;
  };
  $scope.verificarImagen = function(formato){
    formatosImagen = ['png', 'gif', 'jpg', 'jpeg', 'bmp', 'tiff'];
    for(i = 0; i < formatosImagen.length; i++){
      if(formato == formatosImagen[i]){
        return true;
      }
    }
    return false;
  };
  $scope.validar = function(){
    return !(!$scope.archivoValido || !$scope.portadaValida || $scope.subirobra.$invalid);
  };
}]);

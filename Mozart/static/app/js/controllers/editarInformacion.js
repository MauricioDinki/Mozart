'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:editarInformacionCtrl
 * @description
 * # editarInformacionCtrl
 * Controller of the mozArtApp
 */

//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('editarInformacionCtrl', ['$scope', function($scope){
  $scope.videoValido = true;
  $scope.portadaValida = true;
  $scope.imagenValida = true;
  $scope.video = {
    name: ''
  };
  $scope.portada = {
    name: ''
  };
  $scope.imagen = {
    name: ''
  };
  $scope.$on('archivoVideo', function (event, args) {
    $scope.$apply(function () { //add the file object to the scope's files collection
      $scope.video = args.file;
      divisiones = $scope.video.name.split('.');
      $scope.formatoVideo = divisiones[divisiones.length - 1];
      $scope.videoValido = $scope.verificarVideo($scope.formatoVideo);
    });
  });
  $scope.$on('archivoPortada', function (event, args) {
    $scope.$apply(function () { //add the file object to the scope's files collection
      $scope.portada = args.file;
      divisiones = $scope.portada.name.split('.');
      $scope.formatoPortada = divisiones[divisiones.length - 1];
      $scope.portadaValida = $scope.verificarImagen($scope.formatoPortada);
    });
  });
  $scope.$on('archivoImagen', function (event, args) {
    $scope.$apply(function () { //add the file object to the scope's files collection
      $scope.imagen = args.file;
      divisiones = $scope.imagen.name.split('.');
      $scope.formatoImagen = divisiones[divisiones.length - 1];
      $scope.imagenValida = $scope.verificarImagen($scope.formatoImagen);
    });
  });
  $scope.verificarVideo = function(formato){
    formatosVideo = ['mp4', 'mpeg', 'avi', '3gp'];
    for(i = 0; i < formatosVideo.length; i++){
      if(formato == formatosVideo[i]){
        return true;
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
}]);

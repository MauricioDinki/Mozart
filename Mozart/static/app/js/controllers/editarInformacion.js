'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:editarInformacionCtrl
 * @description
 * # editarInformacionCtrl
 * Controller of the mozArtApp
 */

//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('editarInformacionCtrl', ['$scope', 'validateFile', function($scope, validateFile){
  var videoValido = true;
  var portadaValida = true;
  var imagenValida = true;
  $scope.video = {
    name: ''
  };
  $scope.portada = {
    name: ''
  };
  $scope.imagen = {
    name: ''
  };
  $scope.mostrarTexto = function(){
    return $scope.imagen.name != '';
  };
  $scope.mostrarMensaje = function(){
    return !(imagenValida || $scope.imagen.name == '');
  };
  $scope.$on('videoFile', function (event, args) {
    $scope.$apply(function () { 
      $scope.video = args.file;
      var formato = validateFile.getExtension($scope.video);
      videoValido = validateFile.isAnImage(formato);
    });
  });
  $scope.$on('coverFile', function (event, args) {
    $scope.$apply(function () { 
      $scope.portada = args.file;
      var formato = validateFile.getExtension($scope.portada);
      portadaValida = validateFile.isAnImage(formato);
    });
  });
  $scope.$on('profilePicture', function (event, args) {
    $scope.$apply(function () { 
      $scope.imagen = args.file;
      var formato = validateFile.getExtension($scope.imagen);
      imagenValida = validateFile.isAnImage(formato);
    });
  });
  $scope.validar = function(){
    return !(!imagenValida || !videoValido || !portadaValida || $scope.informationform.$invalid);
  };
}]);

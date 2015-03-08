'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:editInformationCtrl
 * @description
 * # editInformationCtrl
 * Controller of the mozArtApp
 */

app.controller('editInformationCtrl', ['$scope', 'fileProperties', function($scope, fileProperties){
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
      var formato = fileProperties.getExtension($scope.video);
      videoValido = fileProperties.isAnImage(formato);
    });
  });
  $scope.$on('coverFile', function (event, args) {
    $scope.$apply(function () { 
      $scope.portada = args.file;
      var formato = fileProperties.getExtension($scope.portada);
      portadaValida = fileProperties.isAnImage(formato);
    });
  });
  $scope.$on('profilePicture', function (event, args) {
    $scope.$apply(function () { 
      $scope.imagen = args.file;
      var formato = fileProperties.getExtension($scope.imagen);
      imagenValida = fileProperties.isAnImage(formato);
    });
  });
  $scope.validar = function(){
    return !(!imagenValida || !videoValido || !portadaValida || $scope.informationform.$invalid);
  };
}]);

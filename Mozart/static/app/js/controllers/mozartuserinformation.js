'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:mozartUserInformation
 * @description
 * # mozartUserInformation
 * Controller of the mozArtApp
 */

app.controller('mozartUserInformationCtrl', ['$scope','mozartUser', 'user','contact','dateOfBirth', function($scope, mozartUser, user,contact,dateOfBirth){
  $scope.cargar = function(){
    mozartUser.get(
      function(usuario) {
        $scope.usuario = usuario[0].user;
        if(usuario[0].profile_picture == null){
          $scope.imagen = '/static/img/default.png'
        }
        else{
          $scope.imagen = usuario[0].profile_picture;
        }
       if(usuario[0].description == null || usuario[0].description == ''){
          $scope.descripcion = 'Sin descripción.'
        }
        else{
          $scope.descripcion = usuario[0].description;
        }
        if(usuario[0].sex == null){
          $scope.sexo = 'No disponible.'
        }
        else{
          $scope.sexo = usuario[0].sex;
        }
        $scope.cpais =  usuario[0].nationality;
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      $scope.usuario
    );
    user.get(
      function(usuario) {
        var arr = usuario[0].date_joined.split('T');
        $scope.fechamozart = arr[0];
        var nombres = usuario[0].first_name;
        var apellidos = usuario[0].last_name;
        if(nombres == '' || apellidos == '' ){
          $scope.nombrecompleto = 'No disponible.';
        }
        else{
          $scope.nombrecompleto = nombres + ' ' + apellidos;
        }
        $scope.email =  usuario[0].email;
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      $scope.usuario
    );
    contact.get(
      function(usuario) {
        if(usuario[0].phone_number == null){
          $scope.telefono = 'No disponible.'
        }
        else{
          $scope.telefono = usuario[0].phone_number;
        }
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      $scope.usuario
    );
    dateOfBirth.get(
      function(usuario) {
        $scope.fechanacimiento = usuario[0].day + ' de ' + usuario[0].month + ' de ' + usuario[0].year;
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      $scope.usuario
    );
  };
  $scope.cargar();
}]);
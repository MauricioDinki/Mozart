'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:mozartUserInformation
 * @description
 * # mozartUserInformation
 * Controller of the mozArtApp
 */

app.controller('mozartUserInformationCtrl', ['$scope','userInformation', function($scope, userInformation){
  $scope.cargar = function(){
    userInformation.get(
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
      $scope.usuario,
      'mozart_user'
    );
    userInformation.get(
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
      $scope.usuario,
      'users'
    );
    userInformation.get(
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
      $scope.usuario,
      'user_contact'
    );
    userInformation.get(
      function(usuario) {
        $scope.fechanacimiento = usuario[0].day + ' de ' + usuario[0].month + ' de ' + usuario[0].year;
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      $scope.usuario,
      'user_dateofbirth'
    );
    userInformation.get(
      function(usuario) {
        console.log(usuario[0]);
        $scope.domicilio = usuario[0].adress + ', ' + usuario[0].neighborhood + ', ' + usuario[0].city + ', ' + usuario[0].zip_code;
        if(usuario[0].adress == '' && usuario[0].city == '' && usuario[0].zip_code == '' && usuario[0].neighborhood == ''){
          $scope.domicilio = 'No disponible.';
        }
        else if(usuario[0].adress == '' || usuario[0].city == '' || usuario[0].zip_code == '' || usuario[0].neighborhood == ''){
          $scope.domicilio += ' (Domicilio incompleto)';
        }
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      $scope.usuario,
      'adress'
    );
  };
  $scope.cargar();
}]);
(function() { 
  'use strict';

  function mozartUserInformationController($scope, $window, userInformation){
    $scope.user = {};
    var mozart_user = {};
    (function(username) {
      userInformation.get(
        function(user) {
          mozart_user.username = user[0].user;
          mozart_user.profile_picture = 
            (user[0].profile_picture !== null) ? user[0].profile_picture : '/static/img/default.png';
          mozart_user.description = 
            (user[0].description !== null || user[0].description === '') ? user[0].description : 'Sin descripción.';
          mozart_user.sex = 
            (user[0].sex !== null) ? user[0].sex : 'No disponible.';
          mozart_user.countryCode =  user[0].nationality;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'mozart_user'
      );
      userInformation.get(
        function(user) {
          var arr = user[0].date_joined.split('T');
          mozart_user.mozArtDate = arr[0];
          var names = user[0].first_name;
          var surnames = user[0].last_name;
          mozart_user.fullname = 
            !(names === '' || surnames === '' ) ? names + ' ' + surnames : 'No disponible.';
          mozart_user.email =  user[0].email;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'users'
      );
      userInformation.get(
        function(user) {
          mozart_user.phoneNumber = 
            (user[0].phone_number !== null) ? user[0].phone_number : 'No disponible.';
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'user_contact'
      );
      userInformation.get(
        function(user) {
          mozart_user.dateOfBirth = user[0].day + ' de ' + user[0].month + ' de ' + user[0].year;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'user_dateofbirth'
      );
      userInformation.get(
        function(user) {
          mozart_user.adress = user[0].adress + ', ' + user[0].neighborhood + ', ' + user[0].city + ', ' + user[0].zip_code;
          if(user[0].adress === '' && user[0].city === '' && user[0].zip_code === '' && user[0].neighborhood === ''){
            mozart_user.adress = 'No disponible.';
          }
          else if(user[0].adress === '' || user[0].city === '' || user[0].zip_code === '' || user[0].neighborhood === ''){
            mozart_user.adress += ' (Domicilio incompleto)';
          }
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        username,
        'adress'
      );
      $scope.user = mozart_user;
    })($scope.base_username);
  }

  mozartUserInformationController.$inject = ['$scope', '$window', 'userInformation'];

  angular.module('mozArtApp')
    .controller('mozartUserInformationCtrl', mozartUserInformationController);
})();
(function() { 
  'use strict';

  function mozartUserInformationController($scope, $window, userInformation){
    (function() {
      userInformation.get(
        function(user) {
          $scope.user = user[0].user;
          $scope.profile_picture = 
            (user[0].profile_picture !== null) ? user[0].profile_picture : '/static/img/default.png';
          $scope.description = 
            (user[0].description !== null || user[0].description === '') ? user[0].description : 'Sin descripción.';
          $scope.sex = 
            (user[0].sex !== null) ? user[0].sex : 'No disponible.';
          $scope.countryCode =  user[0].nationality;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        $scope.user,
        'mozart_user'
      );
      userInformation.get(
        function(user) {
          var arr = user[0].date_joined.split('T');
          $scope.mozArtDate = arr[0];
          var names = user[0].first_name;
          var surnames = user[0].last_name;
          $scope.fullname = 
            !(names === '' || surnames === '' ) ? names + ' ' + surnames : 'No disponible.';
          $scope.email =  user[0].email;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        $scope.user,
        'users'
      );
      userInformation.get(
        function(user) {
          $scope.phoneNumber = 
            (user[0].phone_number !== null) ? user[0].phone_number : 'No disponible.';
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        $scope.user,
        'user_contact'
      );
      userInformation.get(
        function(user) {
          $scope.dateOfBirth = user[0].day + ' de ' + user[0].month + ' de ' + user[0].year;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        $scope.user,
        'user_dateofbirth'
      );
      userInformation.get(
        function(user) {
          $scope.adress = user[0].adress + ', ' + user[0].neighborhood + ', ' + user[0].city + ', ' + user[0].zip_code;
          if(user[0].adress === '' && user[0].city === '' && user[0].zip_code === '' && user[0].neighborhood === ''){
            $scope.adress = 'No disponible.';
          }
          else if(user[0].adress === '' || user[0].city === '' || user[0].zip_code === '' || user[0].neighborhood === ''){
            $scope.adress += ' (Domicilio incompleto)';
          }
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        $scope.user,
        'adress'
      );
    })();
  }

  mozartUserInformationController.$inject = ['$scope', '$window', 'userInformation'];

  angular.module('mozArtApp')
    .controller('mozartUserInformationCtrl', mozartUserInformationController);
})();
(function() {
  'use strict';

  function signupFormController($scope, validateDates) {
    $scope.agree = false;
    $scope.validDate = true;
    $scope.message = '';
    $scope.validateDate = function(){
      $scope.message = validateDates.validDate($scope.signup.day_of_birth, $scope.signup.month_of_birth, $scope.signup.year_of_birth);
      $scope.validDate = ($scope.message === 'Ok');
    };
    $scope.validate = function(){
      return !(!$scope.validDate || $scope.signupform.$invalid);
    };
  }

  signupFormController.$inject = ['$scope', 'validateDates'];

  angular.module('mozArtApp')
    .controller('signupFormCtrl', signupFormController);
})();
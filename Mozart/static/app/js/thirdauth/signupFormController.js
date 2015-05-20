(function() {
  'use strict';

  function signupFormController($scope, validateDates) {
    $scope.agree = false;
    $scope.validDate = true;
    $scope.message = '';
    $scope.dateIsDirty = false;
    $scope.validateDate = function(){
      $scope.message = validateDates.validDate($scope.day_of_birth, $scope.month_of_birth, $scope.year_of_birth, 18);
      $scope.dateIsDirty = ($scope.signupform.day_of_birth.$dirty && $scope.signupform.month_of_birth.$dirty);
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
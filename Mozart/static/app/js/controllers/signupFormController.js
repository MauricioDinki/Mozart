'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:signupFormCtrl
 * @description
 * # signupFormCtrl
 * Controller of the mozArtApp
 */

app.controller('signupFormCtrl', ['$scope', 'validateDates', function($scope, validateDates){
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
}]);

(function() {
  'use strict';

  function searchResultsController($scope, profileUrl){
    $scope.results = {
      showWorks : true,
      showUsers : false,
      works : {},
      users : {},
      aciveOptionText : 'Obras',
      nonAciveOptionText : 'Usuarios',
      aciveOptionClass : 'left-option',
      nonAciveOptionClass : 'right-option'
    };

    $scope.results.alternateResults = function() {
      if($scope.results.showWorks === false) {
        $scope.results.aciveOptionText = 'Obras';
        $scope.results.nonAciveOptionText = 'Usuarios';
        $scope.results.aciveOptionClass = 'left-option';
        $scope.results.nonAciveOptionClass = 'right-option';
      }
      else {
        $scope.results.nonAciveOptionText = 'Obras';
        $scope.results.aciveOptionText = 'Usuarios';
        $scope.results.nonAciveOptionClass = 'left-option';
        $scope.results.aciveOptionClass = 'right-option';
      }
      $scope.results.showWorks = !$scope.results.showWorks;
      $scope.results.showUsers = !$scope.results.showUsers;
    };
  }

  searchResultsController.$inject = ['$scope'];

  angular.module('mozArtApp')
    .controller('searchResultsCtrl', searchResultsController);
})();
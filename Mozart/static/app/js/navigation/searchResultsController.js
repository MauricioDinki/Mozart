(function() {
  'use strict';

  function searchResultsController($scope, profileUrl){
    $scope.results = {
      showWorks : true,
      showUsers : false,
      works : {},
      users : {}
    };

    $scope.results.displayWorks = function() {
      $scope.results.showUsers = false;
      $scope.results.showWorks = true;
    };

    $scope.results.displayUsers = function() {
      $scope.results.showWorks = false;
      $scope.results.showUsers = true;
    };
  }

  searchResultsController.$inject = ['$scope'];

  angular.module('mozArtApp')
    .controller('searchResultsCtrl', searchResultsController);
})();
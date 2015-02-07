'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:modalCtrl
 * @description
 * # modalCtrl
 * Controller of the mozArtApp
 */

app.controller('modalCtrl', ['$scope', function($scope) {
  $scope.modalShown = false;
  $scope.toggleModal = function() {
    $scope.modalShown = !$scope.modalShown;
  };
}]);

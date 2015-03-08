'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:editWorkCtrl
 * @description
 * # editWorkCtrl
 * Controller of the mozArtApp
 */

app.controller('editWorkCtrl', ['$scope', function($scope){
  $scope.validate = function(){
    return $scope.editworkform.$valid;
  };
}]);

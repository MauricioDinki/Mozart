'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:editarObraCtrl
 * @description
 * # editarObraCtrl
 * Controller of the mozArtApp
 */

app.controller('editarObraCtrl', ['$scope', function($scope){
  $scope.validar = function(){
    return $scope.editworkform.$valid;
  };
}]);

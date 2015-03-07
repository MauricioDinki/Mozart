'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:loadWorksCtrl
 * @description
 * # loadWorksCtrl
 * Controller of the mozArtApp
 */

app.controller('loadWorksCtrl', ['$scope','worksRequest', function($scope, worksRequest){
  $scope.worksPaginate = 6;
  $scope.showMessage = false;
  $scope.getWorks = function(){
    worksRequest.recentWorks.get(
      function(works) {
        $scope.works = works;
        var size = angular.fromJson($scope.works).length;
        if(size < $scope.worksPaginate){
          if($scope.worksPaginate == 6){
            $scope.showMessage = false;
          }
          else{
            $scope.showMessage = true;
          }
          $scope.worksPaginate = size + 6;
        }
        else{
          $scope.showMessage = false;
          $scope.worksPaginate += 6;
        }
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      $scope.worksCategory,
      $scope.worksAuthor,
      $scope.worksPaginate
    );
  };
  $scope.getWorks();
}]);
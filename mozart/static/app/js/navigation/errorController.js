(function() {
  'use strict'; 

  function errorController($scope, $window, worksRequest){
    var worksAmount = 3;
    (function() {
      worksRequest.randomWorks.get(
        function(works) {
          $scope.works = works;
        },
        function(data, status) {
          $window.alert('Ha fallado la petición. Estado HTTP:' + status);
        },
        'aleatorio',
        'todas',
        'todos',
        worksAmount
      );
    })();
  }

  errorController.$inject = ['$scope', '$window', 'worksRequest'];

  angular.module('mozArtApp')
    .controller('errorCtrl', errorController);
})();
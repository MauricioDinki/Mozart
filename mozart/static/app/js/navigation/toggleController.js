(function () {
    'use strict';

    function toggleController($scope) {
        $scope.isVisible = false;
        $scope.symbol = '+';
        $scope.toggle = function () {
            if ($scope.isVisible) {
                $scope.symbol = '+';
            } else {
                $scope.symbol = '-';
            }
            $scope.isVisible = !$scope.isVisible;
        };
    }

    toggleController.$inject =  ['$scope'];

    angular.module('mozArtApp')
        .controller('toggleCtrl', toggleController);
}());
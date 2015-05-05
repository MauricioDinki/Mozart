(function() {
	'use strict';

	function toggleController($scope) {
	  $scope.isVisible = false;
	  $scope.toggle = function() {
	    $scope.isVisible = !$scope.isVisible;
		};
	}

	toggleController.$inject =  ['$scope'];

	angular.module('mozArtApp')
		.controller('toggleCtrl', toggleController);
})();
(function() {
	'use strict';

	function modalController($scope) {
	  $scope.modalShown = false;
	  $scope.toggleModal = function() {
	    $scope.modalShown = !$scope.modalShown;
	  };
	}

	modalController.$inject =  ['$scope'];

	angular.module('mozArtApp')
		.controller('modalCtrl', modalController);
})();
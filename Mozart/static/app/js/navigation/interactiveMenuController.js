(function() {
	'use strict';

	function interactiveMenuController($scope) {
		$scope.modalShown = false;
		$scope.toggleModal = function() {
			$scope.modalShown = !$scope.modalShown;
		};
		$scope.interactiveClass = 'mz-modal';
	}

	interactiveMenuController.$inject = ['$scope'];

	angular.module('mozArtApp')
		.controller('interactiveMenuCtrl', interactiveMenuController);
})();
(function() {
	'use strict';

	function editWorkController($scope) {
		$scope.validate = function(){
	    return $scope.editworkform.$valid;
	  };
	}

	editWorkController.$inject = ['$scope'];

	angular.module('mozArtApp')
		.controller('editWorkCtrl', editWorkController);
})();
(function() {
	'use strict';

	function loadWorksController($scope, $window, worksRequest) {
		$scope.showMessage = false;
		$scope.works = [];
		$scope.pageNumber = 1;
		$scope.getWorks = function(){
			worksRequest.recentWorks.get(
				function(works, nextPage) {
					var prevSize = $scope.works.length;
					function workExists(work) {
						return $filter('filter')(
							$scope.works,
							work.slug
						)[0];
					}
					for(var i in works) {
						var isRepeated = worksRequest.checkRepeatedWork($scope.works, works[i]);
						if(!isRepeated) {
							$scope.works.push(works[i]);
						}
					}
					if(nextPage !== null) {
						$scope.pageNumber++;
					}
					$scope.showMessage = (prevSize === $scope.works.length);
				},
				function(data, status) {
					$window.alert('Ha fallado la petición. Estado HTTP:' + status);
				},
				$scope.worksCategory,
				$scope.worksAuthor,
				$scope.pageNumber
			);
		};
		$scope.getWorks();
	}

	loadWorksController.$inject = ['$scope', '$window', 'worksRequest'];

	angular.module('mozArtApp')
		.controller('loadWorksCtrl', loadWorksController);
})();
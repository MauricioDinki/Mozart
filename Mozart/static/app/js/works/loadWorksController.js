(function() {
	'use strict';

	function loadWorksController($scope, $window, worksRequest, workUrl, profileUrl) {
		$scope.showMessage = false;
		$scope.works = [];
		$scope.pageNumber = 1;
		$scope.getWorks = function(){
			worksRequest.recentWorks.get(
				function(works, nextPage) {
					var prevSize = $scope.works.length;
					for(var i in works) {
						var work = works[i];
						var isRepeated = worksRequest.checkRepeatedWork($scope.works, {slug: work.slug});
						if(!isRepeated) {
							work.workUrl = workUrl(work.user, work.slug);
							work.userUrl = profileUrl(work.user);
							$scope.works.push(work);
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

	loadWorksController.$inject = ['$scope', '$window', 'worksRequest', 'workUrl', 'profileUrl'];

	angular.module('mozArtApp')
		.controller('loadWorksCtrl', loadWorksController);
})();
(function() {
	'use strict';

	function loadPromotersController($scope, $window, promotersRequest, profileUrl) {
		$scope.showMessage = false;
		$scope.promoters = [];
		$scope.pageNumber = 1;
		$scope.getUsers = function(){
			promotersRequest.get(
				function(promoters, nextPage) {
					var prevSize = $scope.promoters.length;
					for(var i in promoters) {
						var user = promoters[i];
						var isRepeated = promotersRequest.checkRepeatedUser($scope.promoters, user.slug);
						user.picture = (user.profile_picture !== null) ? user.profile_picture : '/static/img/default.png';
						if(!isRepeated) {
							user.userUrl = profileUrl(user.user);
							$scope.promoters.push(user);
						}
					}
					if(nextPage !== null) {
						$scope.pageNumber++;
					}
					$scope.showMessage = (prevSize === $scope.promoters.length);
				},
				function(data, status) {
					$window.alert('Ha fallado la petición. Estado HTTP:' + status);
				},
				$scope.eventsCreator,
				$scope.pageNumber
			);
		};
		$scope.getUsers();
	}

	loadPromotersController.$inject = ['$scope', '$window', 'promotersRequest', 'profileUrl'];

	angular.module('mozArtApp')
		.controller('loadPromotersCtrl', loadPromotersController);
})();
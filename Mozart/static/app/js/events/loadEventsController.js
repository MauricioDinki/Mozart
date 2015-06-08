(function() {
	'use strict';

	function loadEventsController($scope, $window, eventsRequest, profileUrl) {
		$scope.showMessage = false;
		$scope.events = [];
		$scope.pageNumber = 1;
		$scope.getEvents = function(){
			eventsRequest.get(
				function(events, nextPage) {
					var prevSize = $scope.events.length;
					function eventExists(work) {
						return $filter('filter')(
							$scope.events,
							_event.slug
						)[0];
					}
					for(var i in events) {
						var _event = events[i];
						var isRepeated = eventsRequest.checkRepeatedEvent($scope.events, _event);
						var hasFinished = eventsRequest.checkFinishedEvent(_event);
						if(!isRepeated && !hasFinished) {
							_event.userUrl = profileUrl(_event.user);
							$scope.events.push(_event);
						}
					}
					if(nextPage !== null) {
						$scope.pageNumber++;
					}
					$scope.showMessage = (prevSize === $scope.events.length);
				},
				function(data, status) {
					$window.alert('Ha fallado la petición. Estado HTTP:' + status);
				},
				$scope.eventsCreator,
				$scope.pageNumber
			);
		};
		$scope.getEvents();
	}

	loadEventsController.$inject = ['$scope', '$window', 'eventsRequest', 'profileUrl'];

	angular.module('mozArtApp')
		.controller('loadEventsCtrl', loadEventsController);
})();
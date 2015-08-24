(function () {
    'use strict';

    function loadEventsController($scope, baseController, eventsRequest, profileUrl) {
        function extraFunction(mzEvent) {
            mzEvent.userUrl = profileUrl(mzEvent.user);
            return mzEvent;
        }
        function dateFilterFunction(mzEvent) {
            var eventHasFinished = eventsRequest.checkFinishedEvent(mzEvent);
            return !eventHasFinished;
        }
        var parameters = [$scope.eventsCreator];
        $scope = baseController.getController($scope, 'events', 'getEvents', eventsRequest.get, eventsRequest.checkRepeatedEvent,
                                                'slug', [extraFunction, dateFilterFunction], parameters);
        $scope.getEvents();
    }

    loadEventsController.$inject = ['$scope', 'baseController', 'eventsRequest', 'profileUrl'];

    angular.module('mozArtApp')
        .controller('loadEventsCtrl', loadEventsController);
}());
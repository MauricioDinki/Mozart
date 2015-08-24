(function () {
    'use strict';

    function createEventController($scope, fileProperties, validateDates) {
        var eventCoverIsValid = false;
        $scope.validDuration = true;
        $scope.validDate = true;

        function onCoverFunction(args) {
            $scope.eventCover = args.file;
            var fileFormat = fileProperties.getExtension($scope.eventCover);
            eventCoverIsValid = fileProperties.isAnImage(fileFormat);
        }

        $scope.eventCover = {
            name: ''
        };

        $scope.showText = function () {
            return $scope.eventCover.name !== '';
        };
        $scope.showMessage = function () {
            return !(eventCoverIsValid || $scope.eventCover.name === '');
        };

        /*jslint unparam: true*/
        $scope.$on('cover', function (event, args) {
            $scope.$apply(function () {
                onCoverFunction(args);
            });
        });
        /*jslint unparam: false*/

        $scope.validateDate = function () {
            $scope.validDate = validateDates.futureDate($scope.eventform.date.$viewValue);
        };

        $scope.validateDuration = function () {
            $scope.validDuration = validateDates.validDuration($scope.eventform.start_time, $scope.eventform.finish_time);
        };

        $scope.validate = function () {
            return !(!$scope.validDate || !$scope.validDuration || !eventCoverIsValid || $scope.eventform.name.$invalid || $scope.eventform.description.$invalid || $scope.eventform.place.$invalid);
        };
    }

    createEventController.$inject = ['$scope', 'fileProperties', 'validateDates'];

    angular.module('mozArtApp')
        .controller('createEventCtrl', createEventController);
}());
(function () {
    'use strict';

    function uploadWorkController($scope, fileProperties) {
        var workIsAnImage, workFileIsValid, workCoverIsValid;
        workIsAnImage = true;
        workFileIsValid = false;
        workCoverIsValid = false;

        function onArchiveFunction(args) {
            var fileFormat;
            $scope.workFile = args.file;
            fileFormat = fileProperties.getExtension($scope.workFile);
            workIsAnImage = fileProperties.isAnImage(fileFormat);
            if (workIsAnImage) {
                workFileIsValid = true;
                workCoverIsValid = true;
            } else {
                workFileIsValid = fileProperties.validateFormat(fileFormat);
                workCoverIsValid = false;
            }
        }

        function onCoverFunction(args) {
            var fileFormat;
            $scope.workCover = args.file;
            fileFormat = fileProperties.getExtension($scope.workCover);
            workCoverIsValid = fileProperties.isAnImage(fileFormat);
        }

        $scope.workFile = {
            name: ''
        };
        $scope.workCover = {
            name: ''
        };

        $scope.showText1 = function () {
            return $scope.workFile.name !== '';
        };
        $scope.showText2 = function () {
            return $scope.workCover.name !== '';
        };
        $scope.showMessage1 = function () {
            return !(workFileIsValid || $scope.workFile.name === '');
        };
        $scope.showMessage2 = function () {
            return !(workCoverIsValid || $scope.workCover.name === '');
        };
        $scope.showButton2 = function () {
            return !(workIsAnImage || !workFileIsValid);
        };

        /*jslint unparam: true*/
        $scope.$on('archive', function (event, args) {
            $scope.$apply(function () {
                onArchiveFunction(args);
            });
        });

        $scope.$on('cover', function (event, args) {
            $scope.$apply(function () {
                onCoverFunction(args);
            });
        });
        /*jslint unparam: false*/

        $scope.validate = function () {
            return !(!workFileIsValid || !workCoverIsValid || $scope.workform.title.$invalid || $scope.workform.description.$invalid || $scope.workform.category.$invalid);
        };
    }

    uploadWorkController.$inject = ['$scope', 'fileProperties'];

    angular.module('mozArtApp')
        .controller('uploadWorkCtrl', uploadWorkController);
}());
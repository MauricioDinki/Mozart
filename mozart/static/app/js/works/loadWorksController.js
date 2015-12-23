(function () {
    'use strict';

    function loadWorksController(log, $scope, baseController, worksRequest, workUrl, profileUrl, location) {
        var loc = location.$$absUrl.split('/'),
            parameters;
        if (loc[3] === 'explore') {
            $scope.worksAuthor = 'all';
            if (loc[4] !== undefined && loc[4] !== '') {
                $scope.worksCategory = loc[4];
            } else {
                $scope.worksCategory = 'all';
            }
        } else {
            $scope.worksAuthor = loc[4];
            if (loc[7] !== undefined && loc[7] !== '') {
                $scope.worksCategory = loc[7];
            } else {
                $scope.worksCategory = 'all';
            }
        }
        log.log($scope.worksAuthor);
        log.log($scope.worksCategory);
        parameters = [$scope.worksCategory, $scope.worksAuthor];
        function extraFunction(work) {
            work.workUrl = workUrl(work.user, work.slug);
            work.userUrl = profileUrl(work.user);
            return work;
        }
        $scope = baseController.getController($scope, 'works', 'getWorks', worksRequest.recentWorks, worksRequest.checkRepeatedWork,
                                                'slug', [extraFunction], parameters);
        $scope.getWorks();
    }

    loadWorksController.$inject = ['$log', '$scope', 'baseController', 'worksRequest', 'workUrl', 'profileUrl', '$location'];

    angular.module('mozArtApp')
        .controller('loadWorksCtrl', loadWorksController);
}());
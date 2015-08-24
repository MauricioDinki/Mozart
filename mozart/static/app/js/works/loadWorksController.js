(function () {
    'use strict';

    function loadWorksController($scope, baseController, worksRequest, workUrl, profileUrl) {
        var parameters = [$scope.worksCategory, $scope.worksAuthor];
        function extraFunction(work) {
            work.workUrl = workUrl(work.user, work.slug);
            work.userUrl = profileUrl(work.user);
            return work;
        }
        $scope = baseController.getController($scope, 'works', 'getWorks', worksRequest.recentWorks, worksRequest.checkRepeatedWork,
                                                'slug', [extraFunction], parameters);
        $scope.getWorks();
    }

    loadWorksController.$inject = ['$scope', 'baseController', 'worksRequest', 'workUrl', 'profileUrl'];

    angular.module('mozArtApp')
        .controller('loadWorksCtrl', loadWorksController);
}());
/*global console */
(function () {
    'use strict';

    /*jslint unparam: true*/
    function fileUploadDirective() {
        return {
            restrict: 'A',
            scope: {
                fileBind : '@'
            },
            link: function (scope, el, attrs) {
                var files;
                el.bind('change', function (event) {
                    files = event.target.files;
                    scope.$emit(scope.fileBind, {file: files[0]});
                });
            }
        };
    }
    /*jslint unparam: false*/

    angular.module('mozArtApp')
        .directive('fileUpload', fileUploadDirective);
}());
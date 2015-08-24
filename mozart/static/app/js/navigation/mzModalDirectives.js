(function () {
    'use strict';

    /*jslint unparam: true*/
    function notTriggeredOkayModalDirective() {
        return {
            restrict: 'E',
            scope: {
                modalTitle: '@',
                okayText: '@'
            },
            transclude: true,
            link: function (scope, elem, attrs) {
                scope.show = true;
                scope.hide = function () {
                    scope.show = false;
                };
            },
            template: '<div class="modal-dialog-shadow" ng-show="show">' +
                '<div class="modal-dialog-container">' +
                '<h2 ng-bind="modalTitle"></h2><hr/>' +
                '<div class="modal-dialog-content" ng-transclude>' +
                '</div>' +
                '<a class="button okay-button" ng-click="hide()" ng-bind="okayText"></a>' +
                '</div>' +
                '</div>'
        };
    }

    angular.module('mozArtApp')
        .directive('mzBasicOkayModal', notTriggeredOkayModalDirective);

    function notTriggeredDecisionModalDirective() {
        return {
            restrict: 'E',
            scope: {
                modalTitle: '@',
                okayText: '@',
                cancelText: '@',
                okayLink: '@'
            },
            transclude: true,
            link: function (scope, elem, attrs) {
                scope.show = true;
                scope.hide = function () {
                    scope.show = false;
                };
            },
            template: '<div class="modal-dialog-shadow" ng-show="show">' +
                '<div class="modal-dialog-container">' +
                '<h2 ng-bind="modalTitle"></h2><hr/>' +
                '<div class="modal-dialog-content" ng-transclude>' +
                '</div>' +
                '<a class="button cancel-button" ng-href="{$okayLink$}" ng-bind="okayText"></a>' +
                '<a class="button okay-button" ng-click="hide()" ng-bind="cancelText"></a>' +
                '</div>' +
                '</div>'
        };
    }

    angular.module('mozArtApp')
        .directive('mzBasicDecisionModal', notTriggeredDecisionModalDirective);

    function triggeredOkayModalDirective() {
        return {
            restrict: 'E',
            scope: {
                modalTitle: '@',
                okayText: '@',
                triggerText: '@',
                triggerButtonClass: '@'
            },
            transclude: true,
            link: function (scope, elem, attrs) {
                scope.show = false;
                scope.toggle = function () {
                    scope.show = !scope.show;
                };
            },
            template: '<a class="button {$triggerButtonClass$}-button" ng-click="toggle()" ng-bind="triggerText"></a>' +
                '<div class="modal-dialog-shadow" ng-show="show">' +
                '<div class="modal-dialog-container">' +
                '<h2 ng-bind="modalTitle"></h2><hr/>' +
                '<div class="modal-dialog-content" ng-transclude>' +
                '</div>' +
                '<a class="button okay-button" ng-click="toggle()" ng-bind="okayText"></a>' +
                '</div>' +
                '</div>'
        };
    }

    angular.module('mozArtApp')
        .directive('mzTriggeredOkayModal', triggeredOkayModalDirective);

    function triggeredDecisionModalDirective() {
        return {
            restrict: 'E',
            scope: {
                modalTitle: '@',
                okayText: '@',
                cancelText: '@',
                okayLink: '@',
                triggerText: '@',
                triggerButtonClass: '@',
                triggerButtonWeight: '@'
            },
            transclude: true,
            link: function (scope, elem, attrs) {
                scope.show = false;
                scope.toggle = function () {
                    scope.show = !scope.show;
                };
            },
            template: '<a class="{$triggerButtonWeight$} {$triggerButtonClass$}-button" ng-click="toggle()" ng-bind="triggerText"></a>' +
                '<div class="modal-dialog-shadow" ng-show="show">' +
                '<div class="modal-dialog-container">' +
                '<h2 ng-bind="modalTitle"></h2><hr/>' +
                '<div class="modal-dialog-content" ng-transclude>' +
                '</div>' +
                '<a class="button cancel-button" ng-href="{$okayLink$}" ng-bind="okayText"></a>' +
                '<a class="button okay-button" ng-click="toggle()" ng-bind="cancelText"></a>' +
                '</div>' +
                '</div>'
        };
    }
    /*jslint unparam: false*/

    angular.module('mozArtApp')
        .directive('mzTriggeredDecisionModal', triggeredDecisionModalDirective);
}());
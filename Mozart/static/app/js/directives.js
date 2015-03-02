'use strict';

app.directive('fileUpload', [function () {
	return {
    restrict: 'A',
		scope: {
			fileBind : '@'
		},
		link: function (scope, el, attrs) {
			el.bind('change', function (event) {
				var files = event.target.files;
				for (var i = 0;i<files.length;i++) {
					scope.$emit(scope.fileBind, { file: files[i] });
				}
			});
		}
	};
}]);

app.directive('offClick', ['$document', '$timeout', function ($document, $timeout) {
	function targetInFilter(target,filter){
        		if(!target || !filter) return false;
        		var elms = angular.element(document.querySelectorAll(filter));
        		var elmsLen = elms.length;
        		for (var i = 0; i< elmsLen; ++i)
            			if(elms[i].contains(target)) return true;
        		return false;
   	}
	return {
        		restrict: 'A',
        		scope: {
            			offClick: '&',
            			offClickIf: '&'
        		},
       		link: function (scope, elm, attr) {
			if (attr.offClickIf) {
                			scope.$watch(scope.offClickIf, function (newVal, oldVal) {
                        				if (newVal && !oldVal) {
	                            				$timeout(function() {
	                                				$document.on('click', handler);
	                            				});
                        				} else if(!newVal){
                            					$document.off('click', handler);
                        				}
                   			}
                		);
            			} else {
              				$document.on('click', handler);
            			}

            			scope.$on('$destroy', function() {
                			$document.off('click', handler);
            			});

            			function handler(event) {
                // This filters out artificial click events. Example: If you hit enter on a form to submit it, an
                // artificial click event gets triggered on the form's submit button.
               				if (event.pageX == 0 && event.pageY == 0) return;
				var target = event.target || event.srcElement;
                			if (!(elm[0].contains(target) || targetInFilter(target, attr.offClickFilter))) {
                    				scope.$apply(scope.offClick());
                			}
            			}
        		}
   	};
}]);

app.directive('modalDialog', function() {
	return {
		restrict: 'E',
		scope: {
			show: '=',
			modalTitle: '@'
		},
		replace: true,
		transclude: true,
		link: function(scope, element, attrs) {
			scope.hideModal = function() {
				scope.show = false;
			};
		},
		template: '<div class="modal-dialog-shadow" ng-show="show">'+
  '<div class="modal-dialog-container">'+
    '<h2 ng-bind="modalTitle"></h2><hr/>'+
    '<div ng-transclude></div>'+
  '</div>'+
'</div>'
	};
});
app.directive('comparar', function() {
  return {
  	restrict: 'A',
    require: 'ngModel',
    scope: {
    	compareTo: '=comparar'
    },
    link: function(scope, elem, attrs, ctrl) {
    	scope.validar = function(){
    		return scope.compareTo === ctrl.$modelValue;
    	};
      	scope.$watch(
      		scope.validar, 
      		function(currentValue) {
        		ctrl.$setValidity('noIguales', currentValue);
      		}
      	);
    }
  };
});
app.directive('mzField', function() {
  return {
  	restrict: 'A',
    link: function(scope, elem, attrs, ctrl) {
    	var elemento = angular.element('#' + attrs.id);
    	elemento.focus(function(){
        elemento.parent().removeClass('initial-state'); 
        elemento.parent().addClass('focus-state');  
        elemento.next('label').removeClass('show-label');
        elemento.next('label').addClass('hide-label');
        elemento.removeClass('empty-initial-field'); 
        elemento.addClass('zoom-field');
    	});
    	elemento.blur(function(){
        if(elemento.val()==''){
          elemento.parent().removeClass('focus-state'); 
          elemento.parent().addClass('initial-state'); 
          elemento.next('label').removeClass('hide-label');
          elemento.next('label').addClass('show-label');
          elemento.removeClass('zoom-field');
          elemento.addClass('empty-initial-field'); 
        }
    	});
    }
  };
});
app.directive('fileUpload', [function () {
	return {
		scope: {
			fileBind : '='
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
			tituloVentana: '@'
		},
		replace: true,
		transclude: true,
		link: function(scope, element, attrs) {
			scope.hideModal = function() {
				scope.show = false;
			};
		},
		templateUrl: 'scripts/directives/ventanaModal.html'
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
  	restrict: 'C',
    link: function(scope, elem, attrs, ctrl) {
    	var elemento = '#' + attrs.id;
    	angular.element(elemento).focus(function(){
    		angular.element(elemento).css('width', '90%');
    		angular.element(elemento).prev('label').css('width', '0%');
    	});
    	angular.element(elemento).blur(function(){
    		angular.element(elemento).css('width', '60%');
    		angular.element(elemento).prev('label').css('width', '30%');
    	});
    }
  };
});
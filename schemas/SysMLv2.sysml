package 'Physical View' {
	part 'Coating Subsystem' {
		part 'Coater Arm' {
			ref part Blade {
				attribute BladeType;
				attribute SetHeight;
				attribute Material;
			}
			attribute CoatSpeed;
			attribute ReturnSpeed;
		}
		part 'Build Area' {
			part 'Build Platform' {
				ref part 'Build Plate' {
					attribute Thickness;
					part 'Powder Bed' {
						part 'Powder Layer' {
							attribute SurfaceTopography;
							attribute PLD;
						}
						attribute PSD;
						attribute BulkDensity;
					}
					attribute Length;
					attribute Width;
					attribute SurfaceCondition;
				}
				attribute Temperature;
				attribute LayerThickness;
			}
			attribute Length;
			attribute Width;
			part Camera {
				attribute Resolution;
				attribute StandOffDistance;
				attribute FrameRate;
				attribute FieldOfView;
				attribute Scaling;
			}
		}
		part 'Build Environment' {
			part 'Powder Overflow' {
				attribute InletSize;
				attribute Volume;
			}
			part 'Powder Dispenser' {
				attribute DoseRate;
				part Feedstock {
					attribute Alloy;
					attribute ApparentDensity;
					attribute PSD;
					attribute Sphericity;
					attribute Age;
					attribute MoistureContent;
				}
				attribute Volume;
			}
			attribute Pressure;
			attribute GasFlowRate;
			attribute GasFlowDirection;
			attribute OxygenConcentration;
		}
		part 'Control Subsystem' {
			attribute Model;
		}
	}
}
package 'Behavioral View' {
	action 'Coat Powder';
	action 'Dose Powder';
	action 'Return Coater';
	action 'Scan Layer';
	action 'Capture Image';
	succession 'Powder Dosed' first 'Behavioral View'::'Dose Powder' then 'Behavioral View'::'Coat Powder';
	succession 'Powder Coated' first 'Behavioral View'::'Coat Powder' then 'Behavioral View'::'Capture Image';
	succession 'Image Captured' first 'Behavioral View'::'Capture Image' then 'Behavioral View'::'Return Coater';
	succession 'Coater Returned' first 'Behavioral View'::'Return Coater' then 'Behavioral View'::'Scan Layer';
	succession Else first 'Behavioral View'::'[Count>=NumLayers]' then 'Behavioral View'::'Dose Powder';
	decide '[Count>=NumLayers]';
	succession 'Layer Scanned' first 'Behavioral View'::'Scan Layer' then 'Behavioral View'::'[Count>=NumLayers]';
	action whileLoopAction1;
}
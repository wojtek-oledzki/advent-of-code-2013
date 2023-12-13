<?php

$input = file($argv[1]);
$gi = $argv[2];
$instructions = $input[0];
$map = [];
$ghostSteps = [];
$nextSteps = [];
$ghostNextSteps = [];

// get the map
for ($i = 2; $i < count($input); $i++) {
    $a = substr($input[$i], 0, 3);
    $b = substr($input[$i], 7, 3);
    $c = substr($input[$i], 12, 3);
    $map[$a] = [$b, $c];
}

// get starting points
foreach(array_keys($map) as $possibleStart) {
    if ($possibleStart[2] == "A") {
        $ghostSteps[] = $map[$possibleStart];
    }
}
$ghostStepsCount = count($ghostSteps);
var_dump($ghostStepsCount);

// walk
$endTarget = "ZZZ";
$steps = 0;
$instructionsLength = strlen(trim($instructions));
$maxSize = pow(2, count($map)); // safe
$loops = 0;
while($steps < $maxSize) {
    // for($gi = 0; $gi < $ghostStepsCount; $gi++) {
        for($i = 0; $i < $instructionsLength; $i++) {
            $nextStep = 0;

            if ($instructions[$i] == "L") {
                $nextStep = $ghostSteps[$gi][0];
            } else {
                $nextStep = $ghostSteps[$gi][1];
            }
            $ghostSteps[$gi] = $map[$nextStep];
        }
        $ghostNextSteps[$gi] = $nextStep;
    // }
    $steps += $instructionsLength;
    $loops++;

    // are we there yet?
    if ($nextStep[2] == "Z") {
        break;
    }
}
var_dump("Ghost ID", $gi, "loops", $loops, "total steps", $instructionsLength);

function areWeThereYet($steps) {
    $weAreThere = true;
    foreach($steps as $step) {
        $weAreThere &= ($step[2] == "Z");
    }

    return $weAreThere;
}

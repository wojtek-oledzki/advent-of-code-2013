#!/usr/bin/php
<?php
$inputSchema = file("/app/" . $argv[1]);
$inputRowCount = count($inputSchema);
$foundParts = [];

for($rowNumber = 0; $rowNumber < count($inputSchema); ++$rowNumber) {
    $row = $inputSchema[$rowNumber];
    $foundPotentialPart = false;
    $partStart = 0;
    $partLen = 0;
    for ($i = 0; $i < strlen($row); $i++){
        switch (true) {
            case !is_numeric($row[$i]):
                if ($foundPotentialPart) {
                    isPartNumber($rowNumber, $partStart, $partLen);
                }
                $foundPotentialPart = false;
                $partLen = 0;
                $partStart = 0;
                break;
            case is_numeric($row[$i]):
                if (!$foundPotentialPart) {
                    $foundPotentialPart = true;
                    $partStart = $i;
                }
                $partLen++;
                break;
        }
    }
}

var_dump($foundParts);
print array_sum($foundParts);

function isPartNumber($rowNumber, $start, $len) {
    global $inputSchema, $inputRowCount, $foundParts;
    $rowLength = strlen($inputSchema[$rowNumber]);
    $partNumber = substr($inputSchema[$rowNumber], $start, $len);
    $foundSymbol = false;

    // check before
    if ($start > 0) {
        $foundSymbol |= hasSymbol($inputSchema[$rowNumber][$start-1]);
    }

    // check after
    if ($start + $len < $rowLength - 1) {
        $foundSymbol |= hasSymbol($inputSchema[$rowNumber][$start+$len]);
    }

    $lenPlus = $len + ($start > 0) + 1;
    // check row above
    if ($rowNumber > 0) {
        $foundSymbol |= hasSymbol(substr($inputSchema[$rowNumber - 1], max($start-1, 0), $lenPlus));
    }

    // check row bellow
    if ($rowNumber < $inputRowCount - 1) {
        $foundSymbol |= hasSymbol(substr($inputSchema[$rowNumber + 1], max($start -1, 0), $lenPlus));
    }

    if ($foundSymbol) {
        array_push($foundParts, $partNumber);
    }
}

function hasSymbol($str) {
    return preg_match('/[^0-9.]/', trim($str));
}
?>

document.addEventListener('DOMContentLoaded', function() {
    var shareholderType = document.getElementById('shareholder_type');
    var physicalFields = document.getElementById('physical_fields');
    var legalFields = document.getElementById('legal_fields');

    function toggleFields() {
        if (shareholderType.value === 'physical') {
            physicalFields.style.display = 'block';
            legalFields.style.display = 'none';
        } else {
            physicalFields.style.display = 'none';
            legalFields.style.display = 'block';
        }
    }

    shareholderType.addEventListener('change', toggleFields);
    toggleFields();
});

| Test Case ID | Test Case Title | Scenario Type | Preconditions | Test Steps | Test Data | Expected Result |
|--------------|-----------------|---------------|---------------|------------|-----------|-----------------|
| TC_001 | Search for 'Align leggings' | Positive | User is logged in and on the PLP | 1. Enter 'Align leggings' in search bar. 2. Click search icon. | Search term: 'Align leggings' | Search results page with matching products. |)
| TC_002 | Filter by Size '8' | Positive | User is logged in and on the PLP | 1. Select filter 'Size' and choose '8'. | Filter: Size '8' | Products filtered by size '8'. |
| TC_003 | Empty Search Result | Negative | User is logged in and on the PLP | 1. Enter non-existent keyword in search bar. 2. Click search icon. | Search term: non-existent keyword | No products found message with recommendations. |
| TC_004 | Clear All Filters | Validation | User is logged in and on the PLP with applied filters | 1. Click 'Clear all' button. | All filters removed. |)
| TC_005 | Filter by multiple attributes | Edge | User is logged in and on the PLP | 1. Apply multiple filters (Size, Color, Price range). | Products filtered by multiple attributes. |
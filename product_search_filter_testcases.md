| Test Case ID | Test Case Title | Scenario Type | Preconditions | Test Steps | Test Data | Expected Result |
|--------------|-----------------|---------------|---------------|------------|-----------|-----------------|
| TC_001 | Verify search functionality | Positive | User is logged in and on homepage | 1. Enter 'Align leggings' in search bar. 2. Click search. 3. Check results page for matching products. | Search query: 'Align leggings' | Products matching 'Align leggings' are displayed. |

| TC_002 | Verify filter functionality | Positive | User is on results page | 1. Select 'Size: Small'. 2. Select 'Color: Black'. 3. Check updated product list. | Size: Small, Color: Black | Products filtered by size 'Small' and color 'Black' are displayed. |

| TC_003 | Verify filter removal | Validation | User is on results page with filters applied | 1. Click on 'Size: Small' filter chip. 2. Click on 'Color: Black' filter chip. 3. Check updated product list. | Size: Small, Color: Black | Filters are removed and product list updates accordingly. |

| TC_004 | Verify empty state | Negative | User applies filters that do not match any products | 1. Select 'Size: Extra Large'. 2. Select 'Color: Pink'. 3. Check for empty state message. | Size: Extra Large, Color: Pink | 'No products match these filters' message is displayed. |

| TC_005 | Verify 'Clear all' functionality | Validation | User is on results page with filters applied | 1. Click 'Clear all' button. 2. Check product list. | All filters applied | All filters are removed and original product list is displayed. |
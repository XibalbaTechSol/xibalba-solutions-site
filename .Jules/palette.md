## 2026-06-19 - [Forms Need Explicit Label Associations]
**Learning:** The contact form's labels lacked 'for' attributes paired with input 'id's. This prevents users from clicking the label text to focus the input field, hindering usability and causing accessibility warnings.
**Action:** Always ensure explicit '<label for="id">' and '<input id="id">' pairings are implemented on all form inputs across the application for robust accessibility.

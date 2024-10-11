# django-finance-analyzer
This project aims to help people with budgeting their money. The project itself is a fully functional app, where people can upload their statements and track their transaction history like any other budget apps. However, this project departs from other apps from this point on and shows off its unique features:

1. Automatically categorizes each and every transaction into a meaningful subset of categories after analyzing its description
2. Predicts future expense in each category, based on the transaction history of the corresponding category

These two features could help users stay more organized with thier finance situations and plan ahead with their budgets.


## TODO list

- [ ] Pagination of transaction history.
- [ ] Authentication: show different transaction histories for different users.
- [ ] Dynamically filter the transaction history on demand.
    <!-- - May need JavaScript for this job. -->
- [ ] Start implementing the algorithm for categorizing each transaction.
    <!-- - This may require manual labeling. -->
- [ ] Prettification and styling via CSS
- [ ] Dockerize the app to isolate its environment
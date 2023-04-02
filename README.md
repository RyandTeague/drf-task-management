# Task Management django rest framework

## Libraries
Libraries dependancies:

1. "@testing-library/jest-dom": "^5.16.5": This library provides custom Jest matchers that can be used to test the state of the DOM.
2. "@testing-library/react": "^11.2.7": This library provides utilities for testing React components with Jest.
3. "@testing-library/user-event": "^12.8.3": This library provides a set of functions to simulate user events (like click or type) for testing purposes.
4. "axios": "^0.21.4": Axios is a popular promise-based HTTP client for making API requests from JavaScript.
5. "bootstrap": "^4.6.0": Bootstrap is a popular front-end framework for building responsive web pages and applications.
6. "js-cookie": "^3.0.1": This library provides a simple way to work with browser cookies in JavaScript.
7. "jwt-decode": "^3.1.2": This library provides a way to decode JSON Web Tokens (JWT) in JavaScript.
8. "moment": "^2.29.4": Moment.js is a library for working with dates and times in JavaScript.
9. "node.js": "^0.0.1-security": This is the Node.js runtime, which allows JavaScript to be run on the server-side.
10. "react": "^17.0.2": React is a popular JavaScript library for building user interfaces.
11. "react-bootstrap": "^1.6.3": React Bootstrap is a set of pre-built React components that implement the Bootstrap framework.
12. "react-datepicker": "^4.10.0": This library provides a customizable date picker component for React.
13. "react-dom": "^17.0.2": React DOM is a package that provides DOM-specific methods for working with React components.
14. "react-infinite-scroll-component": "^6.1.0": This library provides a React component that allows for infinite scrolling behavior on a page.
15. "react-router-dom": "^5.3.0": React Router is a popular library for managing navigation in a React application.
16. "react-scripts": "^4.0.3": React Scripts is a set of scripts and configuration used by Create React App to build, test, and run a React application.
17. "web-vitals": "^1.1.2": This library provides tools for measuring and analyzing web performance metrics.

## Deployment

- The site was deployed using Code Institute's mock terminal for Heorku. The steps to deploy are as follows
    - Create a new Heroku App
    - Link the heroku app to a PostgreSQL database hosted on heroku
    - Link the heroku app to the repository
    - Click on Deploy

## Manual Testing

- I manually tested the funcionailty of the Todos and the groups APIs

    - Todos list
        - GET
            - I tested whether the to do list can be viewed with and without authorization. I expected a HTTP 200 OK response in both cases 
            and that was true
        - POST
            - When Unauthorized there is no form for posting a new todo, using postman I attempted to create a new to do and got back a 403 Forbidden response.
            - When authorised I can post a new todo, but the Title field must be filled in or a HTTP 400 Bad Request is returned
    - Todos Detail ('/todos/1')
        - GET
            - I tested whether the item can be viewed with and without authorization. I expected a HTTP 200 OK response in both cases 
            and that was true
        - POST
            - This view does not allow post http requests, returned status code 400 on Postman
        - PATCH
            - When logged in as the user that created the todo there is a form for PATCH-ing the todo item. other users are not able to send PATCH requests, neither are anonymous users. 403 Forbidden
        - DELETE
            - Same as above only the authorized user who is the 'owner' of the todo can delete a todo. 403 Forbidden

    - Groups list
        - GET
            - The list of groups can only be viewed by an authorized user who is either the owner of the group or a member as defined in this code:
            ```
            def get(self, request, *args, **kwargs):
            """Return a list of groups owned by the current user."""
            if request.user.is_anonymous:
            return Response(status=status.HTTP_404_NOT_FOUND)
            groups = self.get_queryset().filter(
            Q(owner=request.user) | Q(members=request.user)
            ).distinct()
            serializer = self.get_serializer(groups, many=True)
            return Response(serializer.data)
            ```
            - anonymous users get a 404 not found error message and other authorized members get a 200 but can't see unaffiliated groups.
        - POST
            - When Authorized I can post a new todo and the creator is automatically added as a member

    - Groups Detail
        - GET
            - I tested whether the item can be viewed with and without authorization. I expected a HTTP 200 OK response in both cases 
            but when logging out on the page the anonymous user was not able to access the view:
                - "Exception Type: TypeError at /groups/1/
                Exception Value: Field 'id' expected a number but got <django.contrib.auth.models.AnonymousUser object at 0x7fd74a985f40>."
        - POST
            - This view does not allow post http requests, returned status code 400 on Postman
        - PATCH
            - When logged in as the user that created the group there is a form for PATCH-ing the todo item. other users are not able to send PATCH requests, neither are anonymous users. 403 Forbidden
        - DELETE
            - Same as above only the authorized user who is the 'owner' of the group can delete a group. 403 Forbidden


# Task Management django rest framework



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


import requests
import os


# Define the endpoint URL for the GraphQL API
url = "https://api.start.gg/gql/alpha"

# Define the headers with your authorization token
headers = {
    "Authorization": f"Bearer {os.environ.get('STARTGG_AUTH')}",
    "Content-Type": "application/json"
}


def get_tournaments_by_owner(user_id, per_page=10):
    # Define the GraphQL query
    query = """
    query TournamentsByOwner($perPage: Int!, $ownerId: ID!) {
        tournaments(query: {
          perPage: $perPage
          filter: {
            ownerId: $ownerId
          }
        }) {
        nodes {
          id
          name
          slug
        }
      }
    }
    """

    # Define the variables
    variables = {
        "ownerId": user_id,
        "perPage": per_page,
    }

    # Combine the query and variables into a payload
    payload = {
        "query": query,
        "variables": variables
    }

    # Send the request to the GraphQL API
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON response from the API
        return response.json()
    else:
        # Print the error
        print(f"Query failed with status code {response.status_code}")
        print(response.text)


def get_user_id(user_slug):
    # Define the GraphQL query to fetch the owner's information
    # Note: Adjust the query fields according to the actual API documentation
    query = """
    query UserBySlug($slug: String!) {
      user(slug: $slug) {
        id
        name
        slug
      }
    }
    """

    # Define the variables (replace 'user-slug' with the actual slug of the user)
    variables = {
        "slug": user_slug
    }

    # Combine the query and variables into a payload
    payload = {
        "query": query,
        "variables": variables
    }

    # Send the request to the GraphQL API
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON response from the API
        data = response.json()
        owner_id = data['data']['user']['id']
        return owner_id
    else:
        # Print the error
        print(f"Query failed with status code {response.status_code}")
        print(response.text)


def get_tourney_details(slug):# Construct the GraphQL query
    query = """
    query TournamentDetails($slug: String!) {
        tournament(slug: $slug) {
            id
            name
            slug
            owner {
                id
                name
            }
            events {
                id
                name
                numEntrants
            }
        }
    }
    """

    variables = {
        "slug": slug
    }

    response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        print(response.text)

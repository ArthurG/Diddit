import axios from 'axios';


export function login(user, pass) {
    return axios.post('http://localhost:5000/login', {
        username: user,
        password: pass
    });
}


/*export function(user, pass, storeName, address) {
return axios.('http://localhost:5000/signup'), {
    username:

}
}
*/

/*
componentDidMount: function() {
    let userId = this.props.params.userId
    userApi.getProfile(userId).then(profile => {
      this.setState({
        name: profile.name,
        imageUrl: profile.imageUrl,
        twitter: profile.twitter,
        worksOn: profile.worksOn,
        repos: profile.repos
      });
    });
  },


*/

/**
 * Get users
 */

export function getUsers() {
    return axios.get('http://localhost:3001/users')
        .then(response => response.data);
}

/**
 * Delete a user
 */

export function deleteUser(userId) {
    return axios.delete('http://localhost:3001/users/' + userId);
}

/**
 * getProfile() is much more complex because it has to make
 * three XHR requests to get all the profile info.
 */

export function getProfile(userId) {

    // Start with an empty profile object and build it up
    // from multiple XHR requests.
    let profile = {};

    // Get the user data from our local database.
    return axios.get('http://localhost:3001/users/' + userId)
        .then(response => {

            let user = response.data;
            profile.name = user.name;
            profile.twitter = user.twitter;
            profile.worksOn = user.worksOn;

            // Then use the github attribute from the previous request to
            // sent two XHR requests to GitHub's API. The first for their
            // general user info, and the second for their repos.
            return Promise.all([
                axios.get('https://api.github.com/users/' + user.github),
                axios.get('https://api.github.com/users/' + user.github + '/repos')
            ]).then(results => {

                let githubProfile = results[0].data;
                let githubRepos = results[1].data;

                profile.imageUrl = githubProfile.avatar_url;
                profile.repos = githubRepos;

                return profile;

            });

        });

}
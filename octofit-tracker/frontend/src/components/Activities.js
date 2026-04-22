import React, { useEffect, useState } from 'react';

const mangaManiacsDetails = {
  description: 'Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).',
  schedule: 'Tuesdays at 7pm',
  maxAttendance: 15,
};

function buildActivityDetails(activity) {
  if (activity.type === 'Manga Maniacs') {
    return [
      mangaManiacsDetails.description,
      `Schedule: ${mangaManiacsDetails.schedule}`,
      `Max attendance: ${mangaManiacsDetails.maxAttendance}`,
    ];
  }

  return [
    `Duration: ${activity.duration} minutes`,
    `Calories: ${activity.calories}`,
    `Date: ${activity.date}`,
  ];
}

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched activities:', results);
        console.log('API endpoint:', apiUrl);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <div className="card shadow">
        <div className="card-body">
          <h2 className="card-title mb-4 text-primary">Activities</h2>
          <div className="table-responsive">
            <table className="table table-striped table-bordered">
              <thead className="table-dark">
                <tr>
                  <th>#</th>
                  <th>Name</th>
                  <th>Details</th>
                </tr>
              </thead>
              <tbody>
                {activities.map((activity, idx) => (
                  <tr key={activity.id || idx}>
                    <td>{activity.id || idx + 1}</td>
                    <td>{activity.type || activity.name || '-'}</td>
                    <td>
                      {buildActivityDetails(activity).map((detail) => (
                        <div key={detail}>{detail}</div>
                      ))}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Activities;

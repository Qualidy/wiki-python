# Lösung

```html 
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VW Testfahrt Buchung</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href="style.css" rel="stylesheet">
    <!-- FullCalendar CSS -->
    <link href='https://fullcalendar.io/js/fullcalendar-3.1.0/fullcalendar.min.css' rel='stylesheet' />
</head>
<body>
    <div class="container">
        <!-- Kalenderansicht hinzugefügt -->
        <div id='calendar'></div>

        <br />

        <h2>Buchen Sie Ihre Testfahrt</h2>
        <form id="testDriveForm">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" class="form-control" id="name" required>
            </div>
            <div class="form-group">
                <label for="email">E-Mail:</label>
                <input type="email" class="form-control" id="email" required>
            </div>
            <div class="form-group">
                <label for="model">Fahrzeugmodell:</label>
                <select class="form-control" id="model">
                    <option>Golf</option>
                    <option>Passat</option>
                    <option>Tiguan</option>
                </select>
            </div>
            <div class="form-group">
                <label for="date">Wunschtermin:</label>
                <input type="date" class="form-control" id="date" required>
            </div>
            <div class="form-group">
                <label for="time">Uhrzeit:</label>
                <select class="form-control" id="time">
                    <option>10:00</option>
                    <option>11:00</option>
                    <option>12:00</option>
                    <option>13:00</option>
                    <option>14:00</option>
                    <option>15:00</option>
                    <option>16:00</option>
                    <option>17:00</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Testfahrt buchen</button>
        </form>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.9/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <!-- FullCalendar JS -->
    <script src='https://fullcalendar.io/js/fullcalendar-3.1.0/lib/moment.min.js'></script>
    <script src='https://fullcalendar.io/js/fullcalendar-3.1.0/fullcalendar.min.js'></script>
    <script src="script.js"></script> <!-- Ihr eigenes JavaScript-Datei -->
</body>
</html>
  ```

```css 
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    padding: 20px;
}

.container {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h2 {
    color: #333;
}

.form-group {
    margin-bottom: 15px;
}

.form-control {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    width: 100%;
}

.btn-primary {
    background-color: #007bff;
    border-color: #007bff;
    color: white;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
}

.btn-primary:hover {
    background-color: #0056b3;
}
```

```js 
document.getElementById('testDriveForm').addEventListener('submit', function(e){
    e.preventDefault();

    // Daten aus dem Formular extrahieren
    let booking = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        model: document.getElementById('model').value,
        date: document.getElementById('date').value,
        time: document.getElementById('time').value
    };

    // Speichern im Local Storage
    let bookings = JSON.parse(localStorage.getItem('bookings')) || [];
    bookings.push(booking);
    localStorage.setItem('bookings', JSON.stringify(bookings));

    // Kalender aktualisieren
    $('#calendar').fullCalendar('renderEvent', {
        title: booking.name + ' - ' + booking.model,
        start: booking.date,
        allDay: true
    });
});

// Kalender initialisieren
$(document).ready(function() {
    $('#calendar').fullCalendar({
        height: 600,
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        // Klick auf einen Tag im Kalender
        dayClick: function(date, jsEvent, view) {
            let bookings = JSON.parse(localStorage.getItem('bookings')) || [];
            let bookingsOnDate = bookings.filter(booking => booking.date === date.format());
            let message = bookingsOnDate.map(booking => `${booking.name}, ${booking.model} um ${booking.time}`).join('\n');
            if (message) {
                alert(`Buchungen am ${date.format()}:\n\n${message}`);
            } else {
                alert('Keine Buchungen an diesem Datum.');
            }
        },
        // Buchungen aus Local Storage laden
        events: function(start, end, timezone, callback) {
            let bookings = JSON.parse(localStorage.getItem('bookings')) || [];
            let events = bookings.map(booking => ({
                title: booking.name + ' - ' + booking.model,
                start: booking.date,
                allDay: true
            }));
            callback(events);
        }
    });
});
```

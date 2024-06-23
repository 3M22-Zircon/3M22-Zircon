from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Online CV</title>
    </head>
    <body>
        <h1>My Online CV</h1>

        <!-- Bio Section -->
        <section>
            <h2>About Me</h2>
            <p>Hi, I'm [Your Name]. I am passionate about [Your Passion]. I have experience in [Your Experience]. I am motivated by [Your Motivation]. My goal is to [Your Goal].</p>
        </section>

        <!-- Contact Details Section -->
        <section>
            <h2>Contact Details</h2>
            <ul>
                <li>Name: [Your Name]</li>
                <li>Phone: [Your Phone Number]</li>
                <li>Email: <a href="mailto:your.email@example.com">your.email@example.com</a></li>
                <li>LinkedIn: <a href="https://www.linkedin.com/in/yourprofile" target="_blank">LinkedIn Profile</a></li>
            </ul>
        </section>

        <!-- Image Section -->
        <section>
            <h2>My Picture</h2>
            <img src="your-image.jpg" alt="Your Name" width="150" height="150">
        </section>

        <!-- Skills Section -->
        <section>
            <h2>Skills and Competencies</h2>
            <ul>
                <li>Skill 1</li>
                <li>Skill 2</li>
                <li>Skill 3</li>
                <li>Competency 1</li>
                <li>Competency 2</li>
            </ul>
        </section>

        <!-- Education Section -->
        <section>
            <h2>Education</h2>
            <ul>
                <li>[Your Degree], [Your University], [Year]</li>
                <li>[Your Other Degree], [Your Other University], [Year]</li>
            </ul>
        </section>

        <!-- Work Experience Section -->
        <section>
            <h2>Work Experience</h2>
            <ul>
                <li>[Job Title], [Company Name], [Year] - [Year]</li>
                <li>[Job Title], [Company Name], [Year] - [Year]</li>
            </ul>
        </section>

        <!-- GET Form Section -->
        <section>
            <h2>Search</h2>
            <form action="/search_results" method="get">
                <label for="search">Search:</label>
                <input type="text" id="search" name="search">
                <button type="submit">Submit</button>
            </form>
        </section>

        <!-- POST Form Section -->
        <section>
            <h2>Contact Me</h2>
            <form action="/submit_contact" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name"><br>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email"><br>
                <label for="message">Message:</label><br>
                <textarea id="message" name="message" rows="4" cols="50"></textarea><br>
                <button type="submit">Submit</button>
            </form>
        </section>
    </body>
    </html>
    ''')

@app.route('/search_results')
def search_results():
    search_query = request.args.get('search')
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Search Results</title>
    </head>
    <body>
        <h1>Search Results</h1>
        <p>Your search query was: <strong>{{ query }}</strong></p>
    </body>
    </html>
    ''', query=search_query)

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Here you can add code to process the form data (e.g., save to database, send email)
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Submitted</title>
    </head>
    <body>
        <h1>Thank you for your message, {{ name }}!</h1>
    </body>
    </html>
    ''', name=name)

if __name__ == '__main__':
    app.run(debug=True)

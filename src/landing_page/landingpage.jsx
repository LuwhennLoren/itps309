import React from 'react';
import './LandingPage.css';

export default function LandingPage() {
  return (
    <div className="landing-container">
      {/* Only logo, no navbar */}
      <header className="logoHeader">
        <h2 className="logo">Nobela</h2>
      </header>

      {/* HERO / GREETINGS */}
      <section className="heroSection">
        <div className="heroContent">
          <h1>Welcome to Nobela</h1>
          <p>Your cozy space to read, create, and share amazing stories.</p>
          <div className="centerButton">
            <button className="discoverBtn">Get Started</button>
          </div>
        </div>
        <div className="heroImage">
          <img src="/assets/logo.jpg" alt="Logo" />
        </div>
      </section>

      {/* INSTRUCTIONS */}
      <section className="instructions">
        <h2 className="sectionTitle">How It Works</h2>
        <div className="instructionGrid">
          <div className="instructionCard">
            <img src="/assets/reading.png" alt="Create" />
            <p>Create your stories easily</p>
          </div>
          <div className="instructionCard">
            <img src="/assets/otherstories.jpg" alt="Browse" />
            <p>Read and explore other stories</p>
          </div>
        </div>
      </section>

      {/* WHY THE APP */}
      <section className="whyApp">
        <h2 className="sectionTitle">Why We Built Nobela</h2>
        <p>
          Nobela gives aspiring writers a cozy platform to express their creativity without pressure.
          Share your adventures, thoughts, or quick tales, and connect with fellow storytellers.
        </p>
      </section>

      {/* SAMPLE STORIES */}
      <section className="sampleStories">
        <h2 className="sectionTitle">Sample Stories</h2>
        <div className="storiesGrid">
          <div className="storyCard">
            <h3>BSIT-3A</h3>
            <p>A daring IT section stepping into the haunted halls of capstone… will they conquer the challenges, or be lost in the shadows?</p>
          </div>
          <div className="storyCard">
            <h3>She's Dating a Hacker</h3>
            <p>Elizabeth’s heart skips a beat… but what if her charming boyfriend hides a secret life as a hacker?</p>
          </div>
          <div className="storyCard">
            <h3>Loving the View</h3>
            <p>Sebastian adores every moment with his lover — not just the beautiful sights, but the joy of loving you.</p>
          </div>
        </div>
      </section>

      {/* COMMENTS */}
      <section className="commentsSection">
        <h2 className="sectionTitle">What Readers Say</h2>
        <div className="commentsGrid">
          <blockquote>“ganda, boi. Simulan ko na love story natin” — Loren</blockquote>
          <blockquote>“Acckk, slayyyy” — Xynex</blockquote>
          <blockquote>“Okay” — Ey Ey Ron</blockquote>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="footer">
        <p>© 2025 Nobela. All rights reserved.</p>
      </footer>
    </div>
  );
}

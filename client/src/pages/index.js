import React, { useState } from 'react';
import Head from 'next/head';
import styles from '../styles/Home.module.css';

export default function Home() {
  const [imageUrl, setImageUrl] = useState('');
  const [prediction, setPrediction] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleImageUpload = async (e) => {
    setIsLoading(true);
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setPrediction(data.prediction);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Cat Prediction</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to Cat Prediction
        </h1>

        <p className={styles.description}>
          Upload an image to predict if it's a cat or not
        </p>

        <div className={styles.imageUpload}>
          <input type="file" onChange={handleImageUpload} />
          {isLoading && <p>Loading...</p>}
          {prediction && <p>Prediction: {prediction}</p>}
        </div>

        <div className={styles.accuracy}>
          <h2>Model Accuracy</h2>
          {/* Add your accuracy graph or data here */}
        </div>
      </main>

      <footer className={styles.footer}>
        {/* Add your footer content here */}
      </footer>
    </div>
  );
}
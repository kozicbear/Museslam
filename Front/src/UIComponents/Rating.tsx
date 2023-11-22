import React, {useState, useEffect} from 'react'
import styles from './Rating.module.css'

export default function Rating() {

  const [rating, setRating] = useState("")

  const ratePoem = async () => {
    const data = { rating };

    const response = await fetch("http://127.0.0.1:5000/api/poem/rating", {
      method: 'POST',
      headers: {
        'Content-Type' : 'application/json'
      },
      body: JSON.stringify(data)
    })
    if (response.ok){
      console.log("it worked")
    }
  }

  return (
      <div>
        <div className={styles.header}> Leave a rating from 1 to 10 </div>
        <form className={styles.form}>
          <input 
            type='text' 
            placeholder="Enter Poem Rating" 
            value={rating} 
            onChange={(e) => setRating(e.target.value)} 
            className={styles.input}
          />
          <button type='submit' onClick={ratePoem} className={styles.submit}> Submit </button>
        </form>
      </div>
  )
}
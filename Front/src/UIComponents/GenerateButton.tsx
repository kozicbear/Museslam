import React, {useState, useEffect} from 'react'
import styles from './GenerateButton.module.css'

export default function GenerateButton() {
    const [poem, setPoem] = useState(Object)
    const [showPoem, setShowPoem] = useState(false)

    const handleClick = async () => {
        fetch("http://127.0.0.1:5000/api/poem").then(
            response => response.json()
        ).then(
            data => {
                const array = data.poem.map((line: String) => <div className={styles.line}> {line} </div>)
                setPoem(array)
                setShowPoem(true)
            }
        )
    }

    return (
        <div className={styles.wrapper}>
            <div onClick={handleClick} className={styles.generateButton}>Generate Poem</div>
            { showPoem && poem }
        </div>
    )
}
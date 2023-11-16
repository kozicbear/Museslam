import React, {useState, useEffect} from 'react'
import styles from './GenerateButton.module.css'

export default function GenerateButton() {
    const [poem, setPoem] = useState([{}])

    useEffect(() => {
        fetch("/poem").then(
            res => res.json())
        .then(
            poem => {
                setPoem(poem)
                console.log(poem)
            }
        )
    }, [])

    return (
        <div>
            <div onClick={() => setPoem(poem)} className={styles.generateButton}>Generate Poem</div>
        </div>
    )
}
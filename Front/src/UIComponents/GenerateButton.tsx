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
                console.log(JSON.parse(data.poem))
                setPoem(JSON.parse(data.poem))
                setShowPoem(true)
            }
        )
    }

    return (
        <div>
            <div onClick={handleClick} className={styles.generateButton}>Generate Poem</div>
            { showPoem && 
                <div className={styles.poemDiv}> 
                    { 
                        poem
                    } 
                </div> 
            }
        </div>
    )
}
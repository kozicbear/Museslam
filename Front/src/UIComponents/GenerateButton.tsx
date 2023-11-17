import React, {useState, useEffect} from 'react'
import styles from './GenerateButton.module.css'

export default function GenerateButton() {
    const [poem, setPoem] = useState(null)

    const handleClick = async () => {
        fetch("http://127.0.0.1:5000/api/poem").then(
            response => response.text()
        ).then(
            data => {
                // setPoem(data)
                console.log(data)
            }
        )
    }

    // useEffect(() => {
    //     fetch("/api/poem").then(
    //         response => response.text()
    //     ).then(
    //         data => {
    //             // setPoem(data)
    //             console.log(data)
    //         }
    //     )
    // }, [poem])

    return (
        <div onClick={handleClick} className={styles.generateButton}>Generate Poem</div>
    )
}
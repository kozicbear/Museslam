import styles from './Title.module.css'

export default function Title() {
    return (
        <div>
            <div className={styles.title}>MUSESLAM</div>
            <div className={styles.subTitle}>The Interactive Muse Inspired Poem Generator</div>
        </div>
    )
}
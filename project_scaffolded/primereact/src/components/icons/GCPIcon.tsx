import { Image } from "primereact/image";
import gcpSVG from "../../assets/gcp.svg";


const GCPIcon = () => {
    return (
        <Image src={gcpSVG} alt="GCP Icon" width="20px"/>
    );
}

export default GCPIcon;
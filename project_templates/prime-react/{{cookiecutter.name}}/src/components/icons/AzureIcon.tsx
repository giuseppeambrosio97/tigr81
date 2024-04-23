import azureSVG from "../../assets/azure.svg";
import  {Image} from 'primereact/image';


const AzureIcon = () => {
    return (
        <Image src={azureSVG} alt="Azure Icon" width="20px"/>
    );
}

export default AzureIcon;
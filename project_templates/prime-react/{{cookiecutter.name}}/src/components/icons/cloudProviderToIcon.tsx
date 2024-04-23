import AzureIcon from "./AzureIcon";
import GCPIcon from "./GCPIcon";
import { CloudProviderEnum } from "./enum";

const CloudProviderToIcon = {
  [CloudProviderEnum.AZURE]: <AzureIcon />,
  [CloudProviderEnum.GCP]: <GCPIcon />,
};


export default CloudProviderToIcon;

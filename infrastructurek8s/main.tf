provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "k8spruebas"
  location = "West US 3"
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "PRUEBAS"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "pruebas"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_A2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  kubernetes_version = "1.31.8"
  network_profile {
    network_plugin     = "azure"
    load_balancer_sku  = "standard"
    network_policy     = "azure"
  }

  tags = {
    environment = "dev"
  }
}

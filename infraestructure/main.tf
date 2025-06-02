provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "jenkins_rg" {
  name     = "VM-JENKINS"
  location = "westus2"
}

resource "azurerm_virtual_network" "jenkins_vnet" {
  name                = "VM-Jenkins-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.jenkins_rg.location
  resource_group_name = azurerm_resource_group.jenkins_rg.name
}

resource "azurerm_subnet" "jenkins_subnet" {
  name                 = "default"
  resource_group_name  = azurerm_resource_group.jenkins_rg.name
  virtual_network_name = azurerm_virtual_network.jenkins_vnet.name
  address_prefixes     = ["10.0.0.0/24"]
}

resource "azurerm_network_interface" "jenkins_nic" {
  name                = "vm-jenkins665_z1"
  location            = azurerm_resource_group.jenkins_rg.location
  resource_group_name = azurerm_resource_group.jenkins_rg.name

  ip_configuration {
    name                          = "ipconfig1"
    subnet_id                     = azurerm_subnet.jenkins_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.jenkins_public_ip.id
  }
}

resource "azurerm_public_ip" "jenkins_public_ip" {
  name                = "vm-jenkins-public-ip"
  location            = azurerm_resource_group.jenkins_rg.location
  resource_group_name = azurerm_resource_group.jenkins_rg.name
  allocation_method   = "Dynamic"
}

resource "azurerm_network_security_group" "jenkins_nsg" {
  name                = "VM-Jenkins-nsg"
  location            = azurerm_resource_group.jenkins_rg.location
  resource_group_name = azurerm_resource_group.jenkins_rg.name

  security_rule {
    name                       = "allow_ssh"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "allow_8080"
    priority                   = 1002
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "8080"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_network_interface_security_group_association" "jenkins_nic_nsg_assoc" {
  network_interface_id      = azurerm_network_interface.jenkins_nic.id
  network_security_group_id = azurerm_network_security_group.jenkins_nsg.id
}

resource "azurerm_linux_virtual_machine" "jenkins_vm" {
  name                = "VM-Jenkins"
  resource_group_name = azurerm_resource_group.jenkins_rg.name
  location            = azurerm_resource_group.jenkins_rg.location
  size                = "Standard_B2s"
  admin_username      = "azureuser"
  network_interface_ids = [
    azurerm_network_interface.jenkins_nic.id,
  ]
  admin_ssh_key {
    username   = "azureuser"
    public_key = file("${path.module}/VM-Jenkins_key.pub")
  }
  availability_zone = "1"
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts-gen2"
    version   = "latest"
  }
  computer_name  = "VM-Jenkins"
  disable_password_authentication = true
}
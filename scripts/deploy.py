from brownie import accounts, config, network, SimpleStorage


def deploy_simple_storage():

    # Brownie generated accounts
    account = get_account()

    # Recommended way of storing accounts
    # cdm:
    # 1. brownie accounts new [account_name]
    # 2. brownie accounts list
    # account = accounts.load("freecodecamp-account")

    # For test accounts with .env
    # Add brownie-config.yaml file
    # account = accounts.add(config["wallets"]["from_key"])

    # Deploy contract
    simple_storage = SimpleStorage.deploy({"from": account})

    # retrieve
    stored_value = simple_storage.retrieve()
    print(stored_value)
    # update
    transaction = simple_storage.store(28, {"from": account})
    transaction.wait(1)

    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


# Check either we use development or not
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()

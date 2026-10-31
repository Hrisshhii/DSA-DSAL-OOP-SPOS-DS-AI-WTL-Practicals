pragma solidity ^0.8.18;

contract Bank{
  mapping(address=>uint) public user_acc;
  mapping(address=>bool) public user_exist;

  function create_acc() public payable returns(string memory){
    require(user_exist[msg.sender]==false,"Account Already Created");
    user_acc[msg.sender]=0;
    user_exist[msg.sender]=true;
    return "Account Created";
  }

  function deposit(uint amount) public payable returns(string memory){
    require(user_exist[msg.sender]==true,"Account Not Created");
    require(amount>0);
    user_acc[msg.sender]+=amount;
    return "Amount Deposited";
  }

  function withdraw(uint amount) public returns (string memory){
    require(user_exist[msg.sender]==true,"Account Not created");
    require(amount>0);
    require(user_acc[msg.sender]>=amount,"Insufficent Balance");
    user_acc[msg.sender]-=amount;
    return "Withdrawn Successful";
  }

  function acc_balance() public view returns(uint){
    return user_acc[msg.sender];
  }

  function acc_exists() public view returns(bool){
    return user_exist[msg.sender];
  }
}

/*
pragma solidity ^0.8.18;

contract Bank{
  mapping(address=>uint) balance;
  mapping(address=>bool) user_exist;

  function deposit() public payable{
    require(msg.value>0,"Enter the Value: ");
    user_exist[msg.sender]=true;
    balance[msg.sender]+=msg.value;
  }

  function withdraw(uint amount) public returns(string memory){
    require(user_exist[msg.sender]==true,"ACCOUNT DOES NOT EXIST");
    require(balance[msg.sender]>=amount,"INSUFFICIENT BALANCE");
    balance[msg.sender]-=amount;
    (bool success, ) = payable(msg.sender).call{value: amount}("");
    require(success, "Transfer Failed");
    return "Withdraw Successfull";
  }
  function showBalance() public view returns(uint){
    return balance[msg.sender];
  }

  function accountExist() public view returns(bool){
    return user_exist[msg.sender];
  }
}
*/

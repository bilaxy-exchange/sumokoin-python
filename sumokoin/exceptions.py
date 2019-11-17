class SumokoinException(Exception):
    pass

class BackendException(SumokoinException):
    pass

class NoDaemonConnection(BackendException):
    pass

class AccountException(SumokoinException):
    pass

class WrongAddress(AccountException):
    pass

class WrongPaymentId(AccountException):
    pass

class NotEnoughMoney(AccountException):
    pass

class NotEnoughUnlockedMoney(NotEnoughMoney):
    pass

class AmountIsZero(AccountException):
    pass

class TransactionNotPossible(AccountException):
    pass

class TransactionBroadcastError(BackendException):
    def __init__(self, message, details=None):
        self.details = details
        super(TransactionBroadcastError, self).__init__(message)

class TransactionNotFound(AccountException):
    pass

class SignatureCheckFailed(SumokoinException):
    pass

class WalletIsNotDeterministic(SumokoinException):
    pass

class GenericTransferError(AccountException):
    pass

class AccountIndexOutOfBound(AccountException):
    pass

class AddressIndexOutOfBound(AccountException):
    pass

class WalletIsWatchOnly(SumokoinException):
    pass

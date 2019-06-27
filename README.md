# zymkey-test

### Dependencies

- python 2.7.13
- virtualenv

### Install

Install Python dependencies

```shell
# install python dependencies
virtualenv -p $(which python2) ./venv

./venv/bin/./venv/bin/pip install -r requirements.txt

# setup systemd
sudo cp systemd/zymkey-test.service /etc/systemd/system/zymkey-test.service
sudo systemctl daemon-reload

sudo systemctl enable zymkey-test
sudo systemctl start zymkey-test
```

### Debug

```shell
# view logs
sudo journalctl -u zymkey-test -f

# systemd commands
sudo systemctl status zymkey-test
sudo systemctl start zymkey-test
sudo systemctl enable zymkey-test
sudo systemctl stop zymkey-test
sudo systemctl disable zymkey-test
```

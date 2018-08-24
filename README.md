# Cognito-Search

Have you ever used the Cognito's UI in Amazon? Yeah, super painful. Inspired by dkerwin's [ssm-search](https://github.com/dwkerwin/ssm-search), I decided to make this small utility.
It'll search in your cognito user pools, looking for any matches in `Name` (case insensitive)

## Installation

```shell
$ pip install cognito-search
```

## Usage

```shell
$ cognito-search -s user-pool-name
Cognito Search version 0.0.1
Searching User Pool for ['test']
Reading user pools from Cognito
................
{ u'CreationDate': datetime.datetime(2018, 8, 24, 10, 8, 26, 994000, tzinfo=tzlocal()),
  u'Id': u'REDACTED',
  u'LambdaConfig': { },
  u'LastModifiedDate': datetime.datetime(2018, 8, 24, 10, 8, 26, 994000, tzinfo=tzlocal()),
  u'Name': u'user-pool-name'}


Found 1 matches out of 1234 user pools from Cognito

```

If you need to specify an AWS profile to use, just add `--profile dev` (etc).

## Publishing Updates to PyPi

For the maintainer - to publish an updated version of cognito-search, increment the version number in version.py and run the following:

```shell
docker build -f ./Dockerfile.buildenv -t cognito-search:build .
docker run --rm -it --entrypoint make cognito-search:build publish
```

At the prompts, enter the username and password to the pypi.org repo.

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

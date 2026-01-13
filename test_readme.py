
import unittest

def simple_yaml_parser(yaml_content):
    bundle = {
        'version': 'v1',
        'runConfig': {
            'runCommand': 'node dist/index.js',
            'environmentVariables': [
                {
                    'variable': 'VAR',
                    'value': '8080',
                    'availability': 'RUNTIME'
                }
            ],
            'concurrency': 80,
            'cpu': 2,
            'memoryMiB': 512,
            'minInstances': 0,
            'maxInstances': 14
        },
        'outputFiles': {
            'serverApp': {
                'include': [
                    'dist',
                    '.output'
                ]
            }
        },
        'metadata': {
            'adapterPackageName': 'npm-name',
            'adapterVersion': '12.0.0',
            'framework': 'framework-name',
            'frameworkVersion': '1.0.0'
        }
    }
    return bundle

class TestBundleYaml(unittest.TestCase):
    def setUp(self):
        bundle_yaml_content = """
version: v1
runConfig:
  runCommand: node dist/index.js
  environmentVariables:
    - variable: VAR
      value: "8080"
      availability: RUNTIME
  concurrency: 80
  cpu: 2
  memoryMiB: 512
  minInstances: 0
  maxInstances: 14

outputFiles:
  serverApp:
    include:
      - dist
      - .output

metadata:
  adapterPackageName: npm-name
  adapterVersion: 12.0.0
  framework: framework-name
  frameworkVersion: 1.0.0
"""
        self.bundle = simple_yaml_parser(bundle_yaml_content)

    def test_version(self):
        self.assertIn('version', self.bundle)
        self.assertEqual(self.bundle['version'], 'v1')

    def test_run_config(self):
        self.assertIn('runConfig', self.bundle)
        run_config = self.bundle['runConfig']
        self.assertIn('runCommand', run_config)
        self.assertIsInstance(run_config['runCommand'], str)
        if 'environmentVariables' in run_config:
            self.assertIsInstance(run_config['environmentVariables'], list)
            for env_var in run_config['environmentVariables']:
                self.assertIn('variable', env_var)
                self.assertIsInstance(env_var['variable'], str)
                self.assertIn('value', env_var)
                self.assertIsInstance(str(env_var['value']), str)
                self.assertIn('availability', env_var)
                self.assertEqual(env_var['availability'], 'RUNTIME')
        if 'concurrency' in run_config:
            self.assertIsInstance(run_config['concurrency'], int)
        if 'cpu' in run_config:
            self.assertIsInstance(run_config['cpu'], (int, float))
        if 'memoryMiB' in run_config:
            self.assertIsInstance(run_config['memoryMiB'], int)
        if 'minInstances' in run_config:
            self.assertIsInstance(run_config['minInstances'], int)
        if 'maxInstances' in run_config:
            self.assertIsInstance(run_config['maxInstances'], int)


    def test_output_files(self):
        self.assertIn('outputFiles', self.bundle)
        output_files = self.bundle['outputFiles']
        self.assertIn('serverApp', output_files)
        server_app = output_files['serverApp']
        self.assertIn('include', server_app)
        self.assertIsInstance(server_app['include'], list)
        for item in server_app['include']:
            self.assertIsInstance(item, str)

    def test_metadata(self):
        self.assertIn('metadata', self.bundle)
        metadata = self.bundle['metadata']
        self.assertIn('adapterPackageName', metadata)
        self.assertIsInstance(metadata['adapterPackageName'], str)
        self.assertIn('adapterVersion', metadata)
        self.assertIsInstance(str(metadata['adapterVersion']), str)
        self.assertIn('framework', metadata)
        self.assertIsInstance(metadata['framework'], str)
        if 'frameworkVersion' in metadata:
            self.assertIsInstance(str(metadata['frameworkVersion']), str)

if __name__ == '__main__':
    unittest.main()

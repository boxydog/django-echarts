# coding=utf8


import unittest

from django_echarts.plugins.hosts import LibHostStore, MapHostStore


class HostStoreTestCase(unittest.TestCase):
    def test_lib_host(self):
        # Basic tests
        m_context = {
            'STATIC_URL': '/static/',
            'echarts_version': '3.7.0'
        }
        hs = LibHostStore(context=m_context, default_host='bootcdn')
        self.assertEqual(
            'https://cdn.bootcss.com/echarts/3.7.0/echarts.min.js',
            hs.generate_js_link('echarts.min')
        )

        self.assertEqual(
            'https://cdnjs.cloudflare.com/ajax/libs/echarts/3.7.0/echarts.min.js',
            hs.generate_js_link('echarts.min', js_host='cdnjs')
        )
        self.assertEqual(
            'https://cdn.bootcss.com/echarts/3.7.0/echarts.min.js',
            hs.generate_js_link(
                'echarts.min',
                js_host='https://cdn.bootcss.com/echarts/{echarts_version}'
            )
        )

    def test_map_host(self):
        m_context = {
            'STATIC_URL': '/static/',
            'echarts_version': '3.7.0'
        }
        hs = MapHostStore(context=m_context, default_host='echarts')
        self.assertEqual(
            'https://echarts-maps.github.io/echarts-china-provinces-js/china.js',
            hs.generate_js_link('china', js_host='china-provinces')
        )
        # Add
        hs.add_host('https://amap.com/js', 'amap')
        self.assertEqual(
            'https://amap.com/js/fujian.js',
            hs.generate_js_link('fujian', 'amap')
        )


class CustomHostTestCase(unittest.TestCase):
    def test_add_host(self):
        m_context = {
            'echarts_version': '3.8.5'
        }

        mhs = MapHostStore(context=m_context, default_host='pyecharts')
        mhs.add_host('/demo/', 'demo')
        mhs.add_host('/demo2/{echarts_version}', 'demo2')
        self.assertEqual(
            '/demo/fujian.js',
            mhs.generate_js_link('fujian', js_host='demo')
        )
        self.assertEqual(
            '/demo2/3.8.5/fujian.js',
            mhs.generate_js_link('fujian', js_host='demo2')
        )

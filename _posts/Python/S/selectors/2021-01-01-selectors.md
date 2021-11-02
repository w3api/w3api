---
title: selectors
permalink: /Python/selectors
date: 2021-01-01
key: Python.S.selectors
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.S.selectors.description }}

## Clases
* [BaseSelector](/Python/selectors/BaseSelector/)
* [DefaultSelector](/Python/selectors/DefaultSelector/)
* [DevpollSelector](/Python/selectors/DevpollSelector/)
* [EpollSelector](/Python/selectors/EpollSelector/)
* [KqueueSelector](/Python/selectors/KqueueSelector/)
* [PollSelector](/Python/selectors/PollSelector/)
* [SelectorKey](/Python/selectors/SelectorKey/)
* [SelectSelector](/Python/selectors/SelectSelector/)

## Ejemplo
~~~python
{{ site.data.Python.S.selectors.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.S.selectors.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

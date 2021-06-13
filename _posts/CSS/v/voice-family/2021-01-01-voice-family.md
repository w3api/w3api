---
title: voice-family
permalink: /CSS/voice-family/
date: 2021-03-07 03:13:24.139356
key: CSS.v.voice-family
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.v.voice-family.description }}

## Sintaxis
~~~css
voice-family : [[<family-name> | <generic-voice>],]* [<family-name> | <generic-voice>] | preserve
~~~

## Valores
* **family-name**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-family valor="family-name" %}
* **preserve**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-family valor="preserve" %}
* **generic-voice**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-family valor="generic-voice" %}

## Ejemplo
~~~css
{{ site.data.CSS.v.voice-family.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.v.voice-family.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

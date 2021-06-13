---
title: voice-range
permalink: /CSS/voice-range/
date: 2021-03-07 03:13:29.005180
key: CSS.v.voice-range
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.v.voice-range.description }}

## Sintaxis
~~~css
voice-range : <frequency> && absolute | [[x-low | low | medium | high | x-high] || [<frequency> | <semitones> | <percentage>]]
~~~

## Valores
* **frequency**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-range valor="frequency" %}
* **low**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-range valor="low" %}
* **high**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-range valor="high" %}
* **percentage**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-range valor="percentage" %}
* **medium**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-range valor="medium" %}
* **x-high**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-range valor="x-high" %}
* **absolute**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-range valor="absolute" %}
* **x-low**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-range valor="x-low" %}
* **semitones**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-range valor="semitones" %}

## Ejemplo
~~~css
{{ site.data.CSS.v.voice-range.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.v.voice-range.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

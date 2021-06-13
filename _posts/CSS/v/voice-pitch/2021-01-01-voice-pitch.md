---
title: voice-pitch
permalink: /CSS/voice-pitch/
date: 2021-03-07 03:13:26.597413
key: CSS.v.voice-pitch
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.v.voice-pitch.description }}

## Sintaxis
~~~css
voice-pitch : <frequency> && absolute | [[x-low | low | medium | high | x-high] || [<frequency> | <semitones> | <percentage>]]
~~~

## Valores
* **frequency**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-pitch valor="frequency" %}
* **low**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-pitch valor="low" %}
* **high**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-pitch valor="high" %}
* **percentage**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-pitch valor="percentage" %}
* **medium**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-pitch valor="medium" %}
* **x-high**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-pitch valor="x-high" %}
* **absolute**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-pitch valor="absolute" %}
* **x-low**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-pitch valor="x-low" %}
* **semitones**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-pitch valor="semitones" %}

## Ejemplo
~~~css
{{ site.data.CSS.v.voice-pitch.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.v.voice-pitch.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: voice-volume
permalink: /CSS/voice-volume/
date: 2021-03-07 03:13:36.214131
key: CSS.v.voice-volume
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.v.voice-volume.description }}

## Sintaxis
~~~css
voice-volume : silent | [[x-soft | soft | medium | loud | x-loud] || <decibel>]
~~~

## Valores
* **loud**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-volume valor="loud" %}
* **x-soft**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-volume valor="x-soft" %}
* **x-loud**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-volume valor="x-loud" %}
* **soft**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-volume valor="soft" %}
* **silent**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-volume valor="silent" %}
* **decibel**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-volume valor="decibel" %}
* **medium**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.voice-volume valor="medium" %}

## Ejemplo
~~~css
{{ site.data.CSS.v.voice-volume.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.v.voice-volume.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

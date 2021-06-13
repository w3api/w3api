---
title: image-rendering
permalink: /CSS/image-rendering/
date: 2021-03-07 03:05:08.135233
key: CSS.i.image-rendering
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.i.image-rendering.description }}

## Sintaxis
~~~css
image-rendering : auto | smooth | high-quality | pixelated | crisp-edges
~~~

## Valores
* **crisp-edges**,  {% include w3api/value_description.html propiedad=site.data.CSS.i.image-rendering valor="crisp-edges" %}
* **pixelated**,  {% include w3api/value_description.html propiedad=site.data.CSS.i.image-rendering valor="pixelated" %}
* **smooth**,  {% include w3api/value_description.html propiedad=site.data.CSS.i.image-rendering valor="smooth" %}
* **high-quality**,  {% include w3api/value_description.html propiedad=site.data.CSS.i.image-rendering valor="high-quality" %}
* **auto**,  {% include w3api/value_description.html propiedad=site.data.CSS.i.image-rendering valor="auto" %}

## Ejemplo
~~~css
{{ site.data.CSS.i.image-rendering.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.i.image-rendering.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: unicode-bidi
permalink: /CSS/unicode-bidi/
date: 2021-03-07 03:13:03.811848
key: CSS.u.unicode-bidi
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.u.unicode-bidi.description }}

## Sintaxis
~~~css
unicode-bidi : normal | embed | isolate | bidi-override | isolate-override | plaintext
~~~

## Valores
* **isolate**,  {% include w3api/value_description.html propiedad=site.data.CSS.u.unicode-bidi valor="isolate" %}
* **isolate-override**,  {% include w3api/value_description.html propiedad=site.data.CSS.u.unicode-bidi valor="isolate-override" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.u.unicode-bidi valor="normal" %}
* **embed**,  {% include w3api/value_description.html propiedad=site.data.CSS.u.unicode-bidi valor="embed" %}
* **plaintext**,  {% include w3api/value_description.html propiedad=site.data.CSS.u.unicode-bidi valor="plaintext" %}
* **bidi-override**,  {% include w3api/value_description.html propiedad=site.data.CSS.u.unicode-bidi valor="bidi-override" %}

## Ejemplo
~~~css
{{ site.data.CSS.u.unicode-bidi.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.u.unicode-bidi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

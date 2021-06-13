---
title: justify-self
permalink: /CSS/justify-self/
date: 2021-03-07 03:05:18.486004
key: CSS.j.justify-self
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.j.justify-self.description }}

## Sintaxis
~~~css
justify-self : auto | normal | stretch | <baseline-position> | <overflow-position>? [ <self-position> | left | right ]
~~~

## Valores
* **self-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-self valor="self-position" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-self valor="normal" %}
* **overflow-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-self valor="overflow-position" %}
* **baseline-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-self valor="baseline-position" %}
* **left**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-self valor="left" %}
* **right**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-self valor="right" %}
* **stretch**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-self valor="stretch" %}
* **auto**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-self valor="auto" %}

## Ejemplo
~~~css
{{ site.data.CSS.j.justify-self.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.j.justify-self.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

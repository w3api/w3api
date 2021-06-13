---
title: line-break
permalink: /CSS/line-break/
date: 2021-03-07 03:05:38.590276
key: CSS.l.line-break
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.l.line-break.description }}

## Sintaxis
~~~css
line-break : auto | loose | normal | strict | anywhere
~~~

## Valores
* **strict**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.line-break valor="strict" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.line-break valor="normal" %}
* **loose**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.line-break valor="loose" %}
* **anywhere**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.line-break valor="anywhere" %}
* **auto**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.line-break valor="auto" %}

## Ejemplo
~~~css
{{ site.data.CSS.l.line-break.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.l.line-break.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: font-variant-numeric
permalink: /CSS/font-variant-numeric/
date: 2021-03-07 03:03:22.065115
key: CSS.f.font-variant-numeric
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.f.font-variant-numeric.description }}

## Sintaxis
~~~css
font-variant-numeric : normal | [ <numeric-figure-values> || <numeric-spacing-values> || <numeric-fraction-values> || ordinal || slashed-zero ]
~~~

## Valores
* **numeric-spacing-values**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-numeric valor="numeric-spacing-values" %}
* **ordinal**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-numeric valor="ordinal" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-numeric valor="normal" %}
* **numeric-figure-values**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-numeric valor="numeric-figure-values" %}
* **numeric-fraction-values**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-numeric valor="numeric-fraction-values" %}
* **slashed-zero**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-numeric valor="slashed-zero" %}

## Ejemplo
~~~css
{{ site.data.CSS.f.font-variant-numeric.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.f.font-variant-numeric.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

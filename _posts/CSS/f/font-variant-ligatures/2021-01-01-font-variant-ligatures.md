---
title: font-variant-ligatures
permalink: /CSS/font-variant-ligatures/
date: 2021-03-07 03:03:20.221351
key: CSS.f.font-variant-ligatures
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.f.font-variant-ligatures.description }}

## Sintaxis
~~~css
font-variant-ligatures : normal | none | [ <common-lig-values> || <discretionary-lig-values> || <historical-lig-values> || <contextual-alt-values> ]
~~~

## Valores
* **discretionary-lig-values**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-ligatures valor="discretionary-lig-values" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-ligatures valor="none" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-ligatures valor="normal" %}
* **contextual-alt-values**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-ligatures valor="contextual-alt-values" %}
* **common-lig-values**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-ligatures valor="common-lig-values" %}
* **historical-lig-values**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-variant-ligatures valor="historical-lig-values" %}

## Ejemplo
~~~css
{{ site.data.CSS.f.font-variant-ligatures.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.f.font-variant-ligatures.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

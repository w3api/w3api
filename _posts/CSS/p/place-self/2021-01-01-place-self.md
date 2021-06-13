---
title: place-self
permalink: /CSS/place-self/
date: 2021-03-07 03:09:51.214504
key: CSS.p.place-self
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.p.place-self.description }}

## Sintaxis
~~~css
place-self : <'align-self'> <'justify-self'>?
~~~

## Valores
* **justify-self**,  {% include w3api/value_description.html propiedad=site.data.CSS.p.place-self valor="justify-self" %}
* **align-self**,  {% include w3api/value_description.html propiedad=site.data.CSS.p.place-self valor="align-self" %}

## Ejemplo
~~~css
{{ site.data.CSS.p.place-self.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.p.place-self.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

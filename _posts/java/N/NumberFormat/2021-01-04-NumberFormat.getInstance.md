---
title: NumberFormat.getInstance()
permalink: Java/NumberFormat/getInstance
date: 2021-01-04
key: JavaJava.N.NumberFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberFormat.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static NumberFormat getInstance()
public static NumberFormat getInstance(Locale inLocale)
~~~

## Parámetros
* **Locale inLocale**,  {% include w3api/param_description.html metodo=_data parametro="Locale inLocale" %}

## Clase Padre
[NumberFormat](/Java/NumberFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NumberFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

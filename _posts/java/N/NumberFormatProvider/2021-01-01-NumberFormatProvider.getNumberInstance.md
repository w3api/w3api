---
title: NumberFormatProvider.getNumberInstance()
permalink: /Java/NumberFormatProvider/getNumberInstance/
date: 2021-01-11
key: Java.N.NumberFormatProvider
category: Java
tags: ['java se', 'java.text.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberFormatProvider.metodos valor="getNumberInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract NumberFormat getNumberInstance(Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NumberFormatProvider](/Java/NumberFormatProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

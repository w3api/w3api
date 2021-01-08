---
title: NumberFormatProvider.getCurrencyInstance()
permalink: Java/NumberFormatProvider/getCurrencyInstance
date: 2021-01-04
key: JavaJava.N.NumberFormatProvider
category: java
tags: ['java se', 'java.text.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberFormatProvider.metodos valor="getCurrencyInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract NumberFormat getCurrencyInstance(Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NumberFormatProvider](/Java/NumberFormatProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NumberFormatProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

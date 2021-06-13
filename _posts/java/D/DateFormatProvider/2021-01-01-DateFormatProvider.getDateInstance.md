---
title: DateFormatProvider.getDateInstance()
permalink: /Java/DateFormatProvider/getDateInstance/
date: 2021-01-11
key: Java.D.DateFormatProvider
category: Java
tags: ['java se', 'java.text.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateFormatProvider.metodos valor="getDateInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract DateFormat getDateInstance(int style, Locale locale)
~~~

## Parámetros
* **int style**,  {% include w3api/param_description.html metodo=_dato parametro="int style" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DateFormatProvider](/Java/DateFormatProvider/)

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

---
title: Formattable.formatTo()
permalink: Java/Formattable/formatTo
date: 2021-01-04
key: JavaJava.F.Formattable
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.Formattable.metodos valor="formatTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void formatTo(Formatter formatter, int flags, int width, int precision)
~~~

## Parámetros
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **int flags**,  {% include w3api/param_description.html metodo=_data parametro="int flags" %}
* **Formatter formatter**,  {% include w3api/param_description.html metodo=_data parametro="Formatter formatter" %}
* **int precision**,  {% include w3api/param_description.html metodo=_data parametro="int precision" %}

## Excepciones
[IllegalFormatException](/Java/IllegalFormatException/)

## Clase Padre
[Formattable](/Java/Formattable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.Formattable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

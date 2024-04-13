---
title: Formattable.formatTo()
permalink: /Java/Formattable/formatTo/
date: 2021-01-11
key: Java.F.Formattable
category: Java
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
* **int flags**,  {% include w3api/param_description.html metodo=_dato parametro="int flags" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **int precision**,  {% include w3api/param_description.html metodo=_dato parametro="int precision" %}
* **Formatter formatter**,  {% include w3api/param_description.html metodo=_dato parametro="Formatter formatter" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

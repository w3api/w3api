---
title: CharSequence.charAt()
permalink: Java/CharSequence/charAt
date: 2021-01-11
key: JavaJava.C.CharSequence
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharSequence.metodos valor="charAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
char charAt(int index)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[CharSequence](/Java/CharSequence/)

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

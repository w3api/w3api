---
title: StringBuilder.substring()
permalink: Java/StringBuilder/substring
date: 2021-01-11
key: JavaJava.S.StringBuilder
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuilder.metodos valor="substring" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String substring(int start)
public String substring(int start, int end)
~~~

## Parámetros
* **int end**,  {% include w3api/param_description.html metodo=_dato parametro="int end" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}

## Excepciones
[StringIndexOutOfBoundsException](/Java/StringIndexOutOfBoundsException/)

## Clase Padre
[StringBuilder](/Java/StringBuilder/)

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

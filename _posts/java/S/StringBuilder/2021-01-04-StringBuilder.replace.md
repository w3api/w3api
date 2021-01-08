---
title: StringBuilder.replace()
permalink: Java/StringBuilder/replace
date: 2021-01-04
key: JavaJava.S.StringBuilder
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuilder.metodos valor="replace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringBuilder replace(int start, int end, String str)
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **String str**,  {% include w3api/param_description.html metodo=_data parametro="String str" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}

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
{%- for _ldc in site.data.Java.S.StringBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

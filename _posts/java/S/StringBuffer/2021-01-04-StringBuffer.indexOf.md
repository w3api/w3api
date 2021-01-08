---
title: StringBuffer.indexOf()
permalink: Java/StringBuffer/indexOf
date: 2021-01-04
key: JavaJava.S.StringBuffer
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuffer.metodos valor="indexOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int indexOf(String str)
public int indexOf(String str, int fromIndex)
~~~

## Parámetros
* **String str**,  {% include w3api/param_description.html metodo=_data parametro="String str" %}
* **int fromIndex**,  {% include w3api/param_description.html metodo=_data parametro="int fromIndex" %}

## Clase Padre
[StringBuffer](/Java/StringBuffer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringBuffer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

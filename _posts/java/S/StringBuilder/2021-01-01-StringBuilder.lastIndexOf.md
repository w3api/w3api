---
title: StringBuilder.lastIndexOf()
permalink: /Java/StringBuilder/lastIndexOf/
date: 2021-01-11
key: Java.S.StringBuilder
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuilder.metodos valor="lastIndexOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int lastIndexOf(String str)
public int lastIndexOf(String str, int fromIndex)
~~~

## Parámetros
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **int fromIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int fromIndex" %}

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

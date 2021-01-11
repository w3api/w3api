---
title: URLConnection.getHeaderFieldInt()
permalink: Java/URLConnection/getHeaderFieldInt
date: 2021-01-11
key: JavaJava.U.URLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="getHeaderFieldInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getHeaderFieldInt(String name, int Default)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **int Default**,  {% include w3api/param_description.html metodo=_dato parametro="int Default" %}

## Clase Padre
[URLConnection](/Java/URLConnection/)

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

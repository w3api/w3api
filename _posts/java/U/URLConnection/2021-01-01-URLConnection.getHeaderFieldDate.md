---
title: URLConnection.getHeaderFieldDate()
permalink: Java/URLConnection/getHeaderFieldDate
date: 2021-01-11
key: JavaJava.U.URLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="getHeaderFieldDate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long getHeaderFieldDate(String name, long Default)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **long Default**,  {% include w3api/param_description.html metodo=_dato parametro="long Default" %}

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

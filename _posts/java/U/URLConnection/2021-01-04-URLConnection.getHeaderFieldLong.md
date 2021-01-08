---
title: URLConnection.getHeaderFieldLong()
permalink: Java/URLConnection/getHeaderFieldLong
date: 2021-01-04
key: JavaJava.U.URLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="getHeaderFieldLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long getHeaderFieldLong(String name, long Default)
~~~

## Parámetros
* **long Default**,  {% include w3api/param_description.html metodo=_data parametro="long Default" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[URLConnection](/Java/URLConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.URLConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

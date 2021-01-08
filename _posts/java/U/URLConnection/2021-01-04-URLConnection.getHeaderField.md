---
title: URLConnection.getHeaderField()
permalink: Java/URLConnection/getHeaderField
date: 2021-01-04
key: JavaJava.U.URLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="getHeaderField" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getHeaderField(int n)
public String getHeaderField(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **int n**,  {% include w3api/param_description.html metodo=_data parametro="int n" %}

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

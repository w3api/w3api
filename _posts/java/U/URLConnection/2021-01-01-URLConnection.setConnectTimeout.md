---
title: URLConnection.setConnectTimeout()
permalink: /Java/URLConnection/setConnectTimeout/
date: 2021-01-11
key: Java.U.URLConnection
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="setConnectTimeout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setConnectTimeout(int timeout)
~~~

## Parámetros
* **int timeout**,  {% include w3api/param_description.html metodo=_dato parametro="int timeout" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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

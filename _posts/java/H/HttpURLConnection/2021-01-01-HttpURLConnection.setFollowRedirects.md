---
title: HttpURLConnection.setFollowRedirects()
permalink: /Java/HttpURLConnection/setFollowRedirects/
date: 2021-01-11
key: Java.H.HttpURLConnection
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpURLConnection.metodos valor="setFollowRedirects" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setFollowRedirects(boolean set)
~~~

## Parámetros
* **boolean set**,  {% include w3api/param_description.html metodo=_dato parametro="boolean set" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[HttpURLConnection](/Java/HttpURLConnection/)

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

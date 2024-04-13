---
title: HttpURLConnection.setRequestMethod()
permalink: /Java/HttpURLConnection/setRequestMethod/
date: 2021-01-11
key: Java.H.HttpURLConnection
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpURLConnection.metodos valor="setRequestMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setRequestMethod(String method) throws ProtocolException
~~~

## Parámetros
* **String method**,  {% include w3api/param_description.html metodo=_dato parametro="String method" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [ProtocolException](/Java/ProtocolException/)

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

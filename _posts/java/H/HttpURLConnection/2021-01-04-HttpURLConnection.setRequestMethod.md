---
title: HttpURLConnection.setRequestMethod()
permalink: Java/HttpURLConnection/setRequestMethod
date: 2021-01-04
key: JavaJava.H.HttpURLConnection
category: java
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
* **String method**,  {% include w3api/param_description.html metodo=_data parametro="String method" %}

## Excepciones
[ProtocolException](/Java/ProtocolException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[HttpURLConnection](/Java/HttpURLConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpURLConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

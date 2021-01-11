---
title: HttpURLConnection.setFixedLengthStreamingMode()
permalink: Java/HttpURLConnection/setFixedLengthStreamingMode
date: 2021-01-11
key: JavaJava.H.HttpURLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpURLConnection.metodos valor="setFixedLengthStreamingMode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFixedLengthStreamingMode(int contentLength)
public void setFixedLengthStreamingMode(long contentLength)
~~~

## Parámetros
* **int contentLength**,  {% include w3api/param_description.html metodo=_dato parametro="int contentLength" %}
* **long contentLength**,  {% include w3api/param_description.html metodo=_dato parametro="long contentLength" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

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

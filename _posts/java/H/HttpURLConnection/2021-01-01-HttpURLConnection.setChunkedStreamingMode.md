---
title: HttpURLConnection.setChunkedStreamingMode()
permalink: /Java/HttpURLConnection/setChunkedStreamingMode/
date: 2021-01-11
key: Java.H.HttpURLConnection
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpURLConnection.metodos valor="setChunkedStreamingMode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setChunkedStreamingMode(int chunklen)
~~~

## Parámetros
* **int chunklen**,  {% include w3api/param_description.html metodo=_dato parametro="int chunklen" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

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

---
title: HttpsURLConnection.setDefaultSSLSocketFactory()
permalink: Java/HttpsURLConnection/setDefaultSSLSocketFactory
date: 2021-01-04
key: JavaJava.H.HttpsURLConnection
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpsURLConnection.metodos valor="setDefaultSSLSocketFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setDefaultSSLSocketFactory(SSLSocketFactory sf)
~~~

## Parámetros
* **SSLSocketFactory sf**,  {% include w3api/param_description.html metodo=_data parametro="SSLSocketFactory sf" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HttpsURLConnection](/Java/HttpsURLConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpsURLConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

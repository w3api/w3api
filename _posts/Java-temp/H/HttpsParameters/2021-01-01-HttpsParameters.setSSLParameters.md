---
title: HttpsParameters.setSSLParameters()
permalink: /Java/HttpsParameters/setSSLParameters/
date: 2021-01-11
key: Java.H.HttpsParameters
category: Java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpsParameters.metodos valor="setSSLParameters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setSSLParameters(SSLParameters params)
~~~

## Parámetros
* **SSLParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="SSLParameters params" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HttpsParameters](/Java/HttpsParameters/)

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

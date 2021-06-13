---
title: HttpsURLConnection.setHostnameVerifier()
permalink: /Java/HttpsURLConnection/setHostnameVerifier/
date: 2021-01-11
key: Java.H.HttpsURLConnection
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpsURLConnection.metodos valor="setHostnameVerifier" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setHostnameVerifier(HostnameVerifier v)
~~~

## Parámetros
* **HostnameVerifier v**,  {% include w3api/param_description.html metodo=_dato parametro="HostnameVerifier v" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HttpsURLConnection](/Java/HttpsURLConnection/)

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

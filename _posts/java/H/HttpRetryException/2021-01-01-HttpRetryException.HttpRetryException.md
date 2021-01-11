---
title: HttpRetryException.HttpRetryException()
permalink: Java/HttpRetryException/HttpRetryException
date: 2021-01-11
key: JavaJava.H.HttpRetryException
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRetryException.constructores valor="HttpRetryException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HttpRetryException(String detail, int code)
public HttpRetryException(String detail, int code, String location)
~~~

## Parámetros
* **String location**,  {% include w3api/param_description.html metodo=_dato parametro="String location" %}
* **String detail**,  {% include w3api/param_description.html metodo=_dato parametro="String detail" %}
* **int code**,  {% include w3api/param_description.html metodo=_dato parametro="int code" %}

## Clase Padre
[HttpRetryException](/Java/HttpRetryException/)

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

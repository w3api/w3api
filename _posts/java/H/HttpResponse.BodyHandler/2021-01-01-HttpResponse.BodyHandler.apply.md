---
title: HttpResponse.BodyHandler.apply()
permalink: /Java/HttpResponse/BodyHandler/apply/
date: 2021-01-11
key: Java.H.HttpResponse.BodyHandler
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodyHandler.metodos valor="apply" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
HttpResponse.BodySubscriber<T> apply(int statusCode, HttpHeaders responseHeaders)
~~~

## Parámetros
* **HttpHeaders responseHeaders**,  {% include w3api/param_description.html metodo=_dato parametro="HttpHeaders responseHeaders" %}
* **int statusCode**,  {% include w3api/param_description.html metodo=_dato parametro="int statusCode" %}

## Clase Padre
[HttpResponse.BodyHandler](/Java/HttpResponse/BodyHandler/)

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

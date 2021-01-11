---
title: HttpRequest.Builder.method()
permalink: Java/HttpRequest/Builder/method
date: 2021-01-11
key: JavaJava.H.HttpRequest.Builder
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.Builder.metodos valor="method" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract HttpRequest.Builder method(String method, HttpRequest.BodyPublisher bodyPublisher)
~~~

## Parámetros
* **String method**,  {% include w3api/param_description.html metodo=_dato parametro="String method" %}
* **HttpRequest.BodyPublisher bodyPublisher**,  {% include w3api/param_description.html metodo=_dato parametro="HttpRequest.BodyPublisher bodyPublisher" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HttpRequest.Builder](/Java/HttpRequest/Builder/)

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

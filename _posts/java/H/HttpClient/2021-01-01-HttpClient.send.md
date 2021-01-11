---
title: HttpClient.send()
permalink: Java/HttpClient/send
date: 2021-01-11
key: JavaJava.H.HttpClient
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpClient.metodos valor="send" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> HttpResponse<T> send(HttpRequest req, HttpResponse.BodyHandler<T> responseBodyHandler)
~~~

## Parámetros
* **HttpResponse.BodyHandler&lt;T&gt; responseBodyHandler**,  {% include w3api/param_description.html metodo=_dato parametro="HttpResponse.BodyHandler<T> responseBodyHandler" %}
* **HttpRequest req**,  {% include w3api/param_description.html metodo=_dato parametro="HttpRequest req" %}

## Clase Padre
[HttpClient](/Java/HttpClient/)

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

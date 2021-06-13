---
title: HttpClient.sendAsync()
permalink: /Java/HttpClient/sendAsync/
date: 2021-01-11
key: Java.H.HttpClient
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpClient.metodos valor="sendAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> CompletableFuture<HttpResponse<T>> sendAsync(HttpRequest req, HttpResponse.BodyHandler<T> responseBodyHandler)
abstract <U,T> CompletableFuture<U> sendAsync(HttpRequest req, HttpResponse.MultiSubscriber<U,T> multiSubscriber)
~~~

## Parámetros
* **HttpResponse.BodyHandler&lt;T&gt; responseBodyHandler**,  {% include w3api/param_description.html metodo=_dato parametro="HttpResponse.BodyHandler<T> responseBodyHandler" %}
* **HttpRequest req**,  {% include w3api/param_description.html metodo=_dato parametro="HttpRequest req" %}
* **T&gt; multiSubscriber**,  {% include w3api/param_description.html metodo=_dato parametro="T> multiSubscriber" %}
* **HttpResponse.MultiSubscriber&lt;U**,  {% include w3api/param_description.html metodo=_dato parametro="HttpResponse.MultiSubscriber<U" %}

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

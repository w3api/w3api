---
title: HttpResponse.MultiSubscriber.onRequest()
permalink: Java/HttpResponse/MultiSubscriber/onRequest
date: 2021-01-11
key: JavaJava.H.HttpResponse.MultiSubscriber
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.MultiSubscriber.metodos valor="onRequest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
HttpResponse.BodyHandler<T> onRequest(HttpRequest request)
~~~

## Parámetros
* **HttpRequest request**,  {% include w3api/param_description.html metodo=_dato parametro="HttpRequest request" %}

## Clase Padre
[HttpResponse.MultiSubscriber](/Java/HttpResponse/MultiSubscriber/)

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

---
title: HttpResponse.MultiSubscriber.onPushPromise()
permalink: /Java/HttpResponse/MultiSubscriber/onPushPromise/
date: 2021-01-11
key: Java.H.HttpResponse.MultiSubscriber
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.MultiSubscriber.metodos valor="onPushPromise" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Optional<HttpResponse.BodyHandler<T>> onPushPromise(HttpRequest pushPromise)
~~~

## Parámetros
* **HttpRequest pushPromise**,  {% include w3api/param_description.html metodo=_dato parametro="HttpRequest pushPromise" %}

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

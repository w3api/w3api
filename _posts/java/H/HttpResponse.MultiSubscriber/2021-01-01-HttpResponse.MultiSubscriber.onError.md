---
title: HttpResponse.MultiSubscriber.onError()
permalink: Java/HttpResponse/MultiSubscriber/onError
date: 2021-01-11
key: JavaJava.H.HttpResponse.MultiSubscriber
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.MultiSubscriber.metodos valor="onError" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void onError(HttpRequest request, Throwable t)
~~~

## Parámetros
* **Throwable t**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable t" %}
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

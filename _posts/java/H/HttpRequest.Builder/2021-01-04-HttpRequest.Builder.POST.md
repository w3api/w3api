---
title: HttpRequest.Builder.POST()
permalink: Java/HttpRequest/Builder/POST
date: 2021-01-04
key: JavaJava.H.HttpRequest.Builder
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.Builder.metodos valor="POST" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract HttpRequest.Builder POST(HttpRequest.BodyPublisher bodyPublisher)
~~~

## Parámetros
* **HttpRequest.BodyPublisher bodyPublisher**,  {% include w3api/param_description.html metodo=_data parametro="HttpRequest.BodyPublisher bodyPublisher" %}

## Clase Padre
[HttpRequest.Builder](/Java/HttpRequest/Builder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpRequest.Builder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

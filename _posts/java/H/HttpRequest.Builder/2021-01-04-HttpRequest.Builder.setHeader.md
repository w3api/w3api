---
title: HttpRequest.Builder.setHeader()
permalink: Java/HttpRequest/Builder/setHeader
date: 2021-01-04
key: JavaJava.H.HttpRequest.Builder
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.Builder.metodos valor="setHeader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract HttpRequest.Builder setHeader(String name, String value)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String value**,  {% include w3api/param_description.html metodo=_data parametro="String value" %}

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
{%- for _ldc in site.data.Java.H.HttpRequest.Builder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

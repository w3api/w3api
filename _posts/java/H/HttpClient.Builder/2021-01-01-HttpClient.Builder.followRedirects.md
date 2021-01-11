---
title: HttpClient.Builder.followRedirects()
permalink: Java/HttpClient/Builder/followRedirects
date: 2021-01-11
key: JavaJava.H.HttpClient.Builder
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpClient.Builder.metodos valor="followRedirects" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract HttpClient.Builder followRedirects(HttpClient.Redirect policy)
~~~

## Parámetros
* **HttpClient.Redirect policy**,  {% include w3api/param_description.html metodo=_dato parametro="HttpClient.Redirect policy" %}

## Clase Padre
[HttpClient.Builder](/Java/HttpClient/Builder/)

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

---
title: HttpClient.Redirect
permalink: /Java/HttpClient/Redirect/
date: 2021-01-11
key: Java.H.HttpClient.Redirect
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'enumerado java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpClient.Redirect.description }}

## Sintaxis
~~~java
public static enum HttpClient.Redirect extends Enum<HttpClient.Redirect>
~~~

## Enumerados
* [ALWAYS](/Java/HttpClient/Redirect/ALWAYS)
* [NEVER](/Java/HttpClient/Redirect/NEVER)
* [SAME_PROTOCOL](/Java/HttpClient/Redirect/SAME_PROTOCOL)
* [SECURE](/Java/HttpClient/Redirect/SECURE)

## Métodos
* [valueOf()](/Java/HttpClient/Redirect/valueOf)
* [values()](/Java/HttpClient/Redirect/values)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpClient.Redirect.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpClient.Redirect.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

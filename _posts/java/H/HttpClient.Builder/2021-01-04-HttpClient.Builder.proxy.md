---
title: HttpClient.Builder.proxy()
permalink: Java/HttpClient/Builder/proxy
date: 2021-01-04
key: JavaJava.H.HttpClient.Builder
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpClient.Builder.metodos valor="proxy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract HttpClient.Builder proxy(ProxySelector selector)
~~~

## Parámetros
* **ProxySelector selector**,  {% include w3api/param_description.html metodo=_data parametro="ProxySelector selector" %}

## Clase Padre
[HttpClient.Builder](/Java/HttpClient/Builder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpClient.Builder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

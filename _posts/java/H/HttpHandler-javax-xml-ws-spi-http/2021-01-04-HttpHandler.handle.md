---
title: HttpHandler.handle()
permalink: Java/HttpHandler-javax-xml-ws-spi-http/handle
date: 2021-01-04
key: JavaJava.H.HttpHandler-javax-xml-ws-spi-http
category: java
tags: ['java se', 'javax.xml.ws.spi.http', 'java.xml.ws', 'metodo java', 'Java 1.7', 'JAX-WS 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpHandler-javax-xml-ws-spi-http.metodos valor="handle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void handle(HttpExchange exchange) throws IOException
~~~

## Parámetros
* **HttpExchange exchange**,  {% include w3api/param_description.html metodo=_data parametro="HttpExchange exchange" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[HttpHandler](/Java/HttpHandler-javax-xml-ws-spi-http/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpHandler-javax-xml-ws-spi-http.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

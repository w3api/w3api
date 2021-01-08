---
title: WebSocket.Builder.subprotocols()
permalink: Java/WebSocket/Builder/subprotocols
date: 2021-01-04
key: JavaJava.W.WebSocket.Builder
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebSocket.Builder.metodos valor="subprotocols" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
WebSocket.Builder subprotocols(String mostPreferred, String... lesserPreferred)
~~~

## Parámetros
* **String mostPreferred**,  {% include w3api/param_description.html metodo=_data parametro="String mostPreferred" %}
* **String... lesserPreferred**,  {% include w3api/param_description.html metodo=_data parametro="String... lesserPreferred" %}

## Clase Padre
[WebSocket.Builder](/Java/WebSocket/Builder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebSocket.Builder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

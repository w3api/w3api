---
title: SocketHandler.SocketHandler()
permalink: Java/SocketHandler/SocketHandler
date: 2021-01-04
key: JavaJava.S.SocketHandler
category: java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketHandler.constructores valor="SocketHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SocketHandler() throws IOException
public SocketHandler(String host, int port) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **String host**,  {% include w3api/param_description.html metodo=_data parametro="String host" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SocketHandler](/Java/SocketHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SocketHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

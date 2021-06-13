---
title: TransportService.attach()
permalink: /Java/TransportService/attach/
date: 2021-01-11
key: Java.T.TransportService
category: Java
tags: ['java se', 'com.sun.jdi.connect.spi', 'jdk.jdi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransportService.metodos valor="attach" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Connection attach(String address, long attachTimeout, long handshakeTimeout) throws IOException
~~~

## Parámetros
* **long attachTimeout**,  {% include w3api/param_description.html metodo=_dato parametro="long attachTimeout" %}
* **long handshakeTimeout**,  {% include w3api/param_description.html metodo=_dato parametro="long handshakeTimeout" %}
* **String address**,  {% include w3api/param_description.html metodo=_dato parametro="String address" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [TransportTimeoutException](/Java/TransportTimeoutException/)

## Clase Padre
[TransportService](/Java/TransportService/)

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

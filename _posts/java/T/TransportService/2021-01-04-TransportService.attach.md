---
title: TransportService.attach()
permalink: Java/TransportService/attach
date: 2021-01-04
key: JavaJava.T.TransportService
category: java
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
* **long handshakeTimeout**,  {% include w3api/param_description.html metodo=_data parametro="long handshakeTimeout" %}
* **long attachTimeout**,  {% include w3api/param_description.html metodo=_data parametro="long attachTimeout" %}
* **String address**,  {% include w3api/param_description.html metodo=_data parametro="String address" %}

## Excepciones
[TransportTimeoutException](/Java/TransportTimeoutException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[TransportService](/Java/TransportService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransportService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: TransportService.accept()
permalink: Java/TransportService/accept
date: 2021-01-04
key: JavaJava.T.TransportService
category: java
tags: ['java se', 'com.sun.jdi.connect.spi', 'jdk.jdi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransportService.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Connection accept(TransportService.ListenKey listenKey, long acceptTimeout, long handshakeTimeout) throws IOException
~~~

## Parámetros
* **long acceptTimeout**,  {% include w3api/param_description.html metodo=_data parametro="long acceptTimeout" %}
* **TransportService.ListenKey listenKey**,  {% include w3api/param_description.html metodo=_data parametro="TransportService.ListenKey listenKey" %}
* **long handshakeTimeout**,  {% include w3api/param_description.html metodo=_data parametro="long handshakeTimeout" %}

## Excepciones
[TransportTimeoutException](/Java/TransportTimeoutException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

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

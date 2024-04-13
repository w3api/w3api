---
title: TransportService.accept()
permalink: /Java/TransportService/accept/
date: 2021-01-11
key: Java.T.TransportService
category: Java
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
* **long handshakeTimeout**,  {% include w3api/param_description.html metodo=_dato parametro="long handshakeTimeout" %}
* **long acceptTimeout**,  {% include w3api/param_description.html metodo=_dato parametro="long acceptTimeout" %}
* **TransportService.ListenKey listenKey**,  {% include w3api/param_description.html metodo=_dato parametro="TransportService.ListenKey listenKey" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [TransportTimeoutException](/Java/TransportTimeoutException/)

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

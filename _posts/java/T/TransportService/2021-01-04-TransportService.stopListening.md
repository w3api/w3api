---
title: TransportService.stopListening()
permalink: Java/TransportService/stopListening
date: 2021-01-04
key: JavaJava.T.TransportService
category: java
tags: ['java se', 'com.sun.jdi.connect.spi', 'jdk.jdi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransportService.metodos valor="stopListening" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void stopListening(TransportService.ListenKey listenKey) throws IOException
~~~

## Parámetros
* **TransportService.ListenKey listenKey**,  {% include w3api/param_description.html metodo=_data parametro="TransportService.ListenKey listenKey" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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

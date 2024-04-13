---
title: TransportService.startListening()
permalink: /Java/TransportService/startListening/
date: 2021-01-11
key: Java.T.TransportService
category: Java
tags: ['java se', 'com.sun.jdi.connect.spi', 'jdk.jdi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransportService.metodos valor="startListening" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract TransportService.ListenKey startListening() throws IOException
public abstract TransportService.ListenKey startListening(String address) throws IOException
~~~

## Parámetros
* **String address**,  {% include w3api/param_description.html metodo=_dato parametro="String address" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

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

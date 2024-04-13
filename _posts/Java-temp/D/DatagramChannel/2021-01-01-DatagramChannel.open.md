---
title: DatagramChannel.open()
permalink: /Java/DatagramChannel/open/
date: 2021-01-11
key: Java.D.DatagramChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramChannel.metodos valor="open" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DatagramChannel open() throws IOException
public static DatagramChannel open(ProtocolFamily family) throws IOException
~~~

## Parámetros
* **ProtocolFamily family**,  {% include w3api/param_description.html metodo=_dato parametro="ProtocolFamily family" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[DatagramChannel](/Java/DatagramChannel/)

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

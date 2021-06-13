---
title: Connection.readPacket()
permalink: /Java/Connection-com-sun-jdi-connect-spi/readPacket/
date: 2021-01-11
key: Java.C.Connection-com-sun-jdi-connect-spi
category: Java
tags: ['java se', 'com.sun.jdi.connect.spi', 'jdk.jdi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-com-sun-jdi-connect-spi.metodos valor="readPacket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract byte[] readPacket() throws IOException
~~~

## Excepciones
[ClosedConnectionException](/Java/ClosedConnectionException/), [IOException](/Java/IOException/)

## Clase Padre
[Connection](/Java/Connection-com-sun-jdi-connect-spi/)

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

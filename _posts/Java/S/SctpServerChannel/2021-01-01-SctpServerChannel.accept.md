---
title: SctpServerChannel.accept()
permalink: /Java/SctpServerChannel/accept/
date: 2021-01-11
key: Java.S.SctpServerChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpServerChannel.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SctpChannel accept() throws IOException
~~~

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [NotYetBoundException](/Java/NotYetBoundException/), [SecurityException](/Java/SecurityException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

## Clase Padre
[SctpServerChannel](/Java/SctpServerChannel/)

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

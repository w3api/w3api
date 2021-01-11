---
title: SelectorProvider.openDatagramChannel()
permalink: Java/SelectorProvider/openDatagramChannel
date: 2021-01-11
key: JavaJava.S.SelectorProvider
category: java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SelectorProvider.metodos valor="openDatagramChannel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract DatagramChannel openDatagramChannel() throws IOException
public abstract DatagramChannel openDatagramChannel(ProtocolFamily family) throws IOException
~~~

## Parámetros
* **ProtocolFamily family**,  {% include w3api/param_description.html metodo=_dato parametro="ProtocolFamily family" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[SelectorProvider](/Java/SelectorProvider/)

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

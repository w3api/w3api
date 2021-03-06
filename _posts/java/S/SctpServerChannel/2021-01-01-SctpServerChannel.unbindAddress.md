---
title: SctpServerChannel.unbindAddress()
permalink: /Java/SctpServerChannel/unbindAddress/
date: 2021-01-11
key: Java.S.SctpServerChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpServerChannel.metodos valor="unbindAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SctpServerChannel unbindAddress(InetAddress address) throws IOException
~~~

## Parámetros
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}

## Excepciones
[IllegalUnbindException](/Java/IllegalUnbindException/), [ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [NotYetBoundException](/Java/NotYetBoundException/)

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

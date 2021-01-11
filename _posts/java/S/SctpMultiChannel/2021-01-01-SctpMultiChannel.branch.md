---
title: SctpMultiChannel.branch()
permalink: Java/SctpMultiChannel/branch
date: 2021-01-11
key: JavaJava.S.SctpMultiChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpMultiChannel.metodos valor="branch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SctpChannel branch(Association association) throws IOException
~~~

## Parámetros
* **Association association**,  {% include w3api/param_description.html metodo=_dato parametro="Association association" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[SctpMultiChannel](/Java/SctpMultiChannel/)

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

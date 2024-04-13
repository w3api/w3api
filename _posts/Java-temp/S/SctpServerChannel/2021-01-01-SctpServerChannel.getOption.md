---
title: SctpServerChannel.getOption()
permalink: /Java/SctpServerChannel/getOption/
date: 2021-01-11
key: Java.S.SctpServerChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpServerChannel.metodos valor="getOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> T getOption(SctpSocketOption<T> name)
~~~

## Parámetros
* **SctpSocketOption&lt;T&gt; name**,  {% include w3api/param_description.html metodo=_dato parametro="SctpSocketOption<T> name" %}

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

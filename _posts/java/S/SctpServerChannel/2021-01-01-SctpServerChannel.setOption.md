---
title: SctpServerChannel.setOption()
permalink: Java/SctpServerChannel/setOption
date: 2021-01-11
key: JavaJava.S.SctpServerChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpServerChannel.metodos valor="setOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> SctpServerChannel setOption(SctpSocketOption<T> name, T value)
~~~

## Parámetros
* **SctpSocketOption&lt;T&gt; name**,  {% include w3api/param_description.html metodo=_dato parametro="SctpSocketOption<T> name" %}
* **T value**,  {% include w3api/param_description.html metodo=_dato parametro="T value" %}

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

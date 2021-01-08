---
title: DatagramChannel.setOption()
permalink: Java/DatagramChannel/setOption
date: 2021-01-04
key: JavaJava.D.DatagramChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramChannel.metodos valor="setOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> DatagramChannel setOption(SocketOption<T> name, T value)
~~~

## Parámetros
* **T value**,  {% include w3api/param_description.html metodo=_data parametro="T value" %}
* **SocketOption&lt;T&gt; name**,  {% include w3api/param_description.html metodo=_data parametro="SocketOption<T> name" %}

## Clase Padre
[DatagramChannel](/Java/DatagramChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatagramChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

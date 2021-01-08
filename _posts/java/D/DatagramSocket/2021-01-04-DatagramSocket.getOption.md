---
title: DatagramSocket.getOption()
permalink: Java/DatagramSocket/getOption
date: 2021-01-04
key: JavaJava.D.DatagramSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocket.metodos valor="getOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T getOption(SocketOption<T> name)
~~~

## Parámetros
* **SocketOption&lt;T&gt; name**,  {% include w3api/param_description.html metodo=_data parametro="SocketOption<T> name" %}

## Clase Padre
[DatagramSocket](/Java/DatagramSocket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatagramSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: NetworkChannel.getOption()
permalink: Java/NetworkChannel/getOption
date: 2021-01-04
key: JavaJava.N.NetworkChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NetworkChannel.metodos valor="getOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T getOption(SocketOption<T> name)
~~~

## Parámetros
* **SocketOption&lt;T&gt; name**,  {% include w3api/param_description.html metodo=_data parametro="SocketOption<T> name" %}

## Clase Padre
[NetworkChannel](/Java/NetworkChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NetworkChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

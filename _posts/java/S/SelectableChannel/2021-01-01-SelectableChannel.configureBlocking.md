---
title: SelectableChannel.configureBlocking()
permalink: Java/SelectableChannel/configureBlocking
date: 2021-01-11
key: JavaJava.S.SelectableChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SelectableChannel.metodos valor="configureBlocking" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SelectableChannel configureBlocking(boolean block) throws IOException
~~~

## Parámetros
* **boolean block**,  {% include w3api/param_description.html metodo=_dato parametro="boolean block" %}

## Excepciones
[IllegalBlockingModeException](/Java/IllegalBlockingModeException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[SelectableChannel](/Java/SelectableChannel/)

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

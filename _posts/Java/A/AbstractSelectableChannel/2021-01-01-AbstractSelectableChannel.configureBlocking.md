---
title: AbstractSelectableChannel.configureBlocking()
permalink: /Java/AbstractSelectableChannel/configureBlocking/
date: 2021-01-11
key: Java.A.AbstractSelectableChannel
category: Java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractSelectableChannel.metodos valor="configureBlocking" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final SelectableChannel configureBlocking(boolean block) throws IOException
~~~

## Parámetros
* **boolean block**,  {% include w3api/param_description.html metodo=_dato parametro="boolean block" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[AbstractSelectableChannel](/Java/AbstractSelectableChannel/)

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

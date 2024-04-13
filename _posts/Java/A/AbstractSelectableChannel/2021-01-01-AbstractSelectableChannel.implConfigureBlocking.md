---
title: AbstractSelectableChannel.implConfigureBlocking()
permalink: /Java/AbstractSelectableChannel/implConfigureBlocking/
date: 2021-01-11
key: Java.A.AbstractSelectableChannel
category: Java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractSelectableChannel.metodos valor="implConfigureBlocking" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void implConfigureBlocking(boolean block) throws IOException
~~~

## Parámetros
* **boolean block**,  {% include w3api/param_description.html metodo=_dato parametro="boolean block" %}

## Excepciones
[IOException](/Java/IOException/)

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

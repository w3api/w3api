---
title: AbstractSelectableChannel.register()
permalink: Java/AbstractSelectableChannel/register
date: 2021-01-04
key: JavaJava.A.AbstractSelectableChannel
category: java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractSelectableChannel.metodos valor="register" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final SelectionKey register(Selector sel, int ops, Object att) throws ClosedChannelException
~~~

## Parámetros
* **int ops**,  {% include w3api/param_description.html metodo=_data parametro="int ops" %}
* **Selector sel**,  {% include w3api/param_description.html metodo=_data parametro="Selector sel" %}
* **Object att**,  {% include w3api/param_description.html metodo=_data parametro="Object att" %}

## Excepciones
[IllegalBlockingModeException](/Java/IllegalBlockingModeException/), [CancelledKeyException](/Java/CancelledKeyException/), [IllegalSelectorException](/Java/IllegalSelectorException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [ClosedChannelException](/Java/ClosedChannelException/), [ClosedSelectorException](/Java/ClosedSelectorException/)

## Clase Padre
[AbstractSelectableChannel](/Java/AbstractSelectableChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractSelectableChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

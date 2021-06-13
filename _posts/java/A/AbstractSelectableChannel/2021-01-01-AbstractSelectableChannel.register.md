---
title: AbstractSelectableChannel.register()
permalink: /Java/AbstractSelectableChannel/register/
date: 2021-01-11
key: Java.A.AbstractSelectableChannel
category: Java
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
* **Object att**,  {% include w3api/param_description.html metodo=_dato parametro="Object att" %}
* **int ops**,  {% include w3api/param_description.html metodo=_dato parametro="int ops" %}
* **Selector sel**,  {% include w3api/param_description.html metodo=_dato parametro="Selector sel" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalBlockingModeException](/Java/IllegalBlockingModeException/), [IllegalSelectorException](/Java/IllegalSelectorException/), [CancelledKeyException](/Java/CancelledKeyException/), [ClosedSelectorException](/Java/ClosedSelectorException/)

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

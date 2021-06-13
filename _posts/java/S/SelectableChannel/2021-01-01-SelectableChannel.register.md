---
title: SelectableChannel.register()
permalink: /Java/SelectableChannel/register/
date: 2021-01-11
key: Java.S.SelectableChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SelectableChannel.metodos valor="register" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final SelectionKey register(Selector sel, int ops) throws ClosedChannelException
public abstract SelectionKey register(Selector sel, int ops, Object att) throws ClosedChannelException
~~~

## Parámetros
* **Object att**,  {% include w3api/param_description.html metodo=_dato parametro="Object att" %}
* **int ops**,  {% include w3api/param_description.html metodo=_dato parametro="int ops" %}
* **Selector sel**,  {% include w3api/param_description.html metodo=_dato parametro="Selector sel" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalBlockingModeException](/Java/IllegalBlockingModeException/), [IllegalSelectorException](/Java/IllegalSelectorException/), [CancelledKeyException](/Java/CancelledKeyException/), [ClosedSelectorException](/Java/ClosedSelectorException/)

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

---
title: SelectableChannel.keyFor()
permalink: /Java/SelectableChannel/keyFor/
date: 2021-01-11
key: Java.S.SelectableChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SelectableChannel.metodos valor="keyFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SelectionKey keyFor(Selector sel)
~~~

## Parámetros
* **Selector sel**,  {% include w3api/param_description.html metodo=_dato parametro="Selector sel" %}

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

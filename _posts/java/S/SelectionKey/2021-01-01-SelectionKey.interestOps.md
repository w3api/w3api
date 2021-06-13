---
title: SelectionKey.interestOps()
permalink: /Java/SelectionKey/interestOps/
date: 2021-01-11
key: Java.S.SelectionKey
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SelectionKey.metodos valor="interestOps" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int interestOps()
public abstract SelectionKey interestOps(int ops)
~~~

## Parámetros
* **int ops**,  {% include w3api/param_description.html metodo=_dato parametro="int ops" %}

## Excepciones
[CancelledKeyException](/Java/CancelledKeyException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SelectionKey](/Java/SelectionKey/)

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

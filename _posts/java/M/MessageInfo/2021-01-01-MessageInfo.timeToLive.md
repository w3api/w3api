---
title: MessageInfo.timeToLive()
permalink: /Java/MessageInfo/timeToLive/
date: 2021-01-11
key: Java.M.MessageInfo
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageInfo.metodos valor="timeToLive" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract long timeToLive()
public abstract MessageInfo timeToLive(long millis)
~~~

## Parámetros
* **long millis**,  {% include w3api/param_description.html metodo=_dato parametro="long millis" %}

## Clase Padre
[MessageInfo](/Java/MessageInfo/)

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

---
title: ConnectionEvent.ConnectionEvent()
permalink: Java/ConnectionEvent/ConnectionEvent
date: 2021-01-11
key: JavaJava.C.ConnectionEvent
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConnectionEvent.constructores valor="ConnectionEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ConnectionEvent(PooledConnection con)
public ConnectionEvent(PooledConnection con, SQLException ex)
~~~

## Parámetros
* **SQLException ex**,  {% include w3api/param_description.html metodo=_dato parametro="SQLException ex" %}
* **PooledConnection con**,  {% include w3api/param_description.html metodo=_dato parametro="PooledConnection con" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConnectionEvent](/Java/ConnectionEvent/)

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

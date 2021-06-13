---
title: StatementEvent.StatementEvent()
permalink: /Java/StatementEvent/StatementEvent/
date: 2021-01-11
key: Java.S.StatementEvent
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StatementEvent.constructores valor="StatementEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StatementEvent(PooledConnection con, PreparedStatement statement)
public StatementEvent(PooledConnection con, PreparedStatement statement, SQLException exception)
~~~

## Parámetros
* **PreparedStatement statement**,  {% include w3api/param_description.html metodo=_dato parametro="PreparedStatement statement" %}
* **PooledConnection con**,  {% include w3api/param_description.html metodo=_dato parametro="PooledConnection con" %}
* **SQLException exception**,  {% include w3api/param_description.html metodo=_dato parametro="SQLException exception" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StatementEvent](/Java/StatementEvent/)

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

---
title: StatementEvent.StatementEvent()
permalink: Java/StatementEvent/StatementEvent
date: 2021-01-04
key: JavaJava.S.StatementEvent
category: java
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
* **SQLException exception**,  {% include w3api/param_description.html metodo=_data parametro="SQLException exception" %}
* **PooledConnection con**,  {% include w3api/param_description.html metodo=_data parametro="PooledConnection con" %}
* **PreparedStatement statement**,  {% include w3api/param_description.html metodo=_data parametro="PreparedStatement statement" %}

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
{%- for _ldc in site.data.Java.S.StatementEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

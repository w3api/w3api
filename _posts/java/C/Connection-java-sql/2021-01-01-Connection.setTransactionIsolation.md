---
title: Connection.setTransactionIsolation()
permalink: /Java/Connection-java-sql/setTransactionIsolation/
date: 2021-01-11
key: Java.C.Connection-java-sql
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="setTransactionIsolation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setTransactionIsolation(int level) throws SQLException
~~~

## Parámetros
* **int level**,  {% include w3api/param_description.html metodo=_dato parametro="int level" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[Connection](/Java/Connection-java-sql/)

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

---
title: Statement.setPoolable()
permalink: /Java/Statement-java-sql/setPoolable/
date: 2021-01-11
key: Java.S.Statement-java-sql
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="setPoolable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setPoolable(boolean poolable) throws SQLException
~~~

## Parámetros
* **boolean poolable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean poolable" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[Statement](/Java/Statement-java-sql/)

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

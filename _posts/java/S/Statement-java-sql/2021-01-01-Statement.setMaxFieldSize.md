---
title: Statement.setMaxFieldSize()
permalink: /Java/Statement-java-sql/setMaxFieldSize/
date: 2021-01-11
key: Java.S.Statement-java-sql
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="setMaxFieldSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setMaxFieldSize(int max) throws SQLException
~~~

## Parámetros
* **int max**,  {% include w3api/param_description.html metodo=_dato parametro="int max" %}

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

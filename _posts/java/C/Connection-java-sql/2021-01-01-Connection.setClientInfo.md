---
title: Connection.setClientInfo()
permalink: Java/Connection-java-sql/setClientInfo
date: 2021-01-11
key: JavaJava.C.Connection-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Connection-java-sql.metodos valor="setClientInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setClientInfo(String name, String value) throws SQLClientInfoException
void setClientInfo(Properties properties) throws SQLClientInfoException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}
* **Properties properties**,  {% include w3api/param_description.html metodo=_dato parametro="Properties properties" %}

## Excepciones
[SQLClientInfoException](/Java/SQLClientInfoException/)

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

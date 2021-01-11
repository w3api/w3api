---
title: XMLGregorianCalendar.setYear()
permalink: Java/XMLGregorianCalendar/setYear
date: 2021-01-11
key: JavaJava.X.XMLGregorianCalendar
category: java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLGregorianCalendar.metodos valor="setYear" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setYear(int year)
public abstract void setYear(BigInteger year)
~~~

## Parámetros
* **BigInteger year**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger year" %}
* **int year**,  {% include w3api/param_description.html metodo=_dato parametro="int year" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[XMLGregorianCalendar](/Java/XMLGregorianCalendar/)

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

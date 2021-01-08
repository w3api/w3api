---
title: XMLGregorianCalendar.setYear()
permalink: Java/XMLGregorianCalendar/setYear
date: 2021-01-04
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
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **BigInteger year**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger year" %}

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
{%- for _ldc in site.data.Java.X.XMLGregorianCalendar.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

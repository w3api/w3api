---
title: XMLGregorianCalendar.add()
permalink: /Java/XMLGregorianCalendar/add/
date: 2021-01-11
key: Java.X.XMLGregorianCalendar
category: Java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLGregorianCalendar.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void add(Duration duration)
~~~

## Parámetros
* **Duration duration**,  {% include w3api/param_description.html metodo=_dato parametro="Duration duration" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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

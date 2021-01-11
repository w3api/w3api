---
title: XMLGregorianCalendar.toGregorianCalendar()
permalink: Java/XMLGregorianCalendar/toGregorianCalendar
date: 2021-01-11
key: JavaJava.X.XMLGregorianCalendar
category: java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLGregorianCalendar.metodos valor="toGregorianCalendar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract GregorianCalendar toGregorianCalendar()
public abstract GregorianCalendar toGregorianCalendar(TimeZone timezone, Locale aLocale, XMLGregorianCalendar defaults)
~~~

## Parámetros
* **Locale aLocale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale aLocale" %}
* **TimeZone timezone**,  {% include w3api/param_description.html metodo=_dato parametro="TimeZone timezone" %}
* **XMLGregorianCalendar defaults**,  {% include w3api/param_description.html metodo=_dato parametro="XMLGregorianCalendar defaults" %}

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

---
title: JAXBException.printStackTrace()
permalink: Java/JAXBException/printStackTrace
date: 2021-01-11
key: JavaJava.J.JAXBException
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JAXBException.metodos valor="printStackTrace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void printStackTrace()
public void printStackTrace(PrintStream s)
public void printStackTrace(PrintWriter s)
~~~

## Parámetros
* **PrintWriter s**,  {% include w3api/param_description.html metodo=_dato parametro="PrintWriter s" %}
* **PrintStream s**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream s" %}

## Clase Padre
[JAXBException](/Java/JAXBException/)

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

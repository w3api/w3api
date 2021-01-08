---
title: JAXBContext.createBinder()
permalink: Java/JAXBContext/createBinder
date: 2021-01-04
key: JavaJava.J.JAXBContext
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JAXBContext.metodos valor="createBinder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Binder<Node> createBinder()
<T> Binder<T> createBinder(Class<T> domType)
~~~

## Parámetros
* **Class&lt;T&gt; domType**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> domType" %}

## Clase Padre
[JAXBContext](/Java/JAXBContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JAXBContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
